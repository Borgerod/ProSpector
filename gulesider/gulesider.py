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

# # ___ local imports __________
# import sys
# import os
# SCRIPT_DIR  = os.path.dirname(os.path.abspath(__file__))
# sys.path.append(os.path.dirname(SCRIPT_DIR))
# from error_save import errorSave #NB: MIGHT BE WRONG




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

'''
# OPTIONAL:
def linkBuilder(company, type_):
	##builds a search url based on name and type of search ('company or person')
	base_url = 'https://www.gulesider.no'
	url = f'{base_url}/{search_term}/{type_}'
	##Optional: checks if type is 0 = company or 1 = person 
		if type_ == 0:
			unit_type = 'bedrift'
			url = f'{base_url}/{search_term}/bedrifter'
		else:
			unit_type = 
			url = f'{base_url}/{search_term}/personer'
	return url
'''



def pullRequest(url, source):
	'''
	1. makes a pull request from gulesider.no.
	2. then checks the connection.
	3. then returns a soup.
	'''
	# print(url)
	try:
		r = requests.get(url, timeout=10)
		soup = BeautifulSoup(r.content, "html.parser")
		r.raise_for_status()

	except (requests.exceptions.RequestException, ValueError) as e:
		''' 
		if exception occurred:
			- prints error & related url
			- sends the faulty url (++) to errorSave() from error_save.py for later use
			- returns an empty soup
		'''	
		print("="*91)
		print("|											  |")
		print("|				WARNING: ERROR CAUGHT! 				  |")
		print("|											  |")
		print("="*91)
		print(f'					{print(e)}')
		# errorSave(url, e, source) #Currently not in nuse (not yet finished)
		# soup = ""
		pass 
	return soup



def getCompanyInfoLinks(cont):
	a = cont.find('a',{'href' : True})
	href = a['href']
	base_url = 'https://www.gulesider.no'
	new_url = base_url+href
	return new_url


def getNewLinks(soup):
	'''
	first: get full list of search results ['article', {'class':'CompanyResultListItem'}]
	'''

	'''
	ANALYSE:
		bedre link, gir oss et pagenumber vi kan parse igjennom. 
		'84423496' gjør meg litt bekymret da, vet ikke hva det er. Den endrer seg ikke når man endrer page number,
		gir meg inntrykk av at det er org_num.
		bekreftet at dette var feil: 965 614 923
		bekreftet at dette var div name='84423496' og finnes i html filen to plasser;
		i  <div name='84423496'> og i <a id='company_link_84423496'> --> som også gir deg linken i "href"	
		Alt dette finner du inni ResultList items, som er rett i blinken	
	'''

	# GET RESULTLSIT 
	result_list = soup.findAll('article', {'class':'CompanyResultListItem'})
	result_list = [i for i in result_list]
	# ANTAGELSE: virker som [0] og [last] elementet i listen er trash
	print(f'num of list items: {len(result_list)}')
	


	# GET LIST COMPANY INFO URLS
	''' example url: https://www.gulesider.no/felleskatalogen+as+oslo/84423496/bedrift?page=1&query=felleskatalogen%20as '''	
	new_link_list = [getCompanyInfoLinks(cont) for cont in result_list ]
	return new_link_list
import pprint 


