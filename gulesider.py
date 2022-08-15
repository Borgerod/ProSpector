''' TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP 
							
							_____ WHERE I LEFT OF _____
						[08.08.22]

						legg til en kode som fjerner navn fra imput_list når et bedrift har blitt suksessfullt skrapet.

						NOTE 400 enheter --> Finished in 119.64 second(s)

- TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP '''


import time; start = time.perf_counter() #Since it also takes time to Import libs, I allways start the timer asap. 
import requests
from bs4 import BeautifulSoup
from fake_headers import Headers
import pandas as pd
import pprint
import os.path
from os import path
from tqdm import tqdm
import concurrent.futures
import os.path
import numpy as np
# ___ local imports __________
from config import payload, tablenames, settings
from postgres import databaseManager, getInputTable
from file_manager import *
from input_table import inputTable

'''
	* CURRENT EXTRACTION TIME *
		- Amount of companies : 6034  
		- Finished in 11.2 second(s)
'''
	
'''
TODO :
	- [X] bytt ut CSV  med database
	- [X] implementer file_manager
	- [ ] implementer error management
	- [ ] utfør ett av løsningsforslagene til "mangfoldig søkeresultat"
	- [ ] endre på org_num til å være str of ikke flaot
TODO optional:
	- [ ] lag en "validator"; sjekker om org_num og search_term == søkeresultatet.  
'''

'''
* RUNDOWN OF THE PROGRAM:
	[...]
	[...]
'''

'''
! NOTABLE FLAWS: 
	[ ... ]
	[ ... ]
'''

'''
# ENIRO (GULESIDER) API ------> NOT IN USE
api_key = '3BNyz2rRWW4wXOUGDsVz5RLXI_FThV4FmSkrE2LYSUY'
'''

def getInput():
	'''
	imports proff_data.csv from the proff folder
	'''
	inputs = pd.read_csv('../_output_data/proff_data.csv')
	return inputs

def getInputNames():
	'''
	returns company names ['bedrift'] from input dataframe
	'''
	inputs = getInput()
	companies = inputs['bedrift']
	# return company_names

	''' optional; return as np array '''
	return companies.to_numpy()
	 
def genSearchTerm(company):
	'''
	build a search phrase based on company name
	'''
	search_term = company.replace(' ', '+')
	return search_term

def linkBuilder(company):
	'''
	builds a search url based on only company name
	'''
	base_url = 'https://www.gulesider.no'
	url = f'{base_url}/{genSearchTerm(company)}/bedrifter'
	return url

def pullRequest(url, source, org_num, search_term):
	'''
	1. makes a pull request from gulesider.no.
	2. then checks the connection.
	3. then returns a soup.
	4. If a bad request occours; then it will save the error to "gulesider_error_table"
	'''
	r = requests.get(url, timeout = 10)
	soup = BeautifulSoup(r.content, "html.parser")
	r.raise_for_status()
	# * [ikke fjern koden under]
		# try:
		# 	r = requests.get(url, timeout = 10)
		# 	soup = BeautifulSoup(r.content, "html.parser")
		# 	r.raise_for_status()

		
		# except (requests.exceptions.RequestException, ValueError) as e:
		# 	''' 
		# 	if exception occurred:
		# 		- prints error & related url
		# 		- sends the faulty url (++) to errorSave() from error_save.py for later use
		# 		- returns an empty soup
		# 	'''	
		# 	print("="*91)
		# 	print("|											  |")
		# 	print("|				WARNING: ERROR CAUGHT! 				  |")
		# 	print("|											  |")
		# 	print("="*91)
		# 	print(f'					{print(e)}')
		# 	errorManager(org_num, search_term, url, e)
		# 	# errer_df = pd.DataFrame([org_num, search_term, url, e], columns = ['org_num', 'search_term', 'url', 'error_message'])
		# 	# errorSave(url, e, source) #Currently not in nuse (not yet finished)
		# 	# soup = ""
			# pass 
	return soup



def getCompanyInfoLinks(cont):
	a = cont.find('a',{'href' : True})
	href = a['href']
	base_url = 'https://www.gulesider.no'
	new_url = base_url + href
	return new_url

def getNewLinks(soup, url):
	'''
	first: get full list of search results ['article', {'class':'CompanyResultListItem'}]
	'''
	# GET RESULTLSIT 
	result_list = soup.findAll('article', {'class':'CompanyResultListItem'})
	result_list = [i for i in result_list]

	# GET LIST COMPANY INFO URLS
	try:
		new_links = [getCompanyInfoLinks(cont) for cont in result_list ][0]
	except:
		new_links = None
	return new_links
 
