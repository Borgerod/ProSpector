''' TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP  TEMP TEMP TEMP TEMP TEMP TEMP TEMP  TEMP TEMP TEMP TEMP TEMP TEMP 
							
*							_____ WHERE I LEFT OF _____
-						[14.08.2022]
-						holder på å teste ut hastigheten og om den klarer å skrape alt. 
-						error: - reached 829 before error:selenium.common.exceptions.TimeoutException: 

!						__ISSUE:___
-						Får noen ganger denne feilmeldingen:
-						[0807/172348.241:INFO:CONSOLE(247)] "Autofocus processing was blocked because a document already has a focused element.", source: https://www.google.com/ (247) 


TODO					[ ] [KANSKJE] legg til 'C-unlock' til googleExtractor()			
TODO 					[ ]	Change gooogleExtractor to pull input from designated list 		

*						_____ EXTRACTION RECORD _______
-						Skraper 200 enheter --> 	   77.52 second(s) (Etter Endringer)
-						Skraper 600 enheter -->  	  165.02 second(s)
												[old] 232.41 second(s)
												[old] 334.99 second(s)
						
TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP  TEMP TEMP TEMP TEMP TEMP TEMP TEMP  TEMP TEMP TEMP TEMP TEMP TEMP TEMP  TEMP TEMP TEMP TEMP TEMP TEMP TEMP '''

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
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from inspect import currentframe, getframeinfo
import os 
# ___ local imports __________
from config import payload, tablenames, settings
from postgres import databaseManager, getInputTable
from file_manager import *
from input_table import inputTable


'''! ISSUES:
	- reached 829 before error:
	error occored in on line: 220, claimedStatus --> search.send_keys(Keys.RETURN) 
	selenium.common.exceptions.TimeoutException: Message: timeout: Timed out receiving message from renderer: 300.000
'''

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


'''
! [OLD] OPPOSITE : unregistered not registered
'''

# def claimedStatus(chunk, driver):
	# '''
	# 	get the google page for the searchword, 
	# 	then checks if the searchword is a registered business, 
	# 	and if it is unclaimed.
	# 	returns a np.array to saveData() for each iteration
	# '''
	# org_num = chunk[0]
	# search_term = chunk[1]
	# search = driver.find_element("name", "q")
	# search.clear()
	# search.send_keys(search_term+' maps')
	# search.send_keys(Keys.RETURN)
	# try: 
	# 	check_business = driver.find_element(By.XPATH, '//*[@id="rhs"]/div')
	# 	is_unreqistered = False
	# 	try: 
	# 		check_claimed = driver.find_element(By.XPATH, '//*[@id="kp-wp-tab-overview"]/div[2]/div/div/div/div/div/div[5]/div/div/div/div/a')
	# 		is_unclaimed = True
	# 	except:
	# 		is_unclaimed = False
	# except:
	# 	is_unreqistered = True
	# 	is_unclaimed = True
	# return np.array((org_num, search_term, is_unreqistered, is_unclaimed), dtype = object)

'''
* [NEW] registered not unregistered
'''
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
		verify = driver.find_element(By.CLASS_NAME, "osrp-blk").get_attribute('innerHTML')
		if search_term in verify:
			check_business = driver.find_element(By.XPATH, '//*[@id="rhs"]/div')
			is_reqistered = True			
			check = driver.find_element(By.XPATH, '//*[@id="kp-wp-tab-overview"]/div[2]/div/div/div/div/div/div[5]/div/div/div')
			check_info = check.text
			if 'Add missing information' in check_info:
				has_info = False
			elif 'Legg til manglende informasjon' in check_info:
				has_info = False
			else: 
				has_info = True
			check_claimed = check.get_attribute('innerHTML')
			if 'cQhrTd' in check_claimed:
				is_claimed = True
			else:
				is_claimed = False
		else:
			is_reqistered = False
			is_claimed = False
			has_info = False			
	except NoSuchElementException as e:
		is_reqistered = False
		is_claimed = False
		has_info = False
	return np.array((org_num, search_term, is_reqistered, is_claimed, has_info), dtype = object)


# TEMP - test version of claimedStaturs():
# def claimedStatus(chunk, driver):
	# org_num = chunk[0]
	# search_term = chunk[1]

	# search = driver.find_element("name", "q")
	# search.clear()
	# search.send_keys(search_term+' maps')
	# search.send_keys(Keys.RETURN)
	# check_claimed = driver.find_element(By.XPATH, '//*[@id="kp-wp-tab-overview"]/div[2]/div/div/div/div/div/div[5]/div/div/div/div[1]')
	# claimed = driver.find_element(By.XPATH, '//*[@id="kp-wp-tab-overview"]/div[2]/div/div/div/div/div/div[5]/div/div/div/div[1]').get_attribute('innerHTML')
	# if 'cQhrTd' in claimed:
	# 	print(f"'cQhrTd' was found, {search_term} = is claimed")
	# 	is_claimed = True
	# else:
	# 	print(f"'cQhrTd' was NOT found, {search_term} = is unclaimed")
	# 	is_claimed = False

	# # pprint(claimed)
	# # print("_"*100)
	# print()
	# # time.sleep(1)

