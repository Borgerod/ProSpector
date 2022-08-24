''' TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP 
							
*						_____ WHERE I LEFT OF _____
-						[17.08.2022]


*						_____ EXTRACTION RECORD _______
*						Skraper 1000 enheter -->  	26.5 second(s)
	
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
TODO: potensiell annen måte å finne ut om de har betalt oppføring eller ikke
	i searchresults listen kan man se at enkelte er markert som "Low priority", 
	finn ut om det betyr "betalt oppføring" eller "premium oppføring"

	clue:
	 "search-container clear  low-priority"

	andre type merkeringer:
	"search-container clear PRF_PAK_INTRO"
	"search-container clear PRF_PAK_INFO"
	"search-container clear PRF_PAK_BASIS"
	"search-container clear PRF_PAK_STANDARD"
	"search-container clear PRF_PAK_TREFF"
	"search-container clear PRF_PAK_KOMPLETT"
TODO: finn alle typene og ranger dem. 

	1. "PRF_PAK_KOMPLETT"	[Betalt_oppføring] ---> KOMPLETT
	2. "PRF_PAK_TREFF"		[Betalt_oppføring] ---> TREFFLISTE
	3. "PRF_PAK_STANDARD"	[Betalt_oppføring] ---> STANDARD
	4. "PRF_PAK_BASIS"		[Betalt_oppføring] ---> BASIS
	5. "PRF_PAK_INTRO"		[Betalt_oppføring] ---> GRUNNPAKKE
	6. "PRF_PAK_INFO"		[Betalt_oppføring] --->	PRØVEMÅNED	[Dette må jo være folk som har gratis prøvemåned]
	7. "low_priority"		[gratis_oppføring]

	todo: finn forskjellen på "PRF_PAK_INFO" og "low_priority"

	!	NB: pass opp for ad-blocks på denne listen (ligger inni mellom)

'''
def linkBuilder(base_url, term):
	'''
		builds a search url based on only company name
	'''
	return f'{base_url}{term}' #* -> url
	# if isinstance(term, int):
	# 	return f'{base_url}{term}' #* -> url
	# else:
	# 	return f'{base_url}{genSearchTerm(term)}&type=firma' #* -> url

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
	''' 
		used by proffExtractor, divides input array into chunks 
	'''
	return [input_array[i:i+chunksize] for i in range(0, len(input_array), chunksize)]  

def extractionManager(input_array):
	'''
		finds profile for company, 
		then checks if profile contains a 
		promo banner for payed entries
	'''
	org_num = input_array[0]
	search_term = input_array[1]
	if not checkIfMissing(org_num):
		# print("Not Missing, continue") #TEMP - while testing
		source = 'proff.py'
		base_url = 'https://www.proff.no/bransjesøk?q='
		url = linkBuilder(base_url, str(org_num))       
		req = getRequest(url)
		soup = getSoup(req)
		try:
			promo = soup.find('div', class_="search-container-wrap")
			error = False
			tag = promo.div['class'][2]		
			if 'low-priority' in tag: 
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
				deleteData(org_num, tablename = "input_table") #* All inputs that are found can be deleted from input_table 
				# return checkPayScore(org_num, search_term, tag ,error)
				return org_num, search_term #,error
		except AttributeError:
			# tag = None 
			# error = True
			pass
			# return org_num, search_term, tag ,error
	else:
		# print("Missing, pass") #TEMP - while testing
		pass

def proffExtractor(**kwargs):
	'''
		sets up all nessasary functions, 
		then gets list of company names, 
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
		tablename = parseTablenames(file_name, testmode = True) # gets tablename based on filename, [filename + "_table" = tablename] e.g. gulesider.py -> gulesider_table.
		#! [ALT] tablename = 'gulsesider_test_table'
	else:
		parseTablenames(file_name, testmode = False)
		#! [ALT] tablename = 'gulesider_table'
	print(f"chunksize: {chunksize}")
	print(f"input length: {len(input_array)}")
	nested_input_array = makeChunks(input_array, chunksize) # divides input_array into chunks 
	print(f"number of chunks: {len(nested_input_array)}")
	nested_input_array = nested_input_array[1167:] #TEMP --- test
	with tqdm(total = len(nested_input_array)) as pbar: #TEMP --- TEST
		for input_array in nested_input_array:
			with Pool() as pool:
				results = list(tqdm(pool.imap_unordered(extractionManager, input_array), total = len(input_array)))
				results = [x for x in results if x is not None]
				df =  pd.DataFrame(results, columns = ['org_num', 'navn'])
				# print(df)
				databaseManager(df, tablename = "output_table")
				pbar.update(1) #TEMP --- TEST
	'''
		! ____ CURRENT ISSUE____
		- extractor wait untill ALL of the data has been gathered before it passes it to postgres
		TODO: løsningen er å lage sine egne chunks
	'''
	print("_"*62)
	print("                  Data Extraction Complete.                 ")
	print(f"                  Finished in {round(time.perf_counter() - start, 2)} second(s)                ")
	print("_"*62)
	print()

	# print("                                                                     "+"_"*91)
	# print("                                                                     |                  Data Extraction Complete.                  |")
	# print("                                                                     "+"_"*91)
	# print()
	# print(f"                                                                    |                  Finished in {round(time.perf_counter() - start, 2)} second(s)                  |")

if __name__ == '__main__':
	# proffExtractor(testmode = True)
	proffExtractor(testmode = False)