# def getData(soup, url):

# 	''' GET_COMPANY_NAME '''
# 	if [i for i in soup.find('h1', { 'role': "name" })]:
# 		company_name = soup.find('h1', { 'role': "name" }).text
# 	else:
# 		company_name = []

# 	''' GET_PHONE_NUMBER '''
# 	try:
# 		phone_number = [item.text for item in soup.find('div', { 'class': "phoneList"})][0]	
# 		# hrefs = [item['href'] for item in soup.findAll('a', { 'class': "yextLink", 'href': True })] 
# 		# phone_number = ""
# 		# for href in hrefs:
# 		# 	if "phoneNumber" in href:
# 		# 		phone_number = re.split('phoneNumber=|&street',href)[1]
# 	except:
# 		phone_number = None

# 	''' GET_STAFF '''
# 	# if soup.find('div', { 'class': "roles" }):
# 	if [i for i in soup.find('div', { 'class': "roles" })]:
# 		staff = [i for i in soup.find('div', { 'class': "roles" })]
# 	else:
# 		staff = []

# 	'''	MANAGER '''		
# 	if staff[0].find('div', { 'class': "rolename e-icon-user" }).text:
# 		manager = staff[0].find('div', { 'class': "rolename e-icon-user" }).text
# 	else:
# 		manager = None
	

# 	'''	OWNER '''
# 	if len(staff)>1:
# 		if staff[1].find('div', { 'class': "rolename e-icon-user" }).text:
# 			owner = staff[1].find('div', { 'class': "rolename e-icon-user" }).text
# 		else:
# 			owner = None
# 	else:
# 		owner = None

	
# 	''' ORG_NUM '''
# 	if soup.find("strong", text = "Org.nr:").next_sibling.text:
# 		org_num = soup.find("strong", text = "Org.nr:").next_sibling.text
# 		org_num = int(org_num.replace(' ',''))
# 	else:
# 		org_num=None

	
# 	''' IS_CLAIMED?
# 			false:	company is NOT claimed and are possible clients
# 			true: 	company is decleared but could still be potential clients '''
# 	is_claimed = soup.find('div', { 'class': "Yext card full" })
# 	if not is_claimed.find('h2'):         
# 		is_claimed = True
# 	else: 
# 		is_claimed = False


# 	''' HAS_DESCRIPTION?
# 			false:	company has NO description and are possible clients
# 			true: 	company has description but could still be potential clients '''
# 	if soup.find('div', { 'class': 'companyDescription card' }):
# 		has_description = True
# 	else: 
# 		has_description = False
	

# 	''' HAS_FREETEXT?
# 			false:	company has NO freetext and are possible clients
# 			true: 	company has freetext but could still be potential clients '''
# 	if soup.find('div', { 'class': 'freeTextContainer card' }):
# 		has_freetext = True
# 	else: 
# 		has_freetext = False	


# 	''' HAS_DEEPLINKS?
# 			false:	company has NO deeplinks and are possible clients
# 			true: 	company has deeplinks but could still be potential clients '''
# 	if soup.find('div', { 'class': 'deeplinks card full' }):
# 		has_deeplinks = True
# 	else: 
# 		has_deeplinks = False	


# 	''' HAS_SEO?
# 			false:	company has NO seo and are possible clients
# 			true: 	company has seo but could still be potential clients '''
# 	if soup.find('div', { 'class': 'SearchWords company-tags--section' }):
# 		has_seo = True
# 	else: 
# 		has_seo = False	


# 	''' HAS_PREMIUM_SEO?
# 			false:	company has NO premium_seo and are possible clients
# 			true: 	company has premium_seo but could still be potential clients '''
# 	if soup.find('div', { 'class': 'PremiumSearchWords' }):
# 		has_premium_seo = True
# 	else: 
# 		has_premium_seo = False	

# 	''' HAS_FACEBOOK?
# 			false:	company has NO facebook and are possible clients
# 			true: 	company has facebook but could still be potential clients '''
# 	if soup.find('div', { 'class': 'facebook' }):
# 		facebook = soup.find("a", {'class':"e-icon e-icon-facebook"})['href']
# 		has_facebook = True
# 	else: 
# 		has_facebook = False
# 		facebook = None

