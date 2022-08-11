''' TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP 
							
							_____ WHERE I LEFT OF _____
		
						__ISSUE:___
						Får noen ganger denne feilmeldingen:
						[0807/172348.241:INFO:CONSOLE(247)] "Autofocus processing was blocked because a document already has a focused element.", source: https://www.google.com/ (247) 
						
						Skraper 600 enheter --> 334.99 second(s)

TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP '''

import time; start = time.perf_counter() #Since it also takes time to Import libs, I allways start the timer asap. 
import re
import logging
import pandas as pd
import numpy as np
from tqdm import tqdm
import concurrent.futures
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from inspect import currentframe, getframeinfo

# ___ local imports __________
from config import payload, tablenames, settings
from postgres import databaseManager, getInputTable
from file_manager import *
from input_table import inputTable




'''
____ CMD code _____
python google.py
___________________


NOTES, TIME CALCULATION: 
	CHUNK_SIZE = 1 		--> 6.17s	| 					| 
	CHUNK_SIZE = 5 		--> 9.17s	| diff.tot: 3s 		| diff.pr: 3.00/05 		= 1.000s
	CHUNK_SIZE = 15		--> 18.38s	| diff.tot: 9.21s	| diff.pr: 9.21/15 		= 0.614s
	CHUNK_SIZE = 20		--> 23.27s	| diff.tot: 4.89s	| diff.pr: 4.89/20 		= 0.245s
	CHUNK_SIZE = 30		--> 27.1s	| diff.tot: 3.83s	| diff.pr: 3.83/30 		= 0.127s
	CHUNK_SIZE = 100	--> 52.65s	| diff.tot: 25.55s	| diff.pr: 25.55/100 	= 0.256s
	CHUNK_SIZE = 200	--> 94.53s	| diff.tot: s	| diff.pr: / 			= s
	CHUNK_SIZE = 300	--> 124.73s	| diff.tot: s	| diff.pr: / 			= s


	len : t/len
	1 	: 6.17
	5 	: 1.834
	15 	: 1.225
	20 	: 1.1635 
	30 	: 0.903 	[-0.2605s reduction, -22.38%]
	100	: 0.5265	[-0.3765s reduction, -41.69%]
	200 : 0.4727 	[-0.05385 reduction, -10.22%]
	300 : 0.4157	[-0.05700 reduction, -12.05%]



	estimert 
	500  : 0.3108
	1000 : 0.1835 


	totalElements: 1078364 | 1 078 364
	maxPages: 5677 | 53 919

	Current estimated time to extract:
	[CORRECT]	len(chunk)=100 	567758 	 | ----> 6.5d 
	[WRONG]		base t=1s 		10783.64 | 10 783.64s 	--> 179.72m  --> 2.99h
	[WRONG]		len(chunk)=100	5677.58  |  5 677.58s	--> 94m 	 --> 1.57h

	NOTE: 
		gjsn årlige nye bedrifter i norge: 66302


	overall konklusjon:
		
		første runde vil ta lang tid, ca: 1,57 + 2t + 2t = 6t 
							      pr stk: 0.005 + 
		oppdateringene vil ta kortere tid, ettersom brreg funksjonen (den kjappeste) 
		vil holde kontroll på hva som er nytt eller ikke og vil lage en spesifik download list basert på den. [TODO]
		alle extractors skal også inkludere en "ferdig" merknad, for ordensskyld. 

		den estimerte tiden på oppdateringsrundene er: 
		Hvis daglig; (66302/365) = 182 nye bedrifter hver dag.
			--> 95.823s + 95.823 + 95.823 = 287.46 
			==> ca 5m 
		ukentlig; 
			==> 33.5m 
		månentlig;
			==> 145.73m (2.42h)
		årlig; 
			==> 1748.76m (29.15h)100
'''

'''
RUNDOWN OF THE PROGRAM:
	[Updated 06.08.22]

		Part 1:	Extractor - Controlled by extractionManager();
							Fetches 'brreg_table' from database and makes a search-list -> np.array('org_num','name').
							Splits search-lists into chunks, then run iterates through reach chunk as a round.
							Each round the chunk is multithreaded, one thread pr list item, where selenium (chrome) 
							is used to make google searches, and look for relevant data (bool).
							the search-list-chunk is converted to a df, and then concat bool-data to it. 
							finally the df is passed forward to postgresManager() (part 2)

		Part 2: Postgres -  Controlled by postgresManager();
							For each iteration (chunks) -> fetches old df from database 
							(creates a new table if none exist), concats the new df, 
							then replaces the table with the final df. 
'''
	