'''
PRETEST DATA:
	quick testnotes, regarding claimed_status:
	from original 
	nb: False mean "is unclaimed", True mean "is claimed"
	sreachterm: 'COMPANYNAME AS' + ' maps'
		[CLAIMED EXAMPLES]
		- Audun Breines Media: IS claimed [Fasit]
			- did contain '//*[@id="kp-wp-tab-overview"]/div[2]/div/div/div/div/div/div[5]/div/div/div/div/a'
			- html:	<a jsname="cQhrTd" 
					   href="https://business.google.com/create?hl=en&amp;getstarted&amp;authuser=0&amp;fp=11477126425961917591&amp;gmbsrc=no-en-et-ip-z-gmb-s-z-l~skp%7Cclaimbz_aoc_a%7Cu%7Cexp&amp;ppsrc=GMBSI" 
					   ping="/url?sa=t&amp;source=web&amp;rct=j&amp;url=https://business.google.com/create%3Fhl%3Den%26getstarted%26authuser%3D0%26fp%3D11477126425961917591%26gmbsrc%3Dno-en-et-ip-z-gmb-s-z-l~skp%257Cclaimbz_aoc_a%257Cu%257Cexp%26ppsrc%3DGMBSI&amp;ved=2ahUKEwi3-sH39cj5AhU0XvEDHUu7Av8Qk68FKAJ6BAhUEBA">Own this business?</a>
			- result: False 

		- PPHU PECHERZEWSKI: IS claimed [Fasit]
			- did contain '//*[@id="kp-wp-tab-overview"]/div[2]/div/div/div/div/div/div[5]/div/div/div/div/a'
			- html:	<a jsname="cQhrTd" 
					   href="https://business.google.com/create?hl=en&amp;getstarted&amp;authuser=0&amp;fp=4924767740126946066&amp;gmbsrc=no-en-et-ip-z-gmb-s-z-l~skp%7Cclaimbz_aoc_a%7Cu%7Cexp&amp;ppsrc=GMBSI" 
					   ping="/url?sa=t&amp;source=web&amp;rct=j&amp;url=https://business.google.com/create%3Fhl%3Den%26getstarted%26authuser%3D0%26fp%3D4924767740126946066%26gmbsrc%3Dno-en-et-ip-z-gmb-s-z-l~skp%257Cclaimbz_aoc_a%257Cu%257Cexp%26ppsrc%3DGMBSI&amp;ved=2ahUKEwiB8aSGg8n5AhV2X_EDHfZ4AiMQk68FKAJ6BAgzEBA">Own this business?</a>		
			- result: False 	

		[UNCLAIMED EXAMPLES]
		- ANN-MARIE VOLDHEIM: is NOT claimed [Fasit]
			- did NOT contain '//*[@id="kp-wp-tab-overview"]/div[2]/div/div/div/div/div/div[5]/div/div/div/div/a'
			- html: <span jsname="ZzN7De" class="PpkzKf">
						<span 	jscontroller="pk2t0e" 
								jsdata="Gp3Lk;_;Cd0tkk" 
								jsaction="qEUp2e:GpVthf"> 
							<a jsname="ndJ4N" 
							   href="#" 
							   role="button" 
							   jsaction="FNFY6c" 
							   data-ved="2ahUKEwjGtIjX_8j5AhVyX_EDHYdsATAQnW4oAnoECD8QEA"> Own this business? </a> 
							<span jsname="rWB2ud" 
								  data-ved="2ahUKEwjGtIjX_8j5AhVyX_EDHYdsATAQ-MgIKAN6BAg_EBE"></span> </span></span>
			- result: False

		- ANN-MARIE VOLDHEIM: is NOT claimed [Fasit]
			- did NOT contain '//*[@id="kp-wp-tab-overview"]/div[2]/div/div/div/div/div/div[5]/div/div/div/div/a'
			- html: <span jsname="ZzN7De" class="PpkzKf">
						<span jscontroller="pk2t0e" 
							  jsdata="Gp3Lk;_;Ak54ac" 
							  jsaction="qEUp2e:GpVthf"> 
							<a  jsname="ndJ4N" 
								href="#" 
								role="button" 
								jsaction="FNFY6c" 
								data-ved="2ahUKEwjBqvCd9sj5AhWPQvEDHZKcDFUQnW4oAnoECDwQEA"> Own this business? </a> 
							<span jsname="rWB2ud" 
								  data-ved="2ahUKEwjBqvCd9sj5AhWPQvEDHZKcDFUQ-MgIKAN6BAg8EBE"></span> </span></span>
			- result: False


	CONCLUTION: THE FORMULA SHOULD BE RIGHT, except:
		it seems like the program doenst have enough time to check. returning false
'''