# 	''' HAS_HOURS?
# 			false:	company has NO opening hours and are possible clients
# 			true: 	company has opening hours but could still be potential clients''' 
# 	if soup.find('div', { 'class': 'item openingHoursWrapper e-icon e-icon-clock collapsed' }):	
# 		has_hours = True
# 	else: 
# 		has_hours = False

# 	''' HAS_EMAIL?
# 			false:	company has NO Email and are possible clients
# 			true: 	company has Email but could still be potential clients''' 
# 	if soup.find('div', { 'class': 'item email' }):	
# 		has_email = True
# 	else: 
# 		has_hours = False

# 	df = pd.DataFrame([[ 	 org_num, company_name, phone_number,
# 							 manager, owner, is_claimed, has_description, 
# 							 has_freetext, has_deeplinks, has_seo, 
# 							 has_premium_seo, has_hours, has_facebook, facebook, 	]], 
# 			columns = [		'org_num', 'navn', 'tlf', 'daglig_leder', 
# 							'styreleder', 'er_Eierbekreftet', 'har_Beskrivelse', 
# 							'har_Fritekst', 'har_Dyplenker', 'har_SEO', 'har_Premium_SEO', 
# 							'har_Åpningstider', 'har_Facebook', 'facebook'					])
# 	return df


def getData(soup, url):

	''' GET_COMPANY_NAME '''
	if [i for i in soup.find('h1', { 'role': "name" })]:
		company_name = soup.find('h1', { 'role': "name" }).text
	else:
		company_name = []

	''' GET_PHONE_NUMBER '''
	try:
		phone_number = [item.text for item in soup.find('div', { 'class': "phoneList"})][0]	
		# hrefs = [item['href'] for item in soup.findAll('a', { 'class': "yextLink", 'href': True })] 
		# phone_number = ""
		# for href in hrefs:
		# 	if "phoneNumber" in href:
		# 		phone_number = re.split('phoneNumber=|&street',href)[1]
	except:
		phone_number = None

	''' GET_STAFF '''
	# if soup.find('div', { 'class': "roles" }):
	# if [i for i in soup.find('div', { 'class': "roles" })]:
	try:
		staff = [i for i in soup.find('div', { 'class': "roles" })]
	except TypeError:
		staff = []
	# else:
	# 	staff = []

	'''	MANAGER '''		
	# if staff[0].find('div', { 'class': "rolename e-icon-user" }).text:
	try:
		manager = staff[0].find('div', { 'class': "rolename e-icon-user" }).text
	# else:
		# manager = None
	except:
		manager = None

	# '''	MANAGER '''
	# if staff.empty:	
	# 	manager = None
	# else:
	# 	try:

	# # if staff[0].find('div', { 'class': "rolename e-icon-user" }).text:
	# # try:
	# 		manager = staff[0].find('div', { 'class': "rolename e-icon-user" }).text
	# # else:
	# # 	manager = None
	# 	except:
	# 		manager = None


	'''	OWNER '''
	if len(staff)>1:
		if staff[1].find('div', { 'class': "rolename e-icon-user" }).text:
			owner = staff[1].find('div', { 'class': "rolename e-icon-user" }).text
		else:
			owner = None
	else:
		owner = None

	
	''' ORG_NUM '''
	# if soup.find("strong", text = "Org.nr:").next_sibling.text:
	try:
		org_num = soup.find("strong", text = "Org.nr:").next_sibling.text
		org_num = int(org_num.replace(' ',''))
	# else:
	except:
		org_num=None

	
	''' IS_CLAIMED?
			false:	company is NOT claimed and are possible clients
			true: 	company is decleared but could still be potential clients '''
	is_claimed = soup.find('div', { 'class': "Yext card full" })
	if not is_claimed.find('h2'):         
		is_claimed = True
	else: 
		is_claimed = False


	''' HAS_DESCRIPTION?
			false:	company has NO description and are possible clients
			true: 	company has description but could still be potential clients '''
	if soup.find('div', { 'class': 'companyDescription card' }):
		has_description = True
	else: 
		has_description = False
	

	''' HAS_FREETEXT?
			false:	company has NO freetext and are possible clients
			true: 	company has freetext but could still be potential clients '''
	if soup.find('div', { 'class': 'freeTextContainer card' }):
		has_freetext = True
	else: 
		has_freetext = False	


	''' HAS_DEEPLINKS?
			false:	company has NO deeplinks and are possible clients
			true: 	company has deeplinks but could still be potential clients '''
	if soup.find('div', { 'class': 'deeplinks card full' }):
		has_deeplinks = True
	else: 
		has_deeplinks = False	


	''' HAS_SEO?
			false:	company has NO seo and are possible clients
			true: 	company has seo but could still be potential clients '''
	if soup.find('div', { 'class': 'SearchWords company-tags--section' }):
		has_seo = True
	else: 
		has_seo = False	


	''' HAS_PREMIUM_SEO?
			false:	company has NO premium_seo and are possible clients
			true: 	company has premium_seo but could still be potential clients '''
	if soup.find('div', { 'class': 'PremiumSearchWords' }):
		has_premium_seo = True
	else: 
		has_premium_seo = False	

	''' HAS_FACEBOOK?
			false:	company has NO facebook and are possible clients
			true: 	company has facebook but could still be potential clients '''
	if soup.find('div', { 'class': 'facebook' }):
		facebook = soup.find("a", {'class':"e-icon e-icon-facebook"})['href']
		has_facebook = True
	else: 
		has_facebook = False
		facebook = None

	''' HAS_HOURS?
			false:	company has NO opening hours and are possible clients
			true: 	company has opening hours but could still be potential clients	''' 
	if soup.find('div', { 'class': 'item openingHoursWrapper e-icon e-icon-clock collapsed' }):	
		has_hours = True
	else: 
		has_hours = False

	''' HAS_EMAIL?
			false:	company has NO Email and are possible clients
			true: 	company has Email but could still be potential clients	''' 
	if soup.find('div', { 'class': 'item email' }):	
		has_email = True
	else: 
		has_hours = False
	# [array verrion]
		# result_array = np.array([ 	 org_num, company_name, phone_number,
		# 						 manager, owner, is_claimed, has_description, 
		# 						 has_freetext, has_deeplinks, has_seo, 
		# 						 has_premium_seo, has_hours, has_facebook, facebook, 	])
	result = pd.DataFrame([[ org_num, company_name, phone_number,
							 manager, owner, is_claimed, has_description, 
							 has_freetext, has_deeplinks, has_seo, 
							 has_premium_seo, has_hours, has_facebook, facebook, 	]], 
			columns = [		'org_num', 'navn', 'tlf', 'daglig_leder', 
							'styreleder', 'er_Eierbekreftet', 'har_Beskrivelse', 
							'har_Fritekst', 'har_Dyplenker', 'har_SEO', 'har_Premium_SEO', 
							'har_Åpningstider', 'har_Facebook', 'facebook'					])
	return result



