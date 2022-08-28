
''' TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP 
							
*						_____ WHERE I LEFT OF _____
-						[16.08.2022]
-						- koden sletter elementer fra input_table slik som den skal. 
-						- koden klarer å arbeide med noen elementer før den raiser en av to Errors

!						__ISSUE:___
!					1. 	sqlalchemy.exc.ProgrammingError: (psycopg2.errors.UndefinedTable) table "output_table" does not exist
						[SQL: DROP TABLE output_table]
						(Background on this error at: https://sqlalche.me/e/14/f405)

!					2. 	sqlalchemy.exc.ProgrammingError: (psycopg2.errors.UndefinedTable) relation "output_table" does not exist
						LINE 1: INSERT INTO output_table (org_num, navn, feilmelding) VALUES...
						(Background on this error at: https://sqlalche.me/e/14/f405)
						
!					3. 	sqlalchemy.exc.IntegrityError: (psycopg2.errors.UniqueViolation) duplicate key value violates unique constraint "pg_type_typname_nsp_index"
!						DETAIL:  Key (typname, typnamespace)=(output_table, 2200) already exists.
						[SQL: CREATE TABLE output_table (org_num BIGINT, navn TEXT, feilmelding BOOLEAN)]
						(Background on this error at: https://sqlalche.me/e/14/gkpj)

					TODO possible solution:
					problemet ligger i SQL at den ikke klarer å henge med når du bruker multiprocessing så mange ganger. 
						"Well, Actually, the only way I found to solve this is to create chunks big enough to have back a 
						writing process slower than the calculation itself. With bigger chunks this error doesn't rise."
					TODO: prøv å del opp arbeidet i større chunks
					TODO: eller prøver å samle opp arbeidet før du sender det til postgres

*						_____ EXTRACTION RECORD _______
*						Extracts (600) units -->  	 54.14 second(s)				  | => (1000) :  90.00 sec | [0.090 s/unit]

*						_____ ESTIMATIONS _______
*						Estimated length of input_list: 						1.069.577 rows / [1069577]
*						Estimated total extraction time: 						[26:44:21] / [01:02:44:21]


TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP'''

import time; start = time.perf_counter() #Since it also takes time to Import libs, I allways start the timer asap. 
import requests
from bs4 import BeautifulSoup
from fake_headers import Headers
from fake_useragent import UserAgent
import pandas as pd
import pprint
import os.path
from os import path
from tqdm import tqdm
import concurrent.futures
import os.path
import numpy as np
from multiprocessing import Pool, Process

''' ___ local imports __________'''
from config import payload, tablenames, settings
from postgres import databaseManager, getInputTable, checkIfMissing
from file_manager import *
from input_table import inputTable
from base_extractor import genSearchTerm, pullRequest

'''
NOTES:
	url example: 'https://www.1881.no/?query=mediavest+AS'

* IMPORTANT:
	- if you use 'org_num' as searchterm it will take you straight to the profile
	! unless they have more then one company in the same name, example:
	- https://www.1881.no/?query=+925476633
	TODO: look into this
'''
def linkBuilder(base_url, term):
	'''
		builds a search url based on only company name
	'''
	if isinstance(term, int):
		return f'{base_url}{term}' #* -> url
	else:
		return f'{base_url}{genSearchTerm(term)}&type=firma' #* -> url



# ! OLD GET REQUEST 
# def getRequest(url):
	# '''
	# 	1. makes a pull request from gulesider.no.
	# 	2. then checks the connection.
	# 	3. then returns a soup.
	# 	4. If a bad request occours; then it will save the error to "gulesider_error_table"
	# '''
	

	# cookies = { 'ASP.NET_SessionId':'5btxqhyab4kildcfudsowc31',
	# 			'__uzma':'c8749bb2-abdf-40b3-b4e2-3377bc4d33ae',
	# 			'__uzmb':'1660651793',
	# 			'__ssds':'2',
	# 			'__uzmaj2':'b50a61ac-fc20-49eb-aea0-9b9f7a292f82',
	# 			'__uzmbj2':'1660651794',
	# 			'_gid':'GA1.2.1371187027.1660652841',
	# 			'__ssuzjsr2':'a9be0cd8e',
	# 			'_MBL':'%7B%22u%22%3A%22G6fq8SYahK%22%2C%22t%22%3A1660653383%7D',
	# 			'__mbl':'%7B%22u%22%3A%5B%7B%22uid%22%3A%22YEIoShT3dFg6GprZ%22%2C%22ts%22%3A1660653384%7D%2C1660743384%5D%7D',
	# 			'_ga_60EFTS75DG':'GS1.1.1660652841.1.1.1660653384.0',
	# 			'_ga':'GA1.1.1591735888.1660652841',
	# 			'__uzmcj2':'995972548674',
	# 			'__uzmdj2':'1660653739',
	# 			'captchaResponse':'1',
	# 			'__uzmc':'856834036869',
	# 			'__uzmd':'1660653747',}
	# return requests.get(url, cookies=cookies, verify=True) #* -> req 