'''
TEST 1:
	different: 
	- try returns is_claimed = True [false before]
	- except returns is_clamed = False [true before] 
	- uses small testlist
	nb: False mean "is claimed", True mean "is unclaimed"
	sreachterm: 'COMPANYNAME AS' + ' maps'
	
		[CLAIMED EXAMPLES]
		- Audun Breines Media: IS claimed [Fasit]
			- did contain '//*[@id="kp-wp-tab-overview"]/div[2]/div/div/div/div/div/div[5]/div/div/div/div/a'
			- html:	<a jsname="cQhrTd" 
					   href="https://business.google.com/create?hl=en&amp;getstarted&amp;authuser=0&amp;fp=11477126425961917591&amp;gmbsrc=no-en-et-ip-z-gmb-s-z-l~skp%7Cclaimbz_aoc_a%7Cu%7Cexp&amp;ppsrc=GMBSI" 
					   ping="/url?sa=t&amp;source=web&amp;rct=j&amp;url=https://business.google.com/create%3Fhl%3Den%26getstarted%26authuser%3D0%26fp%3D11477126425961917591%26gmbsrc%3Dno-en-et-ip-z-gmb-s-z-l~skp%257Cclaimbz_aoc_a%257Cu%257Cexp%26ppsrc%3DGMBSI&amp;ved=2ahUKEwi3-sH39cj5AhU0XvEDHUu7Av8Qk68FKAJ6BAhUEBA">Own this business?</a>
			- result: False 

		- PPHU PECHERZEWSKI: IS claimed [Fasit]
			- did contain '//*[@id="kp-wp-tab-overview"]/div[2]/div/div/div/div/div/div[5]/div/div/div/div/a'
			- html:	<a jsname="cQhrTd" 
					   href="https://business.google.com/create?hl=en&amp;getstarted&amp;authuser=0&amp;fp=4924767740126946066&amp;gmbsrc=no-en-et-ip-z-gmb-s-z-l~skp%7Cclaimbz_aoc_a%7Cu%7Cexp&amp;ppsrc=GMBSI" 
					   ping="/url?sa=t&amp;source=web&amp;rct=j&amp;url=https://business.google.com/create%3Fhl%3Den%26getstarted%26authuser%3D0%26fp%3D4924767740126946066%26gmbsrc%3Dno-en-et-ip-z-gmb-s-z-l~skp%257Cclaimbz_aoc_a%257Cu%257Cexp%26ppsrc%3DGMBSI&amp;ved=2ahUKEwiB8aSGg8n5AhV2X_EDHfZ4AiMQk68FKAJ6BAgzEBA">Own this business?</a>		
			- result: False 	

		[UNCLAIMED EXAMPLES]
		- ANN-MARIE VOLDHEIM: is NOT claimed [Fasit]
			- did NOT contain '//*[@id="kp-wp-tab-overview"]/div[2]/div/div/div/div/div/div[5]/div/div/div/div/a'
			- html: <span jsname="ZzN7De" class="PpkzKf">
						<span 	jscontroller="pk2t0e" 
								jsdata="Gp3Lk;_;Cd0tkk" 
								jsaction="qEUp2e:GpVthf"> 
							<a jsname="ndJ4N" 
							   href="#" 
							   role="button" 
							   jsaction="FNFY6c" 
							   data-ved="2ahUKEwjGtIjX_8j5AhVyX_EDHYdsATAQnW4oAnoECD8QEA"> Own this business? </a> 
							<span jsname="rWB2ud" 
								  data-ved="2ahUKEwjGtIjX_8j5AhVyX_EDHYdsATAQ-MgIKAN6BAg_EBE"></span> </span></span>
			- result: False

		- ANDRE HAGEN MUSIC	: is NOT claimed [Fasit]
			- did NOT contain '//*[@id="kp-wp-tab-overview"]/div[2]/div/div/div/div/div/div[5]/div/div/div/div/a'
			- html: <span jsname="ZzN7De" class="PpkzKf">
						<span jscontroller="pk2t0e" 
							  jsdata="Gp3Lk;_;Ak54ac" 
							  jsaction="qEUp2e:GpVthf"> 
							<a  jsname="ndJ4N" 
								href="#" 
								role="button" 
								jsaction="FNFY6c" 
								data-ved="2ahUKEwjBqvCd9sj5AhWPQvEDHZKcDFUQnW4oAnoECDwQEA"> Own this business? </a> 
							<span jsname="rWB2ud" 
								  data-ved="2ahUKEwjBqvCd9sj5AhWPQvEDHZKcDFUQ-MgIKAN6BAg8EBE"></span> </span></span>
			- result: False


	CONCLUTION: DID NOT WORK:
		it returned correct for cliamed but not unclaimed
'''