def makeDataframe():
		return pd.DataFrame( columns = ['org_num', 'navn', 'tlf', 'daglig_leder', 
										'styreleder', 'er_Eierbekreftet', 'har_Beskrivelse', 
										'har_Fritekst', 'har_Dyplenker', 'har_SEO', 'har_Premium_SEO', 
										'har_Åpningstider', 'har_Facebook', 'facebook'					])

def visabilityTest(data):
	'''
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

def errorManager(org_num, search_term, url, e):
	# try:
	tablename = 'gulesider_error_table'
	df = pd.DataFrame([[org_num, search_term, url, e]], columns = ['org_num', 'search_term', 'url', 'error_message'])
	next_result = 0
	while next_result == 0:
		try:
			databaseManager(result, tablename)
			next_result = 1
		except:
			continue
		break

#* _____ MAIN __________________________
def extractionManager(input_array):
	org_num = input_array[0]
	search_term = input_array[1]
	source = 'gulsesider.py'
	url = linkBuilder(org_num)  		
	soup = pullRequest(url, source, org_num, search_term) 
	new_link = getNewLinks(soup, url)
	if new_link is None:
		e = f'Error: "{search_term}" gave no search results'
		errorManager(org_num, search_term, url, e)
	elif new_link is not None:
		soup = pullRequest(new_link, source, org_num, search_term)
		if soup is None:
			print("soup == None")
		result_array = getData(soup, new_link)
		if result_array is None:
			print("soup == None")
		return result_array
	else:
		e = 'unknown error in: gulesider.py -> extractionManager()'
		errorManager(org_num, search_term, url, e)
		return 

def gulesiderExtractor(testmode):

	
	'''
		sets up all nessasary functions, 
		then gets list of company names, 
		then iterates through the list via multithreading: claimedStatus().
	'''
	print("_"*91)
	print("|											  |")
	print("|			    Starting: GULESIDER EXTRACTOR 				  |")
	print("|											  |")
	print("_"*91)
	print()

	''' preperations: parse config, connect to database and connect to api manager '''

	''' fetching data from config '''
	file_name = getFileName() # fetches name of current file 
	tablename = parseTablenames(file_name) # fetches the appropriate tablename for current file
	settings = parseSettings(file_name)	# fetches the appropriate settings for current file
	input_array = getInputTable(tablenames['input_table'])

	''' temporary code for testing '''
	# if testmode == 'on':
	# 	input_array = input_array[:100] 	# TEMP TEMP TEMP TEMP TEMP TEMP
	# input_array = input_array[99:] 	# TEMP TEMP TEMP TEMP TEMP TEMP

	with tqdm(total = len(input_array)) as pbar:
		with concurrent.futures.ThreadPoolExecutor() as executor:
				results = executor.map(extractionManager, input_array)
				for result in results:
					if result is not None:
						next_result = 0
						while next_result == 0:
							try:
								databaseManager(result, tablename)
								next_result = 1
							except:
								continue
							break
					# deleteData(result['org_num'], tablename = 'input_table')
					pbar.update(1)
	print("																		"+"_"*91)
	print("																		|											  |")
	print("																		|				   Data Extraction Complete. 				  |")
	print("																		|											  |")
	print("																		"+"_"*91)
	print()			
	print(f"																		|				   Finished in {round(time.perf_counter() - start, 2)} second(s)				  |")



# if __name__ == '__main__':
	# '''
	# 	sets up all nessasary functions, 
	# 	then gets list of company names, 
	# 	then iterates through the list via multithreading: claimedStatus().
	# '''
	# print("_"*91)
	# print("|											  |")
	# print("|			    Starting: GULESIDER EXTRACTOR 				  |")
	# print("|											  |")
	# print("_"*91)
	# print()

	# ''' preperations: parse config, connect to database and connect to api manager '''

	# ''' fetching data from config '''
	# file_name = getFileName() # fetches name of current file 
	# tablename = parseTablenames(file_name) # fetches the appropriate tablename for current file
	# settings = parseSettings(file_name)	# fetches the appropriate settings for current file
	# input_array = getInputTable(tablenames['input_table'])

	# ''' temporary code for testing '''
	# # input_array = input_array[:100] 	# TEMP TEMP TEMP TEMP TEMP TEMP
	# with tqdm(total = len(input_array)) as pbar:
	# 	with concurrent.futures.ThreadPoolExecutor() as executor:
	# 			results = executor.map(extractionManager, input_array)
	# 			for result in results:
	# 				if result is not None:
	# 					next_result = 0
	# 					while next_result == 0:
	# 						try:
	# 							databaseManager(result, tablename)
	# 							next_result = 1
	# 						except:
	# 							continue
	# 						break
	# 				pbar.update(1)
	# print("																		"+"_"*91)
	# print("																		|											  |")
	# print("																		|				   Data Extraction Complete. 				  |")
	# print("																		|											  |")
	# print("																		"+"_"*91)
	# print()			
	# print(f"																		|				   Finished in {round(time.perf_counter() - start, 2)} second(s)				  |")



