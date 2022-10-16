import time; start = time.perf_counter() #Since it also takes time to Import libs, I allways start the timer asap. 
import pandas as pd
from tqdm import tqdm
from multiprocessing import Pool

''' ___ local imports __________'''
from config import tablenames
from postgres import databaseManager, getInputTable, checkIfMissing, deleteData
from file_manager import *
from base_extractor import genSearchTerm, pullRequest


''' 
	* CURRENT EXTRACTION TIME *
		- Amount of companies : 6034  
		- Finished in 11.2 second(s)
'''

def linkBuilder(base_url, term):
	if isinstance(term, int):
		return f'{base_url}/{term}/bedrifter'
	else:
		return f'{base_url}/{genSearchTerm(term)}/bedrifter'

def getCompanyInfoLinks(cont):
	a = cont.find('a',{'href' : True})
	href = a['href']
	base_url = 'https://www.gulesider.no'
	new_url = base_url + href
	return new_url

def getNewLinks(soup):
	'''
	first: get full list of search results ['article', {'class':'CompanyResultListItem'}]
	'''
	result_list = soup.findAll('article', {'class':'CompanyResultListItem'})
	result_list = [i for i in result_list]
	try:
		new_links = [getCompanyInfoLinks(cont) for cont in result_list ][0]
	except:
		new_links = None
	return new_links
""" #! OLD GET DATA, KEEP IN CASE YOU NEED MORE DATA LATER
	def getData(soup):
		''' CHECK_PAYED_ENTRY'''
		if soup.find('div', { 'class': "SearchWords company-tags--section" }):
			has_payed_entry = True

			''' ORG_NUM '''
			try:
				org_num = soup.find("strong", text = "Org.nr:").next_sibling.text
				org_num = int(org_num.replace(' ',''))
			except:
				org_num = None

			''' GET_COMPANY_NAME '''
			if [i for i in soup.find('h1', { 'role': "name" })]:
				company_name = soup.find('h1', { 'role': "name" }).text
			else:
				company_name = []

			''' GET_PHONE_NUMBER '''
			try:
				phone_number = [item.text for item in soup.find('div', { 'class': "phoneList"})][0]	
			except:
				phone_number = None

			''' GET_STAFF '''
			try:
				staff = [i for i in soup.find('div', { 'class': "roles" })]
			except TypeError:
				staff = []

			'''	MANAGER '''		
			try:
				manager = staff[0].find('div', { 'class': "rolename e-icon-user" }).text
			except:
				manager = None

			'''	OWNER '''
			if len(staff)>1:
				if staff[1].find('div', { 'class': "rolename e-icon-user" }).text:
					owner = staff[1].find('div', { 'class': "rolename e-icon-user" }).text
				else:
					owner = None
			else:
				owner = None

			result = pd.DataFrame([[ org_num, company_name, has_payed_entry, phone_number,
									manager, owner, ]], 
					columns = [		'org_num', 'navn', 'betalt_oppføring', 'tlf', 'daglig_leder', 
									'styreleder', ])
			return result
"""

def getData(soup):
	''' CHECK_PAYED_ENTRY'''
	if soup.find('div', { 'class': "SearchWords company-tags--section" }):
		has_payed_entry = True

		''' ORG_NUM '''
		try:
			org_num = soup.find("strong", text = "Org.nr:").next_sibling.text
			org_num = int(org_num.replace(' ',''))
		except:
			org_num = None

		''' GET_COMPANY_NAME '''
		if [i for i in soup.find('h1', { 'role': "name" })]:
			company_name = soup.find('h1', { 'role': "name" }).text
		else:
			company_name = []

	return pd.DataFrame([[ org_num, company_name, has_payed_entry,]], 
				columns = ['org_num', 'navn', 'betalt_oppføring',])

def makeChunks(input_array, chunksize):
	return [input_array[i:i+chunksize] for i in range(0, len(input_array), chunksize)]  

def makeDataframe():
		return pd.DataFrame( columns = ['org_num', 'navn', 'betalt_oppføring', 'tlf', 'daglig_leder', 
										'styreleder', 'er_Eierbekreftet', ])

def errorManager(org_num, search_term, source, url, e):
	tablename = 'error_table'
	df = pd.DataFrame([[org_num, search_term, source, url, e]], columns = ['org_num', 'search_term', 'source', 'url', 'error_message'])
	next_result = 0
	while next_result == 0:
		try:
			databaseManager(df, tablename)
			next_result = 1
		except:
			continue
		break