'''
TODO: 
	
	- [X] bytt ut CSV  med database
	- [X] fix issue: "org_num" forsvinner -> feil i database & hindrer concat
	- [X] fix issue: selenium -> "unable to discover open pages"
	- [X] bytt ut postgres kode med en egen postgres-fil (postgres.py)
	- [X] rydd opp i imports
	- [ ] change system according to "NOTABLE FLAWS"
	- [ ] optimaliser tiden mål --> 2 timer
	- [ ] fullfør chunks --> alt research en annen måte å gjøre selenium multithreading
	- [X] oppdater webdriver (chrome)
	- [X] lag input_list i database + oppdater config
	- [ ] lag output_list i database + oppdater config
'''

'''
NOTABLE FLAWS: 
	- Slow Proccess:
		Systemet i dag (selenium + multithreading m/chunks) ekstrakter data veldig langsomt, 
		grunnet at webdriver ikke fungerer så bra med multithreading.

			Løsningsforslag: 
			En thread pr chunk i chunks, der webdriverne blir tildelt en chunk hver, 
			hvor den har X antall bedrifter å arbeide med før den lukkes ned. 

	- (mistanke) Cache Overflow:
		mulig jeg ikke beskriver problemet riktig, men jeg har en mistanke om et mulig problem;
		Å åpne opp mange nettlesere på en gang vil kanskje fylle opp noe "temp storage" (f.eks. cache)
		--> Vil gjøre maskinen treg veldig fort.(opplevde noe lignende, her om dagen 06.08.22)

			Løsningsforslag: 
			En thread pr chunk i chunks, der webdriverne blir tildelt en chunk hver, 
			hvor den har X antall bedrifter å arbeide med før den lukkes ned. 
'''

def getDriver():
	''' gets chrome driver '''
	return webdriver.Chrome(options = driverOptions())

def driverOptions():
	''' selenium settings for opening invisible webdrivers '''
	options = webdriver.ChromeOptions()
	options.add_experimental_option("excludeSwitches", ["enable-automation"]) # disable the automation bar [part 1]
	options.add_experimental_option('useAutomationExtension', False) # disable the automation bar [part 2]
	options.add_argument("--headless") # opens window as invisible
	options.add_argument("--disable-gpu") # disable GPU rendering (only software render) 
	options.add_argument('--no-sandbox') # Bypass OS security model	
	options.add_experimental_option('excludeSwitches', ['enable-logging'])  #stops webdriver from printing in console
	return options

def claimedStatus(chunk, driver):
	'''
		get the google page for the searchword, 
		then checks if the searchword is a registered business, 
		and if it is unclaimed.
		returns a np.array to saveData() for each iteration
	'''
	org_num = chunk[0]
	search_term = chunk[1]
	search = driver.find_element("name", "q")
	search.clear()
	search.send_keys(search_term+' maps')
	search.send_keys(Keys.RETURN)
	try: 
		check_business = driver.find_element(By.XPATH, '//*[@id="rhs"]/div')
		is_unreqistered = False
		try: 
			check_claimed = driver.find_element(By.XPATH, '//*[@id="kp-wp-tab-overview"]/div[2]/div/div/div/div/div/div[5]/div/div/div/div/a')
			is_unclaimed = True
		except:
			is_unclaimed = False
	except:
		is_unreqistered = True
		is_unclaimed = True
	return np.array((org_num, search_term, is_unreqistered, is_unclaimed), dtype = object)


def makeDataframe(status):
	''' makes dataframe from json '''
	df = pd.DataFrame([status], columns = ['org_num', 'navn', 'google Uregistrert', 'google Uerklært'])
	return df


def extractionManager(chunk):
	''' 
		import list 
		NB: remember to make sure it gets imported correctly 
		chunk = [] # consists of 500-1000 company names.
	'''

	''' generate driver for this worker'''
	base_url = "https://www.google.com/" 
	driver = getDriver()
	driver.get(base_url)

	''' bypass cookie-consent  '''
	WebDriverWait(driver, 0).until(EC.element_to_be_clickable((By.XPATH, './/*[@id="W0wltc"]'))).click()
	
	''' initiate scraper '''

	status = claimedStatus(chunk, driver)
	df = makeDataframe(status)
	# print("_"*100)
	# print('from extractionManager, printing df after claimedStatus():')	
	# print(f'line: {getLineNumber()}, print(df): \n{df}')
	# print()
	return df

