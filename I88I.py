
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
*						Skraper 600 enheter -->  	 54.14 second(s)
	
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
	return requests.get(url, cookies=cookies, verify=True) #* -> req 

def getSoup(req):
	''' gets soup '''
	return BeautifulSoup(req.content, "html.parser") #* -> soup

def findPromoDiv(soup):
	''' checks for promo banner '''
	return soup.find('div', {'class':'box dm-promo'})

def stringRetry(base_url, search_term):
	'''
		redos what extractionManager() did only with 
		search_term being company name instead of org_num
	'''
	url = linkBuilder(base_url, str(search_term))
	req = getRequest(url)
	soup = getSoup(req)
	if soup.find('div',{'class':'box text-section'}):
		return False, True
	else:
		return findPromoDiv(soup), False

def newSoup(listing):
	''' 
		if soup is a listing; this will find a link 
		to the profile of the first list element 
	'''
	a = listing[0].find('a',{'href' : True})
	new_link = a['href']
	return getSoup(getRequest(new_link))

def checkIfList(soup):
	''' checks if page is a profile or a listing '''
	return soup.findAll('div',{'class':'box listing listing--business '})

def extractionManager(input_array):
	'''
		finds profile for company, 
		then checks if profile contains a 
		promo banner for payed entries
	'''
	# element_exist = checkIfMissing(org_num)
	org_num = input_array[0]
	search_term = input_array[1]
	if not checkIfMissing(org_num):
		# print("Not Missing, continue") #TEMP - while testing
		source = '1881.py'
		base_url = 'https://www.1881.no/?query='
		url = linkBuilder(base_url, str(org_num))       
		req = getRequest(url)
		soup = getSoup(req)
		listing = checkIfList(soup)
		if listing:
			soup = newSoup(listing)
		error = False
		if soup.find('div',{'class':'box text-section'}):
			''' found no search results '''
			div, error = stringRetry(base_url, search_term)
		else:
			''' found search results '''
			div = findPromoDiv(soup)
		# else:
		if div is None:	
			try:
				''' has payed entry '''
				deleteData(org_num, tablename = "input_table") #* All inputs that are found can be deleted from input_table 
				return org_num, search_term #, error
			except:
				''' already deleted '''
				pass
		else:
			pass	
			'''
				! Try statement was removed because; 
				- even if the company does not have a payed entry here, doesnt mean that they have a payed_entry for the other ones. 
				try:
					deleteData(org_num, tablename = "input_table")
				except:
					pass			
			'''
	else:
		# print("Missing, pass") #TEMP - while testing
		pass

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
	# print("|                 	   	    Starting: 1881 EXTRACTOR 	                    	  |")
	print("_"*62)
	print()
	''' fetching data from config '''
	file_name = getFileName() # gets filename of this file.
	settings = parseSettings(file_name) # same as above, only for settings.
	chunksize = settings['chunk_size']
	input_array = getInputTable(tablenames['input']).to_numpy() #fetches the input data
	''' making adjustments if testmode '''
	if kwargs.get('testmode', None):
		input_array = input_array[:1000]
		tablename = parseTablenames(file_name, testmode = True) # gets tablename based on filename, [filename + "_table" = tablename] e.g. gulesider.py -> gulesider_table.
		#! [ALT] tablename = 'gulses'ider_test_table'
	else:
		parseTablenames(file_name, testmode = False)
		#! [ALT] tablename = 'gulesider_table'
	print(f"chunksize: {chunksize}")
	print(f"input length: {len(input_array)}")
	nested_input_array = makeChunks(input_array, chunksize) # divides input_array into chunks 
	print(f"number of chunks: {len(nested_input_array)}")
	with tqdm(total = len(nested_input_array)) as pbar: #TEMP --- TEST
		for input_array in nested_input_array:
			with Pool() as pool:
				results = list(tqdm(pool.imap_unordered(extractionManager, input_array), total = len(input_array)))
				# results = list(tqdm(pool.imap_unordered(extractionManager, input_array, chunksize = chunksize), total = len(input_array)))
				results = [x for x in results if x is not None]    # 00:51 seconds
				df =  pd.DataFrame(results, columns = ['org_num', 'navn'])
				databaseManager(df, tablename = "output_table")
				# print(f" Chunk finished in {round(time.perf_counter() - start, 2)} second(s)")
		pbar.update(1) #TEMP --- TEST
	'''
		! ____ CURRENT ISSUE____
		- extractor wait untill ALL of the data has been gathered before it passes it to postgres
		TODO: løsningen er å lage sine egne chunks
	'''
	print("_"*62)
	print("                  Data Extraction Complete.                 ")
	print(f"                  Finished in {round(time.perf_counter() - start, 2)} second(s)                 ")
	print("_"*62)
	print()

	# print("                                                                     "+"_"*91)
	# print("                                                                     |                  Data Extraction Complete.                  |")
	# print("                                                                     "+"_"*91)
	# print()
	# print(f"                                                                    |                  Finished in {round(time.perf_counter() - start, 2)} second(s)                  |")

if __name__ == '__main__':
	# opplysningenExtractor(testmode = True)
	opplysningenExtractor(testmode = False)





















'''_________________________ OLD CODE _______________________________________________
'''