'''
TEST 2:
	different: 
	- try returns is_claimed = False [true before] 
	- except returns is_clamed =  True [false before]
	- uses small testlist
	- will not look for unclaimed instead of claimed, xpath: //*[@id="kp-wp-tab-overview"]/div[2]/div/div/div/div/div/div[5]/div/div/div/div[1]/span[2]/span/a
	nb: False mean "is claimed", True mean "is unclaimed"
	sreachterm: 'COMPANYNAME AS' + ' maps'
	
		[CLAIMED EXAMPLES]
		- Audun Breines Media: IS claimed [Fasit]
			- did contain '//*[@id="kp-wp-tab-overview"]/div[2]/div/div/div/div/div/div[5]/div/div/div/div/a'
			- html:	<a jsname="cQhrTd" 
					   href="https://business.google.com/create?hl=en&amp;getstarted&amp;authuser=0&amp;fp=11477126425961917591&amp;gmbsrc=no-en-et-ip-z-gmb-s-z-l~skp%7Cclaimbz_aoc_a%7Cu%7Cexp&amp;ppsrc=GMBSI" 
					   ping="/url?sa=t&amp;source=web&amp;rct=j&amp;url=https://business.google.com/create%3Fhl%3Den%26getstarted%26authuser%3D0%26fp%3D11477126425961917591%26gmbsrc%3Dno-en-et-ip-z-gmb-s-z-l~skp%257Cclaimbz_aoc_a%257Cu%257Cexp%26ppsrc%3DGMBSI&amp;ved=2ahUKEwi3-sH39cj5AhU0XvEDHUu7Av8Qk68FKAJ6BAhUEBA">Own this business?</a>
			- result: False 

		- PPHU PECHERZEWSKI: IS claimed [Fasit]
			- did contain '//*[@id="kp-wp-tab-overview"]/div[2]/div/div/div/div/div/div[5]/div/div/div/div/a'
			- html:	<a jsname="cQhrTd" 
					   href="https://business.google.com/create?hl=en&amp;getstarted&amp;authuser=0&amp;fp=4924767740126946066&amp;gmbsrc=no-en-et-ip-z-gmb-s-z-l~skp%7Cclaimbz_aoc_a%7Cu%7Cexp&amp;ppsrc=GMBSI" 
					   ping="/url?sa=t&amp;source=web&amp;rct=j&amp;url=https://business.google.com/create%3Fhl%3Den%26getstarted%26authuser%3D0%26fp%3D4924767740126946066%26gmbsrc%3Dno-en-et-ip-z-gmb-s-z-l~skp%257Cclaimbz_aoc_a%257Cu%257Cexp%26ppsrc%3DGMBSI&amp;ved=2ahUKEwiB8aSGg8n5AhV2X_EDHfZ4AiMQk68FKAJ6BAgzEBA">Own this business?</a>		
			- result: False 	

		[UNCLAIMED EXAMPLES]
		- ANN-MARIE VOLDHEIM: is NOT claimed [Fasit]
			- did NOT contain '//*[@id="kp-wp-tab-overview"]/div[2]/div/div/div/div/div/div[5]/div/div/div/div/a'
			- html: <span jsname="ZzN7De" class="PpkzKf">
						<span 	jscontroller="pk2t0e" 
								jsdata="Gp3Lk;_;Cd0tkk" 
								jsaction="qEUp2e:GpVthf"> 
							<a jsname="ndJ4N" 
							   href="#" 
							   role="button" 
							   jsaction="FNFY6c" 
							   data-ved="2ahUKEwjGtIjX_8j5AhVyX_EDHYdsATAQnW4oAnoECD8QEA"> Own this business? </a> 
							<span jsname="rWB2ud" 
								  data-ved="2ahUKEwjGtIjX_8j5AhVyX_EDHYdsATAQ-MgIKAN6BAg_EBE"></span> </span></span>
			- result: False

		- ANDRE HAGEN MUSIC	: is NOT claimed [Fasit]
			- did NOT contain '//*[@id="kp-wp-tab-overview"]/div[2]/div/div/div/div/div/div[5]/div/div/div/div/a'
			- html: <span jsname="ZzN7De" class="PpkzKf">
						<span jscontroller="pk2t0e" 
							  jsdata="Gp3Lk;_;Ak54ac" 
							  jsaction="qEUp2e:GpVthf"> 
							<a  jsname="ndJ4N" 
								href="#" 
								role="button" 
								jsaction="FNFY6c" 
								data-ved="2ahUKEwjBqvCd9sj5AhWPQvEDHZKcDFUQnW4oAnoECDwQEA"> Own this business? </a> 
							<span jsname="rWB2ud" 
								  data-ved="2ahUKEwjBqvCd9sj5AhWPQvEDHZKcDFUQ-MgIKAN6BAg8EBE"></span> </span></span>
			- result: False


	CONCLUTION: THE FORMULA SHOULD BE RIGHT, except:
		it seems like the program doenst have enough time to check. returning false
'''
 

def makeDataframe(status):
	''' makes dataframe from json '''
	df = pd.DataFrame([status], columns = ['org_num', 'navn', 'google_profil', 'google_erklært', 'komplett_profil'])
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
	claimedStatus(chunk, driver)
	try: 
		status = claimedStatus(chunk, driver)
		df = makeDataframe(status)
		return df
	except:
		print("DF returned NONE")
		pass 
	# print("_"*100)
	# print('from extractionManager, printing df after claimedStatus():')	
	# print(f'line: {getLineNumber()}, print(df): \n{df}')
	# print()


def makeChunks(input_array, chunksize):
	''' 
		used by proffExtractor, divides input array into chunks 
	'''
	return [input_array[i:i+chunksize] for i in range(0, len(input_array), chunksize)]  

