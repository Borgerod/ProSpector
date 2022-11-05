import time; start = time.perf_counter() #Since it also takes time to Import libs, I allways start the timer asap. 
import requests
import pandas as pd
from tqdm import tqdm
from bs4 import BeautifulSoup
from multiprocessing import Pool

''' ___ local imports __________'''
from postgres import databaseManager, getInputTable, checkIfMissing, deleteData
from gulesider import errorManager 
from config import tablenames
from file_manager import *

def linkBuilder(base_url, term):
	return f'{base_url}{term}' #* -> url

def getRequest(url):
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
	return BeautifulSoup(req.content, "html.parser") #* -> soup

def checkPayScore(org_num, search_term, tag ,error):
		if 'PRF_PAK_KOMPLETT' in tag:
			print("True")
			tag_score = 6
			return org_num, search_term, tag_score ,error 
		elif 'PRF_PAK_TREFF' in tag: 
			tag_score = 5
			return org_num, search_term, tag_score ,error 
		elif 'PRF_PAK_STANDARD' in tag: 
			tag_score = 4
			return org_num, search_term, tag_score ,error 
		elif 'PRF_PAK_BASIS' in tag: 
			tag_score = 3
			return org_num, search_term, tag_score ,error 
		elif 'PRF_PAK_INTRO' in tag: 
			tag_score = 2
			return org_num, search_term, tag_score ,error 
		elif 'PRF_PAK_INFO' in tag: 
			tag_score = 1
			return org_num, search_term, tag_score ,error 

def makeChunks(input_array, chunksize):
	return [input_array[i:i+chunksize] for i in range(0, len(input_array), chunksize)]  

def extractionManager(input_array):
	'''
		finds profile for company, then checks if profile 
		contains a promo banner for payed entries
	'''
	org_num = input_array[0]
	search_term = input_array[1]
	if not checkIfMissing(org_num):
		source = 'proff.py'
		base_url = 'https://www.proff.no/bransjesøk?q='
		url = linkBuilder(base_url, str(org_num))       
		req = getRequest(url)
		soup = getSoup(req)
		try:
			promo = soup.find('div', class_="search-container-wrap")
			tag = promo.div['class'][2]		
			if 'low-priority' in tag: 
				pass
			else:
				deleteData(org_num, tablename = "input_table") #* All inputs that are found can be deleted from input_table 
				return org_num, search_term 
		except AttributeError as e:
			errorManager(org_num, search_term, source, url, e)
	else:
		pass

def proffExtractor(**kwargs):
	'''
		sets up all nessasary functions, then gets list of company names, 
		then iterates through the list via multithreading: claimedStatus().
	'''
	print("_"*62)
	print("|                  Starting: Proff Extractor                 |")
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
				databaseManager(df, tablename = "output_table")
				pbar.update(1) 
	print("_"*62)
	print("                  Data Extraction Complete.                 ")
	print(f"                  Finished in {round(time.perf_counter() - start, 2)} second(s)                ")
	print("_"*62)
	print()

if __name__ == '__main__':
	# proffExtractor(testmode = True)
	proffExtractor(testmode = False)








''' TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP 
							
*						_____ WHERE I LEFT OF _____
-						[17.08.2022]


*						_____ EXTRACTION RECORD _______
*						Extracts (1000) units -->  	26.5 second(s) 				  | => (1000) :  26.50 sec | [0.027 s/unit]
*						Extracts (483.500) units -->  	22029.89 second(s)		  | => (1000) :  45.60 sec | 0.0456 s/unit]	
						967 * 500 = 483500 [6:07:07]
*						Extracts (975500) units -->  	36402.69 second(s)		  | => (1000) :  37.30 sec | 0.0373 s/unit]	
						1951 * 500 = 975500 [10:06:42]

*						_____ ESTIMATIONS _______
*						Estimated length of input_list: 						1.069.577 rows / [1069577]
*						Estimated total extraction time: 						[13:32:52] / 812.88 minutes 
* 						ACTUAL TOTAL EXTRACTION TIME: 							[10:06:42] / 606.71 minutes
	
TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP'''
