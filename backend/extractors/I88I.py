

import time; start = time.perf_counter() #Since it also takes time to Import libs, I allways start the timer asap. 
import requests
import pandas as pd
from tqdm import tqdm
from bs4 import BeautifulSoup
from multiprocessing import Pool

''' ___ local imports __________'''
from postgres import databaseManager, getInputTable, deleteData
from file_manager import *

def linkBuilder(base_url, term):
	return f'{base_url}{term}'

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
	req = s.get(url, cookies = cookies, verify = True, allow_redirects = False)
	a = getSoup(req).find('a',{'href' : True})
	if a['href'] != '#query':
		url = 'https://www.1881.no/'+a['href']
		return s.get(url, cookies = cookies, verify = True, allow_redirects = False) 


def getSoup(req):
	return BeautifulSoup(req.content, "html.parser") #* -> soup

def findPromoDiv(soup):
	return soup.find('div', {'class':'box dm-promo'})

def newSoup(listing):
	''' 
		if soup is a listing; this will find a link 
		to the profile of the first list element 
	'''
	h2 = listing.find('h2',{'class' : "listing-name"})
	a = h2.find('a',{'href' : True})
	return getSoup(getRequest('https://www.1881.no/'+a['href']))


def checkIfList(soup):
	''' checks if page is a profile or a listing '''
	return soup.find('div',{'class':'box listing listing--business'})

def makeChunks(input_array, chunksize):
	return [input_array[i:i+chunksize] for i in range(0, len(input_array), chunksize)]  

def extractionManager(input_array):
	'''
		finds profile for company, then checks if profile 
		contains a promo banner for payed entries
	'''
	org_num = input_array[0]
	search_term = input_array[1]
	base_url = 'https://www.1881.no/?query='
	url = linkBuilder(base_url, str(org_num))
	req = getRequest(url)
	if req:
		soup = getSoup(req)
		''' #! USIKKER PÅ OM DENNE VIL KJØRE!!
		'''
		if not checkIfList(soup) and not soup.find('div',{'class':'box text-section'}) and not findPromoDiv(soup):
			# if not soup.find('div',{'class':'box text-section'}):
			# if not findPromoDiv(soup):
			deleteData(org_num, tablename = "input_table") #* All inputs that are found can be deleted from input_table  
			return org_num, search_term
				
def getSettings(kwargs):
	''' 
		Prepwork; fetches config-data & propriate input 
	'''
	file_name = 'I88I'
	chunksize = parseSettings(file_name)['chunk_size']
	input_array = (getInputTable(file_name))[['org_num', 'navn']].to_numpy()
	
	''' 
		making adjustments to settings based on **kawrg: "testmode" 
	'''
	if kwargs: 
		mode = 'Test Mode'
		tablename = '1881_test_output_table' #? [ALT] tablename = parseTablenames('1881', testmode = True)
		start_limit, end_limit = 674000, 674500
		input_array = input_array[start_limit : end_limit]
	else:
		mode = 'Publish Mode' #? [ALT]: mode = 'Final Mode'
		tablename = '1881_output_table' #? [ALT] tablename = parseTablenames('1881', testmode = False)
		start_limit, end_limit = 674000, None 				#! TEMP while testing 
		input_array = input_array[start_limit : end_limit]	
	return file_name, chunksize, mode, tablename, start_limit, end_limit, input_array

def printSettingsInfo(nested_input_array, testmode_kwarg):
	chunksize, mode, tablename, start_limit, end_limit, input_array = getSettings(testmode_kwarg)
	print(f"Running: {mode}")
	print(f"output_table used: {tablename}")
	print(f"Input_array starts from: [{start_limit}:{end_limit}]")
	print(f"chunksize: {chunksize}")
	print(f"input length: {len(input_array)}")
	print(f"number of chunks: {len(nested_input_array)}")
	print("\n\n\n")

def opplysningenExtractor(**kwargs):
	'''
		sets up all nessasary functions, then gets list of company names, 
		then iterates through the list via multithreading: claimedStatus().
	'''
	print("_"*62)
	print("|                  Starting: 1881 Extractor                  |")
	print("_"*62)
	print()

	testmode_kwarg = kwargs.get('testmode', None)
	chunksize, tablename, input_array = getSettings(testmode_kwarg)
	nested_input_array = makeChunks(input_array, chunksize) # divides input_array into chunks 
	printSettingsInfo(nested_input_array, testmode_kwarg)

	with tqdm(total = len(nested_input_array)) as pbar: 
		for input_array in nested_input_array:
			with Pool() as pool:
				results = list(tqdm(pool.imap_unordered(extractionManager, input_array), total = len(input_array)))
				results = [x for x in results if x is not None]
				df =  pd.DataFrame(results, columns = ['org_num', 'navn'])
				print(df)
				databaseManager(df, tablename)
				pbar.update(1)
	
	print("_"*62)
	print("                  Data Extraction Complete.                 ")
	print(f"                  Finished in {round(time.perf_counter() - start, 2)} second(s)                 ")
	print("_"*62)
	print()

if __name__ == '__main__':
	# opplysningenExtractor(testmode = True)
	opplysningenExtractor(testmode = False)
























'''
FIXME --- Where the issue was raised:
	
	 54%|██████████████████████████████████████                                | 970/1782 [11:48:19<10:03:34, 44.60s/it]
	100%|████████████████████████████████████████████████████████████████████████████▊| 499/500 [00:45<00:00,  2.54it/s]

	chunk :  970/1782 + (499/500) 
	input array : (485000 + 499) / 891_000 =  from [485000/89100] to [485499/891000] ==> (485000+189000)/(891000+189000) = from [674000/1080000] to [674499/1080000]
'''



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
812
*						Extracts (406K) units --> 	 33151.87 second(s)				  | => (1000) :  256.83 sec | [0.0816 s/unit]
*						Extracts (1000) units --> 	 81.11 second(s)				  | => (1000) :   81.11 sec | [0.0811 s/unit]
						Extracts (600) units -->  	 54.14 second(s)				  | => (1000) :   90.00 sec | [0.090 s/unit]
						Extracts (1000) units --> 	 256.83 second(s)				  | => (1000) :  256.83 sec | [0.257 s/unit]

*						_____ ESTIMATIONS _______
*						Estimated length of input_list: 						1.069.577 rows / [1069577]
*						Estimated total extraction time: 						[24:15:36] / [01:00:15:36]
* 

TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP'''