# * ORIGINAL - disabled while testing
def googleExtractor():
	'''
		sets up all nessasary functions, 
		then gets list of company names, 
		then iterates through the list via multithreading: claimedStatus().
	'''
	print("_"*62)
	print("|                  Starting: Google Extractor                |")
	print("_"*62)
	print()
	''' preperations: parse config, connect to database and connect to api manager '''

	''' fetching data from config '''
	file_name = getFileName()	# fetches name of current file 
	tablename = parseTablenames(file_name) # fetches the appropriate tablename for current file
	settings = parseSettings(file_name)	# fetches the appropriate settings for current file
	chunksize = settings['chunk_size']
	input_array = fetchData('output_table').to_numpy()
	print(f'full input_array: {len(input_array)}')
	
	chunks = makeChunks(input_array, chunksize)
	print(f'current run uses {len(chunks)}')
	print(f'current run uses {len(chunks[0])}')
	print(f'example; first element in the first chunk: {chunks[0][0]}')
	print(f'number of workers in use {min(32, (os.cpu_count() or 1) + 4)}')
	# with tqdm(total = len(chunks)) as pbar:
	# 	# with concurrent.futures.ThreadPoolExecutor() as executor:
	# 	with concurrent.futures.ThreadPoolExecutor(max_workers=min(32, (os.cpu_count() or 1) + 4)) as executor:
	# 			results = executor.map(extractionManager, chunks)
	# 			for df in results:
	# 				if df is None:
	# 					pass
	# 				else:
	# 					databaseManager(df, tablename)
	# 				pbar.update(1)
	print("_"*62)
	print("                   Data Extraction Complete.                 ")
	print(f"                  Finished in {round(time.perf_counter() - start, 2)} second(s)                 ")
	print("_"*62)
	print()




# # TEMP - TEST VERSION:
# def googleExtractor():
# 	'''
# 		sets up all nessasary functions, 
# 		then gets list of company names, 
# 		then iterates through the list via multithreading: claimedStatus().
# 	'''
# 	# print("_"*91)
# 	# print("|			Starting: GOOGLE Extractor TEST			  |")
# 	# print("_"*91)
# 	# print()

# 	''' preperations: parse config, connect to database and connect to api manager '''

# 	''' fetching data from config '''
# 	file_name = getFileName()	# fetches name of current file 
# 	tablename = parseTablenames(file_name) # fetches the appropriate tablename for current file
# 	settings = parseSettings(file_name)	# fetches the appropriate settings for current file
# 	chunk_size = settings['chunk_size']
# 	# chunks = [	  [812721232,	"ANDRE HAGEN MUSIC"],]
# 				  # [815124022,	"1 P.P.H.U PECHERZEWSKI PECHERZEWSKI WALDEMAR"],]
# 				  # [811555622,	"AUDUN BREINES MEDIA"],]
# 				   # [812531042,	"ANN-MARIE VOLDHEIM"],
# 				  # [812721232,	"ANDRE HAGEN MUSIC"],]

# 	chunks = [[928434508,	"A. JENSEN KONSULENT"],
# 				  [811555622,	"AUDUN BREINES MEDIA"],
# 				  [811599492,	"2Ø SERVICE AS"],
# 				  [811699632,	"2 CLAP STUDIO DA"],
# 				  [811733652,	"BLUEBELL TELECOM AB"],
# 				  [811879312,	"17. MAI NEMDA KAUPANGER"],
# 				  [812467182,	"&MORE AS"],
# 				  [812531042,	"ANN-MARIE VOLDHEIM"],
# 				  [812587412,	"820 GRADER"],
# 				  [812721232,	"ANDRE HAGEN MUSIC"],
# 				  [815124022,	"1 P.P.H.U PECHERZEWSKI PECHERZEWSKI WALDEMAR"],]	
# 	# print(f'current run uses {len(chunks)} chunks')
# 	# print(f'each chunk has {len(chunks[0])} units')
# 	# print(f'example; first element in the first chunk: {chunks[0][0]}')
# 	# print(f'number of workers in use {min(32, (os.cpu_count() or 1) + 4)}')
	



# 	with tqdm(total = len(chunks)) as pbar:
# 		# with concurrent.futures.ThreadPoolExecutor() as executor:
# 		with concurrent.futures.ThreadPoolExecutor(max_workers = min(32, (os.cpu_count() or 1) + 4)) as executor:
# 				results = executor.map(extractionManager, chunks)
# 				for df in results:
# 					if df is None:
# 						pass			
# 					else:
# 						databaseManager(df, tablename = 'google_test_table')
# 					pbar.update(1)

# 	# with concurrent.futures.ThreadPoolExecutor() as executor:
# 	# 	results = executor.map(extractionManager, chunks)

# 	# print("																		"+"_"*91)
# 	# print("																		|				   TEST Complete. 				  |")
# 	# print("																		"+"_"*91)
# 	# print()			
# 	# print(f"|				   Finished in {round(time.perf_counter() - start, 2)} second(s)				  |")












if __name__ == '__main__':
	googleExtractor()

# søkeord [garantert]
# bilde galleri [garantert]
# "Er dette din bedrift?" [mulig]

# alle som kommer opp på søkelisten på f.eks "sko" er betalt.