if __name__ == '__main__':	
	'''
		sets up all nessasary functions, 
		then gets list of company names, 
		then iterates through the list via multithreading: claimedStatus().
	'''
	print("_"*91)
	print("|											  |")
	print("|			    Starting: GULESIDER EXTRACTOR 				  |")
	print("|											  |")
	print("_"*91)
	print()

	''' preperations: parse config, connect to database and connect to api manager '''

	''' fetching data from config '''
	file_name = getFileName() # fetches name of current file 
	tablename = parseTablenames(file_name) # fetches the appropriate tablename for current file
	settings = parseSettings(file_name)	# fetches the appropriate settings for current file
	input_array = getInputTable(tablenames['input_table'])

	''' temporary code for testing '''
	# if testmode == 'on':
	# 	input_array = input_array[:100] 	# TEMP TEMP TEMP TEMP TEMP TEMP
	input_array = input_array[100:] 	# TEMP TEMP TEMP TEMP TEMP TEMP

	with tqdm(total = len(input_array)) as pbar:
		with concurrent.futures.ThreadPoolExecutor() as executor:
				results = executor.map(extractionManager, input_array)
				for result in results:
					if result is not None:
						next_result = 0
						while next_result == 0:
							try:
								databaseManager(result, tablename)
								next_result = 1
							except:
								continue
							break
					deleteData(org_num, tablename = 'input_table')
					pbar.update(1)
	print("																		"+"_"*91)
	print("																		|											  |")
	print("																		|				   Data Extraction Complete. 				  |")
	print("																		|											  |")
	print("																		"+"_"*91)
	print()			
	print(f"																		|				   Finished in {round(time.perf_counter() - start, 2)} second(s)				  |")









	
	# #* FOR TESTING: extractionManager
	# with concurrent.futures.ThreadPoolExecutor() as executor:
	# 		results = executor.map(extractionManager, input_array)
	# 		for result in results:
	# 			if result is not None:
	# 				databaseManager(result, tablename)


