def getData(soup, url):

	''' GTE_NAME '''
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
		# print(f'could not extract phone_number from {url}')
		phone_number = None

	''' GET_STAFF '''
	# if soup.find('div', { 'class': "roles" }):
	if [i for i in soup.find('div', { 'class': "roles" })]:
		staff = [i for i in soup.find('div', { 'class': "roles" })]
	else:
		staff = []

	'''	MANAGER '''		
	if staff[0].find('div', { 'class': "rolename e-icon-user" }).text:
		manager = staff[0].find('div', { 'class': "rolename e-icon-user" }).text
		# print(f'Daglig leder : {manager}')
	else:
		manager = None
	

	'''	OWNER '''
	if len(staff)>1:
		if staff[1].find('div', { 'class': "rolename e-icon-user" }).text:
			owner = staff[1].find('div', { 'class': "rolename e-icon-user" }).text
			# print(f'Styreleder : {owner}')
		else:
			owner = None
	else:
		owner = None


	# ''' NACE_INDUSTRY'''
	# try:
	# 	if soup.find("strong", text="NACE-bransje:").next_sibling.text:
	# 		nace_industry = soup.find("strong", text="NACE-bransje:").next_sibling.text
	# 		# print(f'NACE-bransje : {nace_industry}')
	# 	else: 
	# 		nace_industry = None
	# except AttributeError as e:
	# 	print()  
	# 	print(e)
	# 	print(url)	
	# 	print()
	# 	nace_industry = 0	

	# # ''' MARKET_CAP '''
	# try: 
	# 	if soup.find("strong", text="Aksjekapital:").next_sibling.text:
	# 		market_cap_str = soup.find("strong", text = "Aksjekapital:").next_sibling.text
	# 		try:
	# 			market_cap = int(market_cap_str.replace(' ',''))
	# 			# print(f'Aksjekapital : {market_cap}')
	# 		except ValueError as e:
	# 			print() 
	# 			print(e)
	# 			print(url)
	# 			print()
	# 			market_cap = market_cap_str
	# 	else:
	# 		market_cap = None
	# except AttributeError as e: 
	# 	print() 
	# 	print(e)
	# 	print(url)	
	# 	print()
	# 	market_cap = 0

	# ''' ORG_NUM '''
	if soup.find("strong", text = "Org.nr:").next_sibling.text:
		org_num = soup.find("strong", text = "Org.nr:").next_sibling.text
		org_num = int(org_num.replace(' ',''))
		# print(f'Org.nr : {org_num}')
	else:
		org_num=None


	# # ''' revenue '''
	# try: 
	# 	if soup.find("div", text = "Driftsinntekter"):
	# 		revenue = soup.find("div", text = "Driftsinntekter").next_sibling.text
	# 		revenue_str = (revenue.split('tkr'))[0].replace(' ','')
	# 		try:
	# 			revenue = int(float(revenue_str)* 1000)
	# 		except ValueError:
	# 			revenue = revenue_str
	# 		# print(f'Driftsinntekter : {revenue}')
	# 	else: 
	# 		revenue=None
	# except AttributeError as e:
	# 	print()  
	# 	print(e)
	# 	print(url)	
	# 	print()
	# 	revenue = 0

	# # ''' profitability'''
	# try:
	# 	if soup.find("div", text = "Lønnsomhet").next_sibling.text:
	# 		profitability_str = soup.find("div", text = "Lønnsomhet").next_sibling.text
	# 		try:
	# 			profitability = float((profitability_str.split('%'))[0].replace(' ','')) / 100
	# 		except ValueError:
	# 			profitability = profitability_str
	# 		# print(f'Lønnsomhet : {profitability}')
	# 	else:
	# 		profitability = None
	# except AttributeError as e:
	# 	print() 
	# 	print(e)
	# 	print(url)	
	# 	print()
	# 	profitability = 0

	# # ''' len_employees'''
	# try:
	# 	if soup.find("div", text = "Antall ansatte").next_sibling.text:
	# 		try:
	# 			len_employees = int(soup.find("div", text = "Antall ansatte").next_sibling.text)
	# 			# print(f'Antall ansatte : {len_employees}')
	# 		except ValueError:
	# 			len_employees = soup.find("div", text = "Antall ansatte").next_sibling.text
	# 	else:
	# 		len_employees = None
	# except AttributeError as e:
	# 	print()  
	# 	print(e)
	# 	print(url)	
	# 	print()
	# 	len_employees = 0
		
	''' IS_CLAIMED?
			false:	company is NOT claimed and are possible clients
			true: 	company is decleared but could still be potential clients '''
	is_claimed = soup.find('div', { 'class': "Yext card full" })
	if not is_claimed.find('h2'):
		# print('is_claimed: true')
		is_claimed = True
	else: 
		# print('is_claimed: false')
		is_claimed = False


	''' HAS_DESCRIPTION?
			false:	company has NO description and are possible clients
			true: 	company has description but could still be potential clients '''
	if soup.find('div', { 'class': 'companyDescription card' }):
		# print('has_description: true')
		has_description = True
	else: 
		# print('has_description: false')
		has_description = False
	

	''' HAS_FREETEXT?
			false:	company has NO freetext and are possible clients
			true: 	company has freetext but could still be potential clients '''
	if soup.find('div', { 'class': 'freeTextContainer card' }):
		# print('has_freetext: true')
		has_freetext = True
	else: 
		# print('has_freetext: false')
		has_freetext = False	


	''' HAS_DEEPLINKS?
			false:	company has NO deeplinks and are possible clients
			true: 	company has deeplinks but could still be potential clients '''
	if soup.find('div', { 'class': 'deeplinks card full' }):
		# print('has_deeplinks: true')
		has_deeplinks = True
	else: 
		# print('has_deeplinks: false')
		has_deeplinks = False	


	''' HAS_SEO?
			false:	company has NO seo and are possible clients
			true: 	company has seo but could still be potential clients '''
	if soup.find('div', { 'class': 'SearchWords company-tags--section' }):
		# print('has_seo: true')
		has_seo = True
	else: 
		# print('has_seo: false')
		has_seo = False	


	''' HAS_PREMIUM_SEO?
			false:	company has NO premium_seo and are possible clients
			true: 	company has premium_seo but could still be potential clients '''
	if soup.find('div', { 'class': 'PremiumSearchWords' }):
		# print('has_premium_seo: true')
		has_premium_seo = True
	else: 
		# print('has_premium_seo: false')
		has_premium_seo = False	

	''' HAS_FACEBOOK?
			false:	company has NO facebook and are possible clients
			true: 	company has facebook but could still be potential clients '''
	if soup.find('div', { 'class': 'facebook' }):
		# print('has_facebook: true')
		facebook = soup.find("a", {'class':"e-icon e-icon-facebook"})['href']
		has_facebook = True
		# print(f'facebook: {facebook}')
	else: 
		# print('has_facebook: false')
		has_facebook = False
		facebook = None

	''' HAS_HOURS?
			false:	company has NO opening hours and are possible clients
			true: 	company has opening hours but could still be potential clients''' 
	if soup.find('div', { 'class': 'item openingHoursWrapper e-icon e-icon-clock collapsed' }):	
		# print('has_hours: true')
		has_hours = True
	else: 
		# print('has_hours: false')
		has_hours = False

	''' HAS_EMAIL?
			false:	company has NO Email and are possible clients
			true: 	company has Email but could still be potential clients''' 
	if soup.find('div', { 'class': 'item email' }):	
		# print('has_email: true')
		has_email = True
	else: 
		# print('has_email: false')
		has_hours = False
	
	df = pd.DataFrame([[ 	 company_name,
							 phone_number,
							 manager, 
							 owner, 
							 # nace_industry,
							 # market_cap,
							 # revenue,
							 # profitability,
							 # len_employees,
							 is_claimed, 
							 has_description, 
							 has_freetext, 
							 has_deeplinks, 
							 has_seo, 
							 has_premium_seo,
							 has_hours,
							 has_facebook,
							 facebook,
							 org_num,  		]], 
				columns = [	'bedrift',
							'tlf',
							'daglig leder',
							'styreleder',
							# 'NACE-bransje',
							# 'Aksjekapital',
							# 'Driftsinntekter',
							# 'Lønnsomhet',
							# 'Antall ansatte',
							'er Eierbekreftet',
							'har Beskrivelse',
							'har Fritekst',
							'har Dyplenker',
							'har SEO',
							'har Premium SEO',
							'har Åpningstider',
							'har Facebook',
							'facebook',
							'org num', 		])
	# print(df)
	return df, url