def extractionManager(input_array):
	org_num = input_array[0]
	search_term = input_array[1]
	
	if not checkIfMissing(org_num):
		source = 'gulsesider.py'
		base_url = 'https://www.gulesider.no'
		url = linkBuilder(base_url, str(org_num))  		
		soup = pullRequest(url) 
		new_link = getNewLinks(soup)
		if new_link is None:
			e = f'Error: "{search_term}" gave no search results'
			errorManager(org_num, search_term, source, url, e)
		elif new_link is not None:
			soup = pullRequest(new_link)
			if soup is None:
				print("soup == None")
			df = getData(soup)
			deleteData(org_num, tablename = "input_table") #* All inputs that are found can be deleted from input_table 
			if df is not None:
				return org_num, search_term
		else:
			e = 'unknown error in: gulesider.py -> extractionManager()'
			errorManager(org_num, search_term, source, url, e)

#* _____ MAIN __________________________
def gulesiderExtractor(**kwargs):
	'''
		sets up all nessasary functions, 
		then gets list of company names, 
		then iterates through the list via multithreading: claimedStatus().
	'''
	print("_"*62)
	print("|                Starting: Gulesider Extractor               |")
	print("_"*62)
	print()
	
	''' fetching data from config '''
	file_name = getFileName() 
	settings = parseSettings(file_name)
	chunksize = settings['chunk_size']
	input_array = getInputTable(tablenames['input']).to_numpy() 

	''' making adjustments if testmode '''
	if kwargs.get('testmode', None):
		input_array = input_array[129500:] #TEMP TEMP TEMP

	print(f"chunksize: {chunksize}")
	print(f"input length: {len(input_array)}")
	nested_input_array = makeChunks(input_array, chunksize) 
	print(f"number of chunks: {len(nested_input_array)}")
	with tqdm(total = len(nested_input_array)) as pbar:
		for input_array in nested_input_array:
			with Pool() as pool:
				results = list(tqdm(pool.imap_unordered(extractionManager, input_array), total = len(input_array)))
				results = [x for x in results if x is not None]
				df =  pd.DataFrame(results, columns = ['org_num', 'navn'])
				print(df)
				databaseManager(df, tablename = "gulesider_output_table")
				pbar.update(1) 
	print("_"*62)
	print("                   Data Extraction Complete.                 ")
	print(f"                  Finished in {round(time.perf_counter() - start, 2)} second(s)                 ")
	print("_"*62)
	print()

if __name__ == '__main__':
	gulesiderExtractor(testmode = True)
	# gulesiderExtractor(testmode = False)

















''' TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP  TEMP TEMP TEMP TEMP TEMP  TEMP TEMP TEMP TEMP 
							
*							_____ WHERE I LEFT OF _____
*						[08.08.22]


*						_____ EXTRACTION RECORD _______
*						Extracts (668.5K) units  --> 	36170.92 second(s)			| => (1000) :  256.83 sec | [0.054 s/unit]				
 				   		Extracts (1000) units 	 -->  	51.00 second(s) 			| => (1000) :  51.00 sec  | [0.051 s/unit]
 				   AVG: Extracts (500) units 	 -->  	18.25 second(s) 			| => (1000) :  36.50 sec  | [0.037 s/unit]
 						Extracts (100) units 	 -->  	20.76 second(s)				  
						Extracts (500) units 	 -->    19.54 second(s) 
						Extracts (500) units 	 -->    16.97 second(s)


*						_____ ESTIMATIONS _______
*						Estimated length of input_list: 						1.069.577 rows / [1069577]
*						Estimated total extraction time: 						[16:04:32] / 964.54 minutes
* 						ACTUAL TOTAL EXTRACTION TIME: 							[--:--:--] / ---.-- minutes

10:02:50

TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP  TEMP TEMP TEMP TEMP TEMP  TEMP TEMP TEMP TEMP TEMP '''



#* [INACTIVE] def visabilityTest(data):
"""	'''
	BONUS TEST SYNLIGHET
		example link: https://nettsjekk.gulesider.no/?utm_source=gulesider&utm_medium=corefront&utm_campaign=netcheck&companyName=Felleskatalogen%20AS&phoneNumber=23%2016%2015%2050&street=Essendrops%20gate%203&postCode=0368&postArea=Oslo
		we should be able to get these from the proff_data.csv
			note: the parameters might need to be formated correctly
				--> replace(' ', '%20')
			Will use insomnia or charlie for further testing
	'''

	''' _____________ TEST INPUT _____________'''
	company_name = 'Felleskatalogen%20AS'
	tlf = '23%2016%2015%2050'
	address = 'Essendrops%20gate%203'
	post_code = '0368' 
	post_area = 'Oslo'
	base_url = 'https://nettsjekk.gulesider.no/?utm_source=gulesider&utm_medium=corefront&utm_campaign=netcheck&'
	

	url = f'''
	{base_url}
	companyName={company_name}&
	phoneNumber={tlf}&
	street={address}&
	postCode={post_code}&
	postArea={post_area}
	'''

	''' Antall final url, dette skal sjekkes opp i.. '''
	fullname = 'Ole%20Nordmann'	  #---> will use randomly generated names if needed  
	email = 'example@hotmail.com' #---> will use randomly generated emails 
	final_url = f'{url}&fullName={fullname}&email={email}'
"""