# def extractionManager(input_array):
# 	org_num = input_array[0]
# 	search_term = input_array[1]
# 	source = 'gulsesider.py'
# 	url = linkBuilder(org_num)  		
# 	soup = pullRequest(url, source, org_num, search_term) 
# 	new_link = getNewLinks(soup, url)

# 	'''Try-except version'''
# 		# try:
# 		# 	soup = pullRequest(new_link, source, org_num, search_term)
# 		# 	df = getData(soup, new_link)
# 		# 	return df
# 		# except Exception as e:
# 		# 	errorManager(org_num, search_term, url, e)

# 	''' only if version '''
# 		# if new_link is None:
# 		# 	e = f'Error: "{search_term}" gave no search results'
# 		# 	errorManager(org_num, search_term, url, e)
# 		# elif new_link is not None:
# 		# 	soup = pullRequest(new_link, source, org_num, search_term)
# 		# 	df = getData(soup, new_link)
# 		# 	return df
# 		# else:
# 		# 	e = 'unknown error in: gulesider.py -> extractionManager()'
# 		# 	errorManager(org_num, search_term, url, e)

# 	''' if + try version '''
# 	if new_link is None:
# 		e = f'Error: "{search_term}" gave no search results'
# 		errorManager(org_num, search_term, url, e)
# 	elif new_link is not None:
# 		soup = pullRequest(new_link, source, org_num, search_term)
# 		if soup is None:
# 			print("soup == None")
# 		df = getData(soup, new_link)
# 		if df is None:
# 			print("soup == None")
# 		return df, url
# 	else:
# 		e = 'unknown error in: gulesider.py -> extractionManager()'
# 		errorManager(org_num, search_term, url, e)
# 		return 

# 	# [OLD CODE]
# 	# try:
# 	# 	try:
# 	# 		soup = [pullRequest(url, source) for url in new_link_list ][0]
# 	# 		# soup_list = [pullRequest(url, source) for url in new_link_list ]#[0]
# 	# 		# comp_data_list = [getData(soup) for soup in soup_list]
# 	# 		df = getData(soup, url)
# 	# 		# df = [getData(soup, url) for soup, url in zip(soup_list, new_link_list)]
# 	# 		# df_new = makeDataframe()
# 	# 		# for df, url in comp_data_list:

# 	# 		# 	df_new = pd.concat([df_new, df], axis = 0)
# 	# 		# 	print(df)
# 	# 		return df
# 	# 	except:
# 	# 		url = linkBuilder(search_term)  		#Note: built for 1 unit not multiple units
# 	# 		soup = pullRequest(url, source)		#Note: built for 1 unit not multiple units
# 	# 		new_link_list = getNewLinks(soup) 	#Gets a list of links for additional info
# 	# 		soup = [pullRequest(url, source) for url in new_link_list ][0]
# 	# 		# soup_list = [pullRequest(url, source) for url in new_link_list ]#[0]

# 	# 		# comp_data_list = [getData(soup) for soup in soup_list]
# 	# 		df = getData(soup, url)
# 	# 		# df = [getData(soup, url) for soup, url in zip(soup_list, new_link_list)]
# 	# 		# df_new = makeDataframe()
# 	# 		# for df, url in comp_data_list:

# 	# 		# 	df_new = pd.concat([df_new, df], axis = 0)
# 	# 		# 	print(df)
# 	# 		return df
# 	# except Exception as e:
# 	# 	errorManager(org_num, search_term, url)

# if __name__ == '__main__':
# 	'''
# 		sets up all nessasary functions, 
# 		then gets list of company names, 
# 		then iterates through the list via multithreading: claimedStatus().
# 	'''
# 	print("_"*91)
# 	print("|											  |")
# 	print("|			    Starting: GULESIDER EXTRACTOR 				  |")
# 	print("|											  |")
# 	print("_"*91)
# 	print()

# 	''' preperations: parse config, connect to database and connect to api manager '''

# 	''' fetching data from config '''
# 	file_name = getFileName() # fetches name of current file 
# 	tablename = parseTablenames(file_name) # fetches the appropriate tablename for current file
# 	settings = parseSettings(file_name)	# fetches the appropriate settings for current file
# 	input_array = getInputTable(tablenames['input_table'])