def makeDataframe():
		return pd.DataFrame( columns = [	'bedrift',
											'tlf',
											'daglig leder',
											'styreleder',
											# 'NACE-bransje',
											# 'Aksjekapital',
											# 'Driftsinntekter',
											# 'Lønnsomhet',
											# 'Antall ansatte',
											'er Eierbekreftet',
											'har Beskrivelse',
											'har Fritekst',
											'har Dyplenker',
											'har SEO',
											'har Premium SEO',
											'har Åpningstider',
											'har Facebook',
											'facebook',
											'org num', 		])
	 



def visabilityTest(data):
	'''
	BONUS TEST SYNLIGHET
		example link: https://nettsjekk.gulesider.no/?utm_source=gulesider&utm_medium=corefront&utm_campaign=netcheck&companyName=Felleskatalogen%20AS&phoneNumber=23%2016%2015%2050&street=Essendrops%20gate%203&postCode=0368&postArea=Oslo
		we should be able to get these from the proff_data.csv
			note: the parameters might need to be formated correctly
				--> replace(' ', '%20')

			Will use insomnia or charlie for further testing
	'''
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


# _____ MAIN __________________________
def scraper(company):
	source = 'gulsesider.py'
	url = linkBuilder(company)  		#Note: built for 1 unit not multiple units
	soup = pullRequest(url, source)		#Note: built for 1 unit not multiple units
	new_link_list = getNewLinks(soup) 	#gets a list of links for additional info
	soup_list = [pullRequest(url, source) for url in new_link_list ]
	# comp_data_list = [getData(soup) for soup in soup_list]
	comp_data_list = [getData(soup, url) for soup, url in zip(soup_list, new_link_list)]
	df_new = makeDataframe()
	for df, url in comp_data_list:
		df_new = pd.concat([df_new, df], axis = 0)
	return df_new


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

		# print(f"succsessfully saved: {df['bedrift']}")

		# # print(df)
		# try: 
		# 	df_final = getInput()
		# 	df = df.reset_index(drop=True)
		# 	df_final = df_final.reset_index(drop=True)
		# 	# print(df)
		# 	try:
		# 		try:
		# 			df = df.set_index(['org num'])			
		# 			df_final = df_final.set_index(['org num'])
		# 			df_final = pd.concat([df_final, df], axis = 1)
		# 		except:
		# 			df = df.set_index(['bedrift'])			
		# 			df_final = df_final.set_index(['bedrift'])
		# 			df_final = pd.concat([df_final, df], axis = 1)
		# 	except:
		# 		print("Indexing error while trying to concat file, the file was:")
		# 		print(df)
		# 		print(df_final)
		# 		print(df_final.index)
		# 		print(df.index)
		# 	df_final = df_final.reset_index()
		# 	df_final = df_final.drop_duplicates()
		# 	df_final.to_csv('../_output_data/gulesider_data.csv', index = False)
		# 	# completed(company)
		# except AttributeError as e:
		# 	print()
		# 	print("ERROR WHILE SAVING FILE:")
		# 	print(df)
		# 	print(url)
		# 	print(e)
		# 	print()