def googleExtractor(testmode):
	'''
		sets up all nessasary functions, 
		then gets list of company names, 
		then iterates through the list via multithreading: claimedStatus().
	'''
	print("_"*91)
	print("|											  |")
	print("|			Starting: GOOGLE Extractor 			  |")
	print("|											  |")
	print("_"*91)
	print()

	''' preperations: parse config, connect to database and connect to api manager '''

	''' fetching data from config '''
	file_name = getFileName()	# fetches name of current file 
	tablename = parseTablenames(file_name) # fetches the appropriate tablename for current file
	settings = parseSettings(file_name)	# fetches the appropriate settings for current file
	

	chunk_size = settings['chunk_size']
	input_array = inputTable()	#get inputs from postgres database
	
	''' temporary code for testing '''
	if testmode == 'on':
		test_chunks = input_array[:chunk_size] 	# TEMP TEMP TEMP TEMP TEMP TEMP
		chunks = [test_chunks] 					# TEMP TEMP TEMP TEMP TEMP TEMP
	else:
		chunks = [input_array[x:x+chunk_size] for x in range(0, len(input_array),chunk_size)]
	for i, chunk in enumerate(chunks):
		print(f"Chunk number {i+1} / {len(chunks)}")
		with tqdm(total = len(chunks)) as pbar:
			with concurrent.futures.ThreadPoolExecutor() as executor:
					results = executor.map(extractionManager, chunk)
					for df in results:
						databaseManager(df, tablename)
						pbar.update(1)
	print("																		"+"_"*91)
	print("																		|											  |")
	print("																		|				   Data Extraction Complete. 				  |")
	print("																		|											  |")
	print("																		"+"_"*91)
	print()			
	print(f"|				   Finished in {round(time.perf_counter() - start, 2)} second(s)				  |")	









if __name__ == '__main__':
	'''
		sets up all nessasary functions, 
		then gets list of company names, 
		then iterates through the list via multithreading: claimedStatus().
	'''
	print("_"*91)
	print("|											  |")
	print("|			Starting: GOOGLE Extractor 			  |")
	print("|											  |")
	print("_"*91)
	print()

	''' preperations: parse config, connect to database and connect to api manager '''

	''' fetching data from config '''
	file_name = getFileName()	# fetches name of current file 
	tablename = parseTablenames(file_name) # fetches the appropriate tablename for current file
	settings = parseSettings(file_name)	# fetches the appropriate settings for current file
	chunk_size = settings['chunk_size']
	input_array = getInputTable(tablenames['input_table'])
	# input_array = inputTable()	#get inputs from postgres database
	# print(len(input_array))
	''' temporary code for testing '''
	# chunk_size = 50 # TEMP TEMP TEMP TEMP TEMP TEMP

	# index = [index for index, i in enumerate(input_array)]
	# test_chunks = [input_array[i::chunk_size] for i in range(len(input_array))]
	# test_chunks = input_array[(len(input_array)/chunk_size)::chunk_size] 	# TEMP TEMP TEMP TEMP TEMP TEMP

	# chunks = [test_chunks] 					# TEMP TEMP TEMP TEMP TEMP TEMP
	# chunks = [input_array[i::chunk_size] for i in range(len(input_array))]
	chunks = [input_array[x:x+chunk_size] for x in range(0, len(input_array),chunk_size)]

	# print(chunks[1])
	for i, chunk in enumerate(chunks):
		print(f"Chunk number {i+1} / {len(chunks)}")
		with tqdm(total = len(chunk)) as pbar:
			with concurrent.futures.ThreadPoolExecutor() as executor:
					results = executor.map(extractionManager, chunk)
					for df in results:
						# print("_"*100)
						# print('printing result from multithread:')	
						# print(f'line: {getLineNumber()}, print(result): \n{df}')
						# print()
						databaseManager(df, tablename)
						pbar.update(1)
	


	# [ OLD PRINT ]
	# 	print("_"*91)
	# 	print("|											  |")
	# 	print("|			Data Extraction Complete. 			  |")
	# 	print("|											  |")
	# 	print("_"*91)
	# 	print()

	print("																		"+"_"*91)
	print("																		|											  |")
	print("																		|				   Data Extraction Complete. 				  |")
	print("																		|											  |")
	print("																		"+"_"*91)
	print()			
	print(f"|				   Finished in {round(time.perf_counter() - start, 2)} second(s)				  |")








'''
	ISSUE LOG:

		Issue:
			Ett eller annet sted i koden forsvinner "org_num", 
			som fører til at det blir lagret feil i databasen og den hindrer concat.
			Dette må fikses.
		
			Update 1:
				I databaseManager; print(old_df): fant jeg df'en som manglet 'org_num'
				altså, df hentet fra database mangler org_num, 
				som betyr at org_num blir fjernet i insertData(df) før den blir lagret,
				og df er helt ok i databaseManager. 
			Issue origin: 
				insertData(df)

			Update 2: 
				etter jeg kommenterte ut concat forsvant problemet. 
			Issue origin: 
				line 281 --> "old_df.set_index(old_df['org_num'].squeeze(), inplace = True)"


		Issue: 
			I driverOptions() -> "--no-startup-window" raiser error: 
			"selenium.common.exceptions.WebDriverException: Message: unkown error: unable to discover open pages"
		
			failed solutions: 
				1. update selenium, chorme and driver 
				2. add argument: "--no-sandbox"
				3. remove arguments: "excludeSwitches", ["enable-automation"] & "useAutomationExtension", False
				4. change chunksize to 1
			
			possible solutions:
				- remove multithreading (might be related to multithreading-FLAW)
			working solution: 
				- replaced "--no-startup-window" with "options.add_argument("--headless")"

'''