# ! [OLD] googleExtractor()
# def googleExtractor(testmode):
	# '''
	# 	sets up all nessasary functions, 
	# 	then gets list of company names, 
	# 	then iterates through the list via multithreading: claimedStatus().
	# '''
	# print("_"*91)
	# print("|											  |")
	# print("|			Starting: GOOGLE Extractor 			  |")
	# print("|											  |")
	# print("_"*91)
	# print()

	# ''' preperations: parse config, connect to database and connect to api manager '''

	# ''' fetching data from config '''
	# file_name = getFileName()	# fetches name of current file 
	# tablename = parseTablenames(file_name) # fetches the appropriate tablename for current file
	# settings = parseSettings(file_name)	# fetches the appropriate settings for current file
	

	# chunk_size = settings['chunk_size']
	# input_array = inputTable()	#get inputs from postgres database
	
	# ''' temporary code for testing '''
	# if testmode == 'on':
	# 	test_chunks = input_array[:chunk_size] 	# TEMP TEMP TEMP TEMP TEMP TEMP
	# 	chunks = [test_chunks] 					# TEMP TEMP TEMP TEMP TEMP TEMP
	# else:
	# 	chunks = [input_array[x:x+chunk_size] for x in range(0, len(input_array),chunk_size)]
	# for i, chunk in enumerate(chunks):
	# 	print(f"Chunk number {i+1} / {len(chunks)}")
	# 	with tqdm(total = len(chunks)) as pbar:
	# 		with concurrent.futures.ThreadPoolExecutor() as executor:
	# 				results = executor.map(extractionManager, chunk)
	# 				for df in results:
	# 					databaseManager(df, tablename)
	# 					# deleteData(df['org_num'], tablename = 'input_table')
	# 					pbar.update(1)
	# print("																		"+"_"*91)
	# print("																		|											  |")
	# print("																		|				   Data Extraction Complete. 				  |")
	# print("																		|											  |")
	# print("																		"+"_"*91)
	# print()			
	# print(f"|				   Finished in {round(time.perf_counter() - start, 2)} second(s)				  |")	