def gulesiderMain():
	pd.set_option('display.max_colwidth', 50)		# Columns  (width)
	pd.set_option('display.max_columns', 5)		# column display border
	pd.set_option('display.width', 1000)		
	# companies = getInputNames() # np array of all companies 
	# companies = companies[0]
	companies =['Felleskatalogen AS',
	'Oslo Mynthandel AS',
	'Focus Media AS',
	'Filatelistisk Forlag AS',
	'Ringlets Forlag Tor Egil Kvalnes',
	'IT Media',
	'Tut for Top20 DA',
	'Mobilportalen DA',
	'Reisenett AS',
	'Tess SÃ¸rÃ¸st AS',
	'Landvik Historielag',
	'Tump ANS',
	'Ambulanse-Norge',
	'Reiseguidenno DA',
	'Nettstart DA',]

	# companies = ['AS Bryggestuen']
	with tqdm(total = len(companies)) as pbar:
		with concurrent.futures.ThreadPoolExecutor() as executor:
			results = executor.map(scraper, companies)
			df_new = makeDataframe()
			for result in results:
				df_new = pd.concat([df_new, result], axis = 0)
				pbar.update(1)

	if os.path.exists('../_output_data/gulesider_data.csv'):
		df_old = pd.read_csv('../_output_data/gulesider_data.csv')
	else:
		df_old = makeDataframe()	
	df_old = df_old.reset_index(drop = True)
	df_new = df_new.reset_index(drop = True)
	df_final = pd.concat([df_old, df_new], axis = 0)
	df_final = df_final.drop_duplicates()
	print("="*100)
	print(df_final)
	df_final.to_csv('../_output_data/gulesider_data.csv', index = False)
	print(f"|				   Finished in {round(time.perf_counter() - start, 2)} second(s)				  |")

if __name__ == '__main__':
	gulesiderMain()
	





















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