# 	''' temporary code for testing '''
# 	input_array = input_array[:10] 	# TEMP TEMP TEMP TEMP TEMP TEMP
# 	# for i, chunk in enumerate(companies):

# 	#* FOR NORMAL RUN 
# 		# with tqdm(total = len(input_array)) as pbar:
# 		# 	with concurrent.futures.ThreadPoolExecutor() as executor:
# 		# 			results = executor.map(extractionManager, input_array)
# 		# 			for df in results:
# 		# 				print("_"*100)
# 		# 				print('printing result from multithread:')	
# 		# 				print(f'line: {getLineNumber()}, print(result): \n{df}')
# 		# 				print()
# 		# 				print(type)
# 		# 				databaseManager(df, tablename)
# 		# 				pbar.update(1)
# 		# 				# pass
	
# 	#* FOR TESTING: extractionManager
# 	with concurrent.futures.ThreadPoolExecutor() as executor:
# 			results = executor.map(extractionManager, input_array)
# 			print(pd.DataFrame(results[0]), columns=[results[1]])	
# 			# for result in results:
# 			# 	time.sleep(0.1)
# 			# 	print(f"{result[0]}\n{result[1]}")
# 			# 	print("-"*100)
# 			# 	# pass
# 	print("																		"+"_"*91)
# 	print("																		|											  |")
# 	print("																		|				   Data Extraction Complete. 				  |")
# 	print("																		|											  |")
# 	print("																		"+"_"*91)
# 	print()			
# 	print(f"																		|				   Finished in {round(time.perf_counter() - start, 2)} second(s)				  |")










			

			# df = pd.DataFrame([[ 	 org_num, company_name, phone_number,
			# 						 manager, owner, is_claimed, has_description, 
			# 						 has_freetext, has_deeplinks, has_seo, 
			# 						 has_premium_seo, has_hours, has_facebook, facebook, 	]], 
			# 		columns = [		'org_num', 'navn', 'tlf', 'daglig_leder', 
			# 						'styreleder', 'er_Eierbekreftet', 'har_Beskrivelse', 
			# 						'har_Fritekst', 'har_Dyplenker', 'har_SEO', 'har_Premium_SEO', 
			# 						'har_Åpningstider', 'har_Facebook', 'facebook'					])

				# df = pd.DataFrame(result, columns = ['org_num', 'navn', 'tlf', 'daglig_leder', 
				# 											'styreleder', 'er_Eierbekreftet', 'har_Beskrivelse', 
				# 											'har_Fritekst', 'har_Dyplenker', 'har_SEO', 'har_Premium_SEO', 
				# 											'har_Åpningstider', 'har_Facebook', 'facebook'					])	

			# for result in results:
			# 	time.sleep(0.1)
			# 	print(f"{result[0]}\n{result[1]}")
			# 	print("-"*100)
			# 	# pass




'''__________________________________ OLD STUFF _______________________________________'''

## [OLD CODE FOR SCRAPING]
	# for df, url in comp_data_list:
	# 	if os.path.exists('../_output_data/gulesider_data.csv'):
	# 	# if pd.read_csv('../_output_data/gulesider_data.csv'):
	# 		df_old = pd.read_csv('../_output_data/gulesider_data.csv')
	# 	else:
	# 		df_old = makeDataframe()
	# 	print(df_old)
	# 	df_old = df_old.reset_index(drop = True)
	# 	df = df.reset_index(drop = True)
	# 	df_final = pd.concat([df_old, df], axis = 0)
	# 	df_final = df_final.drop_duplicates()
	# 	df_final.to_csv('../_output_data/gulesider_data.csv', index = False)

	# 	print(f"succsessfully saved: {df['bedrift']}")

	# 	try: 
	# 		df_final = getInput()
	# 		df = df.reset_index(drop=True)
	# 		df_final = df_final.reset_index(drop=True)
	# 		try:
	# 			try:
	# 				df = df.set_index(['org num'])			
	# 				df_final = df_final.set_index(['org num'])
	# 				df_final = pd.concat([df_final, df], axis = 1)
	# 			except:
	# 				df = df.set_index(['bedrift'])			
	# 				df_final = df_final.set_index(['bedrift'])
	# 				df_final = pd.concat([df_final, df], axis = 1)
	# 		except:
	# 			print("Indexing error while trying to concat file, the file was:")
	# 			print(df)
	# 			print(df_final)
	# 			print(df_final.index)
	# 			print(df.index)
	# 		df_final = df_final.reset_index()
	# 		df_final = df_final.drop_duplicates()
	# 		df_final.to_csv('../_output_data/gulesider_data.csv', index = False)
	# 		# completed(company)
	# 	except AttributeError as e:
	# 		print()
	# 		print("ERROR WHILE SAVING FILE:")
	# 		print(df)
	# 		print(url)
	# 		print(e)
	# 		print()