# * NEW3 GET REQUEST 
def getRequest(url):
	'''
		1. makes a pull request from gulesider.no.
		2. then checks the connection.
		3. then returns a soup.
		4. If a bad request occours; then it will save the error to "gulesider_error_table"
	'''
	cookies = { 'ASP.NET_SessionId':'5btxqhyab4kildcfudsowc31',
				'__uzma':'c8749bb2-abdf-40b3-b4e2-3377bc4d33ae',
				'__uzmb':'1660651793',
				'__ssds':'2',
				'__uzmaj2':'b50a61ac-fc20-49eb-aea0-9b9f7a292f82',
				'__uzmbj2':'1660651794',
				'_gid':'GA1.2.1371187027.1660652841',
				'__ssuzjsr2':'a9be0cd8e',
				'_MBL':'%7B%22u%22%3A%22G6fq8SYahK%22%2C%22t%22%3A1660653383%7D',
				'__mbl':'%7B%22u%22%3A%5B%7B%22uid%22%3A%22YEIoShT3dFg6GprZ%22%2C%22ts%22%3A1660653384%7D%2C1660743384%5D%7D',
				'_ga_60EFTS75DG':'GS1.1.1660652841.1.1.1660653384.0',
				'_ga':'GA1.1.1591735888.1660652841',
				'__uzmcj2':'995972548674',
				'__uzmdj2':'1660653739',
				'captchaResponse':'1',
				'__uzmc':'856834036869',
				'__uzmd':'1660653747',}
	s = requests.Session()
	s.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
	return s.get(url, cookies=cookies, verify=True)

def getSoup(req):
	''' gets soup '''
	return BeautifulSoup(req.content, "html.parser") #* -> soup

def findPromoDiv(soup):
	''' checks for promo banner '''
	# print()
	# print()
	# print(soup.prettify())
	# print()
	# print()
	return soup.find('div', {'class':'box dm-promo'})

def stringRetry(base_url, search_term):
	'''
		redos what extractionManager() did only with 
		search_term being company name instead of org_num
	'''
	# print("retries with search_term")
	search_term_url = linkBuilder(base_url, str(search_term))
	# print(search_term_url)
	req = getRequest(search_term_url)
	soup = getSoup(req)

	listing = checkIfList(soup)
	'''
	if statement:
		if soup == listing then get new soup from href link (redirect to 1881 profile)
		else: keep old soup  (no else statement in code)
	'''
	
	if listing:
		# print("after string retry: is Listing, geting new soup")#TEMP - while testing
		soup = newSoup(listing) #new_soup
	# else: 
	# 	print("after string retry: is NOT Listing, keeping old soup")#TEMP - while testing
		# print(listing)

	if soup.find('div',{'class':'box alert-content'}):
		return None
		# print("after string retry: found NO search results, return False")
		# return None
		# return None
	elif soup.find('div',{'class':'box text-section'}):
		return None
			# print("after string retry: found NO search results, return False")
			# return None
	else:
		# print("after string retry: found search results, return soup")
		# print(soup)
		return soup
		# return findPromoDiv(soup)
		# return findPromoDiv(soup), False
	# 	'''
	# 		! ERROR NOTE:
	# 		- sometimes search results will return a list of companies that are not related to search term, verifying will take a lot of time to do.
	# 			could find org num in side the profile of the first search result then compare.  
	# 	'''

	# if soup.find('div',{'class':'box alert-content'}) or soup.find('div',{'class':'box text-section'}):
	# 	# print("after string retry: found NO search results, return False")
	# 	return False
	# 	# return None
	# else:
	# 	# print("after string retry: found search results, return findPromoDiv(soup)")
	# 	return findPromoDiv(soup)
		