#* ___________ ORIGINAL (UTEN CHUNKS)___________
	# def opplysningenExtractor(**kwargs): #1881Extractor did not work
		# '''
		# 	sets up all nessasary functions, 
		# 	then gets list of company names, 
		# 	then iterates through the list via multithreading: claimedStatus().
		# '''
		# print("_"*91)
		# print("|                Starting: 1881 EXTRACTOR                  |")
		# print("_"*91)
		# print()
		# ''' fetching data from config '''
		# file_name = getFileName() # gets filename of this file.
		# settings = parseSettings(file_name) # same as above, only for settings.
		# chunksize = settings['chunk_size']
		# input_array = getInputTable(tablenames['input']).to_numpy() #fetches the input data
		# ''' making adjustments if testmode '''
		# if kwargs.get('testmode', None):
		# 	input_array = input_array[:600]
		# 	tablename = parseTablenames(file_name, testmode = True) # gets tablename based on filename, [filename + "_table" = tablename] e.g. gulesider.py -> gulesider_table.
		# 	#! [ALT] tablename = 'gulses'ider_test_table'
		# else:
		# 	parseTablenames(file_name, testmode = False)
		# 	#! [ALT] tablename = 'gulesider_table'
		# print(f"chunksize: {chunksize}")
		# print(f"input length: {len(input_array)}")	
		# with Pool() as pool:
		# 	results = list(tqdm(pool.imap_unordered(extractionManager, input_array, chunksize = chunksize), total = len(input_array)))
		# 	results = [x for x in results if x is not None]    # 00:51 seconds
		# 	df =  pd.DataFrame(results, columns = ['org_num', 'navn', 'feilmelding'])
		# 	print(df)
		# 	databaseManager(df, tablename = "output_table")
		
		# '''
		# 	! ____ CURRENT ISSUE____
		# 	- extractor wait untill ALL of the data has been gathered before it passes it to postgres
		# 	TODO: løsningen er å lage sine egne chunks
		# '''

		# print("                                                                     "+"_"*91)
		# print("                                                                     |                  Data Extraction Complete.                  |")
		# print("                                                                     "+"_"*91)
		# print()
		# print(f"                                                                        |                  Finished in {round(time.perf_counter() - start, 2)} second(s)                  |")

	# if __name__ == '__main__':
	# # opplysningenExtractor(testmode = True)
	# opplysningenExtractor(testmode = False)


# def extractionManager(input_array):
	# '''
	# 	finds profile for company, 
	# 	then checks if profile contains a 
	# 	promo banner for payed entries
	# '''
	# org_num = input_array[0]
	# search_term = input_array[1]
	# source = '1881.py'
	# base_url = 'https://www.1881.no/?query='
	# url = linkBuilder(base_url, str(org_num))       
	# req = getRequest(url)
	# soup = getSoup(req)
	# listing = checkIfList(soup)
	# if listing:
	# 	soup = newSoup(listing)
	# error = False
	# if soup.find('div',{'class':'box text-section'}):
	# 	''' found no search results '''
	# 	div, error = stringRetry(base_url, search_term)
	# else:
	# 	''' found search results '''
	# 	div = findPromoDiv(soup)

	# # else:
	# if div is None:	
	# 	''' has payed entry '''
	# 	df =  pd.DataFrame([[org_num, search_term, error]], 
	# 						columns = ['org_num','navn','feilmelding'])
	# 	databaseManager(df, tablename = "output_table")
	# else:	
	# # if div:
	# 	''' has not payed entry '''
	# 	try:
	# 		deleteData(org_num, tablename = "input_table")
	# 	except:
	# 		pass

# def opplysningenExtractor(**kwargs): #1881Extractor did not work
	# '''
	# 	sets up all nessasary functions, 
	# 	then gets list of company names, 
	# 	then iterates through the list via multithreading: claimedStatus().
	# '''
	# print("_"*91)
	# print("|                Starting: 1881 EXTRACTOR                  |")
	# print("_"*91)
	# print()
	# ''' fetching data from config '''
	# file_name = getFileName() # gets filename of this file.
	# settings = parseSettings(file_name) # same as above, only for settings.
	# chunksize = settings['chunk_size']
	# print(f"chunksize: {chunksize}")
	# input_array = getInputTable(tablenames['input']).to_numpy() #fetches the input data
	# ''' making adjustments if testmode '''
	# if kwargs.get('testmode', None):
	# 	input_array = input_array[:30]
	# 	tablename = parseTablenames(file_name, testmode = True) # gets tablename based on filename, [filename + "_table" = tablename] e.g. gulesider.py -> gulesider_table.
	# 	#! [ALT] tablename = 'gulses'ider_test_table'
	# else:
	# 	parseTablenames(file_name, testmode = False)
	# 	#! [ALT] tablename = 'gulesider_table'
	# with Pool() as pool:
	# 	list(tqdm(pool.imap_unordered(extractionManager, input_array, chunksize = chunksize), total = len(input_array)))
	# # with tqdm(total = len(input_array)) as pbar:
	# # 		with Pool() as pool:
	# # 			results = pool.imap_unordered(extractionManager, input_array, chunksize = chunksize)
	# # 			for df in results:
	# ## 				if df is not None:
	# # 				pbar.update(1)  
					
	# print("                                                                     "+"_"*91)
	# print("                                                                     |                  Data Extraction Complete.                  |")
	# print("                                                                     "+"_"*91)
	# print()
	# print(f"                                                                        |                  Finished in {round(time.perf_counter() - start, 2)} second(s)                  |")

# if __name__ == '__main__':
	# opplysningenExtractor(testmode = False)