## [ OLD GULESIDER MAIN ]
	# def gulesiderMain():
	# 	pd.set_option('display.max_colwidth', 50)		# Columns  (width)
	# 	pd.set_option('display.max_columns', 5)		# column display border
	# 	pd.set_option('display.width', 1000)		
	# 	# companies = getInputNames() # np array of all companies 
	# 	# companies = companies[0]
	# 	companies =['Felleskatalogen AS',
	# 	'Oslo Mynthandel AS',
	# 	'Focus Media AS',
	# 	'Filatelistisk Forlag AS',
	# 	'Ringlets Forlag Tor Egil Kvalnes',
	# 	'IT Media',
	# 	'Tut for Top20 DA',
	# 	'Mobilportalen DA',
	# 	'Reisenett AS',
	# 	'Tess SÃ¸rÃ¸st AS',
	# 	'Landvik Historielag',
	# 	'Tump ANS',
	# 	'Ambulanse-Norge',
	# 	'Reiseguidenno DA',
	# 	'Nettstart DA',]

	# 	# companies = ['AS Bryggestuen']
	# 	with tqdm(total = len(companies)) as pbar:
	# 		with concurrent.futures.ThreadPoolExecutor() as executor:
	# 			results = executor.map(extractionManager, companies)
	# 			df_new = makeDataframe()
	# 			for result in results:
	# 				df_new = pd.concat([df_new, result], axis = 0)
	# 				pbar.update(1)

	# 	if os.path.exists('../_output_data/gulesider_data.csv'):
	# 		df_old = pd.read_csv('../_output_data/gulesider_data.csv')
	# 	else:
	# 		df_old = makeDataframe()	
	# 	df_old = df_old.reset_index(drop = True)
	# 	df_new = df_new.reset_index(drop = True)
	# 	df_final = pd.concat([df_old, df_new], axis = 0)
	# 	df_final = df_final.drop_duplicates()
	# 	print("="*100)
	# 	print(df_final)
	# 	df_final.to_csv('../_output_data/gulesider_data.csv', index = False)
	# 	print(f"|				   Finished in {round(time.perf_counter() - start, 2)} second(s)				  |")

# # '''
# # # def nextPageUrl(soup):
# # # 	try:
# # # 		a = soup.find('a',{'class': 'arrow ssproff-right'})
# # # 		next_page_token = a['href']
# # # 		next_page_url = BASE_URL + next_page_token
# # # 	except TypeError:
# # # 		next_page_url = ""
# # # 	return next_page_url



# # # def getPage(url):
# # # 	soup = pullRequest(url)
# # # 	next_page_url = nextPageUrl(soup)
# # # 	return next_page_url
# # '''



# # def scarper(url):
# # 	next_page_url = getPage(url)
# # 	next_url = next_page_url
# # 	url_list = [url, next_url]
# # 	while True:
# # 	        next_page_url = getPage(next_url)
# # 	        next_url = next_page_url
# # 	        url_list.append(next_page_url)
# # 	        if next_url == '':
# # 	            break
# # 	return url_list


# # def genUrls(industries):
# # 	urls = []
# # 	for ind in industries:
# # 		url = f'https://www.proff.no/bransjes%C3%B8k?q={ind}'
# # 		urls.append(url)
# # 	return urls


# # def proffLinkDownloader():
# # 	df_main = pd.DataFrame()
# # 	urls = genUrls(industries)
# # 	print('	loading, please wait..')
# # 	print()
# # 	index=0
# # 	with concurrent.futures.ThreadPoolExecutor() as executor:
# # 		results = executor.map(scarper, urls)
# # 		for result in results:
# # 			index+=1
# # 			print(f'progress:{index}')
# # 			df = pd.DataFrame(result)
# # 			df_main = pd.concat([df_main, df], axis = 0)
# # 	print(df_main)
# # 	df_main.to_csv('links.csv', index = False)
# # 	print(f"|				   Finished in {round(time.perf_counter() - start, 2)} second(s)				  |")