def newSoup(listing):
	''' 
		if soup is a listing; this will find a link 
		to the profile of the first list element 
	'''
	# a = listing[0].find('a',{'href' : True})
	h2 = listing.find('h2',{'class' : "listing-name"})
	a = h2.find('a',{'href' : True})
	new_link = a['href']
	# print(f"newSoup link: {new_link}")
	return getSoup(getRequest('https://www.1881.no/'+new_link))

def checkIfList(soup):
	''' checks if page is a profile or a listing '''
	# return soup.findAll('div',{'class':'box listing listing--business '})
	# return soup.find('div',{'class':'box listing listing--business '})
	return soup.find('div',{'class':'box listing listing--business'})

def extractionManager(input_array):
	'''
		finds profile for company, 
		then checks if profile contains a 
		promo banner for payed entries
	'''
	# element_exist = checkIfMissing(org_num)
	org_num = input_array[0]
	search_term = input_array[1]
	# print(f"___ extracting: {search_term} ___") #TEMP - while testing

	'''
	if statement:
		if org_num is NOT missing from input_table: then continue scraping
		else: pass 
	'''
	if not checkIfMissing(org_num):
		
		source = '1881.py'
		base_url = 'https://www.1881.no/?query='
		url = linkBuilder(base_url, str(org_num))
		# print(f" url: {url}")  #TEMP - while testing
		req = getRequest(url)
		soup = getSoup(req)
		listing = checkIfList(soup)
		# print("NOT missing from input_table")#TEMP - while testing
		'''
		if statement:
			if soup == listing then get new soup from href link (redirect to 1881 profile)
			else: keep old soup  (no else statement in code)
		'''
		if listing:
			# print("is Listing, geting new soup")#TEMP - while testing
			soup = newSoup(listing)
		# else: 
		# 	print("is NOT Listing, keeping old soup")#TEMP - while testing
		'''
		if statement:
			if soup contains a "no search results"-div: Retries search with search_term instead of org_num
			else: Looks for Promo-div
		'''		
		# error = False
		if soup.find('div',{'class':'box text-section'}):
			# print("found NO search results")#TEMP - while testing
			''' found no search results '''
			soup = stringRetry(base_url, search_term)
		if soup:
			# print("soup exists:")
			# print(soup)
			verification = verifyName(soup, search_term, org_num)
			# print(verification)
			if verification:	
				# verifyOrgNum(soup, search_term, org_num)
				div = findPromoDiv(soup)

				# else:
					# print("found search results")#TEMP - while testing
					# ''' found search results '''
					# div = findPromoDiv(soup)

				
					
				'''
				if statement:
					if Promo-div == None (doesn't exist): Has payed entry --> delete from input_table + return org_num, search_term
					else: pass

				try statement:
					try: delete from input_table
					except: one of the other extractors has deleted it. 
				'''	
				# else:
				# print("\n")
				# print(div)
				# print("\n")
				if div is None:	
					# print("has NO Promo div")#TEMP - while testing
					# print("CONCLUTION: WILL BE RETURNED")#TEMP - while testing
					try:
						''' has payed entry '''
						###deleteData(org_num, tablename = "input_table") #* All inputs that are found can be deleted from input_table 
						return org_num, search_term #, error
					except:
						# print("already deleted")#TEMP - while testing
						''' already deleted '''
	# 					pass
	# 		else:
	# 			print("has Promo div") #TEMP - while testing
	# 			pass	
	# else:
	# 	print("missing from input_table") #TEMP - while testing
	# 	pass

'''
TEMP TEST INPUT_ARRAY:
input_array = [ [928726452, 'TITLES-ON LIMITED']
				[916546351, 'TITTTEI VOLHA KOUHAR']
				[924648287, 'TITANIUM RENEWABLE SERVICES LTD']
				[917338213, 'TIUR FRISØR AS']
				[928673510, 'TIYOUBA OY']
				[916018002, 'TJ SUPPORT LTD']
				[928408639, 'TJC SA']
				[915851134, 'TJ74 LTD'] ]
'''