''' ISSUE LOG:

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


# <div class="SOGtLd duf-h"><span><span jscontroller="tuZ5Wc"><a href="#" 
# role="button" jsaction="CnOdef" 
# data-ved="2ahUKEwiircXGk8n5AhVPQ_EDHc4RAqEQ220oAHoECDMQAQ">Foreslå en 
# endring</a><div jscontroller="ql2uGc" style="display:none" 
# jsaction="nD2Qwd:CnOdef;Q53UPc:r9DEDb"><g-dialog jsname="Sx9Kwc" 
# jscontroller="VEbNoe" data-id="_E2X6YuLXMM-Gxc8PzqOIiAo45" 
# jsaction="jxvro:Imgh9b" jsdata="gctHtc;_;BE2Sjs" jsshadow="" 
# data-ved="2ahUKEwiircXGk8n5AhVPQ_EDHc4RAqEQrccDKAF6BAgzEAI" id="ow101" 
# __is_owner="true"><div jsname="XKSfm" id="_E2X6YuLXMM-Gxc8PzqOIiAo45" 
# jsaction="dBhwS:TvD9Pc;mLt3mc" jsowner="ow101"><div jsname="bF1uUb" 
# class="t7xA6 lxG8Hd"></div><div class="bErdLd hFCnyd wwYr3"><div 
# class="ls8Qne" aria-hidden="true" role="button" tabindex="0" 
# jsaction="focus:sT2f3e"></div><span jsslot=""><div class="NJfJb TUOsUe 
# Sr5CLc" aria-label="Foreslå en endring" role="dialog"><g-dialog-content 
# jscontroller="eX5ure" class="BhtQQc ctQZ2b" data-dc="" data-id="" 
# jsshadow="" jsaction="ATJmhe:uOhSee;rcuQ6b:npT2md" style="display: 
# block;"><div jsname="otLmXd" class="sQPTEb gxMdVd yUgQte"><span 
# jsname="LBJcic" class="guvOkb I7Y2H eY4mx u60jwe Tbiej z1asCe u3p1Tb" 
# aria-label="Tilbake" role="button" tabindex="0" jsaction="iO11jf" 
# style="display: none;"><svg focusable="false" 
# xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M15.41 
# 16.59L10.83 12l4.58-4.59L14 6l-6 6 6 6 1.41-1.41z"></path></svg></span><span 
# jsname="X0x7he" class="MBoHTc OSrXXb" style="width: calc(100% - 48px);"><div 
# jsslot=""><div jsname="Ud7fr" class="dedUFc" aria-level="2" 
# role="heading">Foreslå en endring</div></div></span><span 
# jsaction="QQtcRd"><span jsname="vDg59d" class="mU1bAd NLkY2 z1asCe wuXmqc" 
# aria-label="Lukk" role="button" tabindex="0"><svg focusable="false" 
# xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M19 
# 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 
# 19 19 17.59 13.41 12z"></path></svg></span></span></div><div jsname="EMr7db" 
# class="eJIuwd"><div jsslot=""><div class="hlZk0e diAzE"><div><div 
# jsname="dXj7Kb" jsaction="lQuKqf" class="HIIRYc" 
# aria-describedby="_E2X6YuLXMM-Gxc8PzqOIiAo46" 
# aria-labelledby="_E2X6YuLXMM-Gxc8PzqOIiAo47" role="button" tabindex="0" 
# data-ved="2ahUKEwiircXGk8n5AhVPQ_EDHc4RAqEQqccDegQIMxAE"><span 
# class="JpaZw"><span class="z1asCe QJh5z"><svg focusable="false" 
# xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M3 
# 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25zM20.71 7.04c.39-.39.39-1.02 
# 0-1.41l-2.34-2.34c-.39-.39-1.02-.39-1.41 0l-1.83 1.83 3.75 3.75 
# 1.83-1.83z"></path></svg></span></span><div class="WcZOu Aajd3"><div 
# jsname="eSHGZ" class="sAwMGb" id="_E2X6YuLXMM-Gxc8PzqOIiAo47">Endre navn 
# eller annen informasjon</div><div class="oxc7Ze" 
# id="_E2X6YuLXMM-Gxc8PzqOIiAo46">Endre navn, sted, åpningstider 
# osv.</div></div><div jsname="YOoDJc" jscontroller="SHXTGd" 
# data-enable-iframe-replace-history-state-for-sign-in="true" 
# data-is-desktop="true" data-is-internal="false" 
# data-show-thank-you-with-review-button="false" 
# data-submit-merchant-fact-feedback-as-authority="false" 
# jsdata="p0DzRe;_;BE2SkU" 
# jsaction="rcuQ6b:npT2md;LhF17c:UYWrmf;DIyoDc:ZiN7ye"><iframe jsname="L5Fo6c" 
# class="wXRMUd" id="_E2X6YuLXMM-Gxc8PzqOIiAo48" 
# name="_E2X6YuLXMM-Gxc8PzqOIiAo48" style="display:none"></iframe><g-dialog 
# jsname="zvMqKc" jscontroller="VEbNoe" data-id="_E2X6YuLXMM-Gxc8PzqOIiAo49" 
# jsaction="jxvro:Imgh9b" jsdata="gctHtc;_;BE2Sjs" jsshadow="" 
# data-ved="2ahUKEwiircXGk8n5AhVPQ_EDHc4RAqEQrMcDegQIMxAF" id="ow183" 
# __is_owner="true"><div jsname="XKSfm" id="_E2X6YuLXMM-Gxc8PzqOIiAo49" 
# jsaction="dBhwS:TvD9Pc;mLt3mc" jsowner="ow183"><div jsname="bF1uUb" 
# class="t7xA6 lxG8Hd"></div><div class="bErdLd hFCnyd wwYr3"><div 
# class="ls8Qne" aria-hidden="true" role="button" tabindex="0" 
# jsaction="focus:sT2f3e"></div><span jsslot=""><div class="NJfJb TUOsUe 
# Sr5CLc" role="dialog"><div class="ytfbqf"><div class="SVeWrb MBeuO">Takk for 
# tilbakemeldingen.</div><div class="a6TDuf"><p>Svarene du sender oss, bidrar 
# til å forbedre Google-søkeopplevelsen.</p><p><span>Merk: Tilbakemeldingene 
# du sender inn, kommer ikke til å påvirke rangeringen til enkeltsider 
# direkte.</span><br><a class="Kf7Xmd" 
# href="https://support.google.com/websearch/answer/3338405" 
# target="_blank">Finn ut mer</a></p><div class="WdHfdb"><g-flat-button 
# class="Zx8j0b U8shWc r2fjmd hObAcc gTewb VDgVie Vy8nid fSXIc" 
# jsaction="trigger.dBhwS" style="color:#1a73e8" role="button" 
# tabindex="0">Ferdig</g-flat-button></div></div></div></div></span><div 
# class="ls8Qne" aria-hidden="true" role="button" tabindex="0" 
# jsaction="focus:tuePCd"></div></div></div></g-dialog><div jsname="JzBN5" 
# jscontroller="b1qkGc"><input jsname="g4KAJd" accept="image/*" multiple="" 
# type="file" jsaction="change:mo1zIe" style="display:none"><g-snackbar 
# jsname="Ng57nc" jscontroller="OZLguc" style="display:none" jsshadow="" 
# jsaction="rcuQ6b:npT2md" id="ow185" __is_owner="true"><div jsname="Ng57nc" 
# class="FEXCIb" data-ved="2ahUKEwiircXGk8n5AhVPQ_EDHc4RAqEQ4G96BAgzEAg" 
# jsowner="ow185"><div class="EA3l1b"><div class="Xb004" jsslot=""><span 
# class="awHmMb wHYlTd yUTMj">Kan ikke legge til denne filen. Sjekk at det er 
# et gyldig bilde.</span></div></div></div></g-snackbar></div></div></div><div 
# jsname="dXj7Kb" jsaction="lQuKqf" class="HIIRYc" 
# aria-describedby="_E2X6YuLXMM-Gxc8PzqOIiAo50" 
# aria-labelledby="_E2X6YuLXMM-Gxc8PzqOIiAo51" role="button" tabindex="0" 
# data-ved="2ahUKEwiircXGk8n5AhVPQ_EDHc4RAqEQqccDegQIMxAJ"><span 
# class="JpaZw"><span class="z1asCe MtQc8b"><svg focusable="false" 
# xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 6.5c1.38 
# 0 2.5 1.12 2.5 2.5 0 .74-.33 1.39-.83 1.85l3.63 3.63c.98-1.86 1.7-3.8 
# 1.7-5.48 0-3.87-3.13-7-7-7-1.98 0-3.76.83-5.04 2.15l3.19 3.19c.46-.52 
# 1.11-.84 1.85-.84zm4.37 9.6l-4.63-4.63-.11-.11L3.27 3 2 4.27l3.18 3.18C5.07 
# 7.95 5 8.47 5 9c0 5.25 7 13 7 13s1.67-1.85 3.38-4.35L18.73 21 20 
# 19.73l-3.63-3.63z"></path></svg></span></span><div class="WcZOu Aajd3"><div 
# jsname="eSHGZ" class="sAwMGb" id="_E2X6YuLXMM-Gxc8PzqOIiAo51">Steng eller 
# fjern</div><div class="oxc7Ze" id="_E2X6YuLXMM-Gxc8PzqOIiAo50">Merk som 
# stengt, ikke-eksisterende eller duplikat</div></div><div jsname="YOoDJc" 
# jscontroller="SHXTGd" 
# data-enable-iframe-replace-history-state-for-sign-in="true" 
# data-is-desktop="true" data-is-internal="false" 
# data-show-thank-you-with-review-button="false" 
# data-submit-merchant-fact-feedback-as-authority="false" 
# jsdata="p0DzRe;_;BE2Skg" 
# jsaction="rcuQ6b:npT2md;LhF17c:UYWrmf;DIyoDc:ZiN7ye"><iframe jsname="L5Fo6c" 
# class="wXRMUd" id="_E2X6YuLXMM-Gxc8PzqOIiAo52" 
# name="_E2X6YuLXMM-Gxc8PzqOIiAo52" style="display:none"></iframe><g-dialog 
# jsname="zvMqKc" jscontroller="VEbNoe" data-id="_E2X6YuLXMM-Gxc8PzqOIiAo53" 
# jsaction="jxvro:Imgh9b" jsdata="gctHtc;_;BE2Sjs" jsshadow="" 
# data-ved="2ahUKEwiircXGk8n5AhVPQ_EDHc4RAqEQrMcDegQIMxAK" id="ow187" 
# __is_owner="true"><div jsname="XKSfm" id="_E2X6YuLXMM-Gxc8PzqOIiAo53" 
# jsaction="dBhwS:TvD9Pc;mLt3mc" jsowner="ow187"><div jsname="bF1uUb" 
# class="t7xA6 lxG8Hd"></div><div class="bErdLd hFCnyd wwYr3"><div 
# class="ls8Qne" aria-hidden="true" role="button" tabindex="0" 
# jsaction="focus:sT2f3e"></div><span jsslot=""><div class="NJfJb TUOsUe 
# Sr5CLc" role="dialog"><div class="ytfbqf"><div class="SVeWrb MBeuO">Takk for 
# tilbakemeldingen.</div><div class="a6TDuf"><p>Svarene du sender oss, bidrar 
# til å forbedre Google-søkeopplevelsen.</p><p><span>Merk: Tilbakemeldingene 
# du sender inn, kommer ikke til å påvirke rangeringen til enkeltsider 
# direkte.</span><br><a class="Kf7Xmd" 
# href="https://support.google.com/websearch/answer/3338405" 
# target="_blank">Finn ut mer</a></p><div class="WdHfdb"><g-flat-button 
# class="Zx8j0b U8shWc r2fjmd hObAcc gTewb VDgVie Vy8nid fSXIc" 
# jsaction="trigger.dBhwS" style="color:#1a73e8" role="button" 
# tabindex="0">Ferdig</g-flat-button></div></div></div></div></span><div 
# class="ls8Qne" aria-hidden="true" role="button" tabindex="0" 
# jsaction="focus:tuePCd"></div></div></div></g-dialog><div jsname="JzBN5" 
# jscontroller="b1qkGc"><input jsname="g4KAJd" accept="image/*" multiple="" 
# type="file" jsaction="change:mo1zIe" style="display:none"><g-snackbar 
# jsname="Ng57nc" jscontroller="OZLguc" style="display:none" jsshadow="" 
# jsaction="rcuQ6b:npT2md" id="ow189" __is_owner="true"><div jsname="Ng57nc" 
# class="FEXCIb" data-ved="2ahUKEwiircXGk8n5AhVPQ_EDHc4RAqEQ4G96BAgzEA0" 
# jsowner="ow189"><div class="EA3l1b"><div class="Xb004" jsslot=""><span 
# class="awHmMb wHYlTd yUTMj">Kan ikke legge til denne filen. Sjekk at det er 
# et gyldig 
# bilde.</span></div></div></div></g-snackbar></div></div></div></div></div></div></div></g-dialog-content></div></span><div 
# class="ls8Qne" aria-hidden="true" role="button" tabindex="0" 
# jsaction="focus:tuePCd"></div></div></div></g-dialog></div></span></span> · 
# <a 
# href="https://business.google.com/create?hl=no&amp;getstarted&amp;authuser=0&amp;fp=2523340993131639365&amp;gmbsrc=no-no-et-ip-z-gmb-s-z-l~skp%7Cclaimbz%7Cu%7Cexp&amp;ppsrc=GMBSI" 
# data-jsarwt="1" data-usg="AOvVaw2UZgkYh4HGB06NRsqIUNx6" 
# data-ved="2ahUKEwiircXGk8n5AhVPQ_EDHc4RAqEQnW4oAnoECDMQDg">Eier du denne 
# bedriften?</a></div