def verifyName(soup, search_term, org_num):
	if soup.find('h1',{'class' : 'details-name'}) == search_term:
		return True
	else:
		return verifyOrgNum(soup, search_term, org_num)

def verifyOrgNum(soup, search_term, org_num):
	return getSearchOrgNum(soup, search_term, org_num) == org_num

def getSearchOrgNum(soup, search_term, org_num):
	href = soup.find('a',text = 'Org. nummer, firmainformasjon, m.m.')['href']
	soup = getSoup(getRequest(href))
	div = (soup.findAll('table',{'class' : 'tbl'}))[1]
	td = div.find('td').text
	return int(td.replace(' ', ''))


def makeChunks(input_array, chunksize):
	return [input_array[i:i+chunksize] for i in range(0, len(input_array), chunksize)]  

def opplysningenExtractor(**kwargs): #1881Extractor did not work
	'''
		sets up all nessasary functions, 
		then gets list of company names, 
		then iterates through the list via multithreading: claimedStatus().
	'''
	print("_"*62)
	print("|                  Starting: 1881 Extractor                  |")
	print("_"*62)
	print()

	''' fetching data from config '''
	file_name = getFileName() # gets filename of this file.
	# settings = parseSettings(file_name) # same as above, only for settings.
	# chunksize = settings['chunk_size']
	chunksize = 500
	# input_array = getInputTable(tablenames['input']).to_numpy() #fetches the input data
	input_array = (getInputTable('brreg_table'))[['org_num', 'navn']].to_numpy() #fetches the input data  #TEMP --- while testing
	input_array = input_array[:1000]  #TEMP --- while testing
	# input_array = [ [928408639, 'TJC SA'],
	# [979389434, 'Intermezzo Frisør AS'],
					
	# 				[928726452, 'TITLES-ON LIMITED'],
	# 				[916546351, 'TITTTEI VOLHA KOUHAR'],
	# 				[924648287, 'TITANIUM RENEWABLE SERVICES LTD'],
	# 				[917338213, 'TIUR FRISØR AS'],
	# 				[928673510, 'TIYOUBA OY'],
	# 				[916018002, 'TJ SUPPORT LTD'],
	# 				[928408639, 'TJC SA'],
	# 				[915851134, 'TJ74 LTD'], ]
	# ''' making adjustments if testmode '''
	# if kwargs.get('testmode', None):
	# 	# input_array = input_array[:1000]
	# 	input_array = input_array[800000:801000]
	# 	# tablename = parseTablenames(file_name, testmode = False) # gets tablename based on filename, [filename + "_table" = tablename] e.g. gulesider.py -> gulesider_table.
	# 	tablename = 'I88I_test_output_table'
	# else:
	# 	parseTablenames(file_name, testmode = False)
	nested_input_array = makeChunks(input_array, chunksize) # divides input_array into chunks 
	
	print(f"chunksize: {chunksize}")
	print(f"input length: {len(input_array)}")
	print(f"number of chunks: {len(nested_input_array)}")
	print("\n\n\n")
	# for i in input_array:
	# 	results = extractionManager(i)
	# 	if results is not None:
	# 		df =  pd.DataFrame([results], columns = ['org_num', 'navn'])
	# 		print(df)
	# 		print("_"*100)
	# 	else:
	# 		print(pd.DataFrame())
	# 		print("_"*100)			



	with tqdm(total = len(nested_input_array)) as pbar: 
		for input_array in nested_input_array:
			with Pool() as pool:
				# results = list(pool.imap_unordered(extractionManager, input_array)) #TEMP --- while testing
				results = list(tqdm(pool.imap_unordered(extractionManager, input_array), total = len(input_array)))
				results = [x for x in results if x is not None]
				df =  pd.DataFrame(results, columns = ['org_num', 'navn'])
				print(df)
				#### databaseManager(df, tablename = "I88I_test_output_table")
				pbar.update(1)
	
	print("_"*62)
	print("                  Data Extraction Complete.                 ")
	print(f"                  Finished in {round(time.perf_counter() - start, 2)} second(s)                 ")
	print("_"*62)
	print()

if __name__ == '__main__':
	opplysningenExtractor(testmode = True)
	# opplysningenExtractor(testmode = False)
