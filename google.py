# ''' TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP  TEMP TEMP TEMP TEMP TEMP TEMP TEMP  TEMP TEMP TEMP TEMP TEMP TEMP 
							
# *							_____ WHERE I LEFT OF _____
# -						[14.08.2022]
# -						holder på å teste ut hastigheten og om den klarer å skrape alt. 
# -						error: - reached 829 before error:selenium.common.exceptions.TimeoutException: 

# !						__ISSUE:___
# -						Får noen ganger denne feilmeldingen:
# -						[0807/172348.241:INFO:CONSOLE(247)] "Autofocus processing was blocked because a document already has a focused element.", source: https://www.google.com/ (247) 


# TODO					[ ] [KANSKJE] legg til 'C-unlock' til googleExtractor()			
# TODO 					[ ]	Change gooogleExtractor to pull input from designated list 		

# *						_____ EXTRACTION RECORD _______
# -						Skraper 200 enheter --> 	   77.52 second(s) (after changes) | => (1000 enheter) : 00:06:27 | [0.388 s/enh]
# -						Skraper 600 enheter -->  	  165.02 second(s)				   | => (1000 enheter) : 00:04:35 | [0.275 s/enh]
# 												[old] 232.41 second(s)
# 												[old] 334.99 second(s)

# *						_____ ESTIMATIONS _______
# *						Estimated length of google_input_list (output_list): 	10.000 rows / [10000]
# *						Estimated total extraction time: 						[01:04:36] / 64.6 minutes

# TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP  TEMP TEMP TEMP TEMP TEMP TEMP TEMP  TEMP TEMP TEMP TEMP TEMP TEMP TEMP  TEMP TEMP TEMP TEMP TEMP TEMP TEMP '''


import re, csv
from time import sleep, time
from random import uniform, randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException    
import time; start = time.perf_counter() #Since it also takes time to Import libs, I allways start the timer asap. 
import re
import logging
import pandas as pd
import numpy as np
from tqdm import tqdm
# import concurrent.futures
from concurrent.futures import ThreadPoolExecutor, as_completed
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from inspect import currentframe, getframeinfo
import os
import pickle 
import datetime


# ___ local imports __________
from config import payload, tablenames, settings
from postgres import databaseManager, getInputTable
from file_manager import *
from input_table import inputTable


''' * ____ CATCHPA SOLVER __________________________________________________________________________
'''
def write_stat(loops, time):
	with open('stat.csv', 'a', newline='') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',',
								quotechar='"', quoting=csv.QUOTE_MINIMAL)
		spamwriter.writerow([loops, time])  	 
	
def check_exists_by_xpath(xpath):
	try:
		driver.find_element_by_xpath(xpath)
	except NoSuchElementException:
		return False
	return True
	
def wait_between(a,b):
	rand=uniform(a, b) 
	sleep(rand)
 
def dimention(driver): 
	d = int(driver.find_element_by_xpath('//div[@id="rc-imageselect-target"]/table').get_attribute("class")[-1]);
	return d if d else 3  # dimention is 3 by default
	
def catchpaSolver(driver):
	mainWin = driver.current_window_handle  

	# move the driver to the first iFrame 
	driver.switch_to_frame(driver.find_elements_by_tag_name("iframe")[0])

	# *************  locate CheckBox  **************
	CheckBox = WebDriverWait(driver, 10).until(
			EC.presence_of_element_located((By.ID ,"recaptcha-anchor"))
			) 

	# *************  click CheckBox  ***************
	wait_between(0.5, 0.7)  
	# making click on captcha CheckBox 
	CheckBox.click() 
	 
	#***************** back to main window **************************************
	driver.switch_to_window(mainWin)  

	wait_between(2.0, 2.5) 

	# ************ switch to the second iframe by tag name ******************
	driver.switch_to_frame(driver.find_elements_by_tag_name("iframe")[1])  
	i=1
	while i<130:
		print('\n\r{0}-th loop'.format(i))
		# ******** check if checkbox is checked at the 1st frame ***********
		driver.switch_to_window(mainWin)   
		WebDriverWait(driver, 10).until(
			EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME , 'iframe'))
			)  
		wait_between(1.0, 2.0)
		if check_exists_by_xpath('//span[@aria-checked="true"]'): 
			import winsound
			winsound.Beep(400,1500)
			write_stat(i, round(time()-start) - 1 ) # saving results into stat file
			break 
			
		driver.switch_to_window(mainWin)   
		# ********** To the second frame to solve pictures *************
		wait_between(0.3, 1.5) 
		driver.switch_to_frame(driver.find_elements_by_tag_name("iframe")[1]) 
		solve_images(driver)
		i=i+1
	
def solve_images(driver): # main procedure to identify and submit picture solution	
	WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.ID ,"rc-imageselect-target"))
		) 		
	dim = dimention(driver)	
	# ****************** check if there is a clicked tile ******************
	if check_exists_by_xpath('//div[@id="rc-imageselect-target"]/table/tbody/tr/td[@class="rc-imageselect-tileselected"]'):
		rand2 = 0
	else:  
		rand2 = 1 

	# wait before click on tiles 	
	wait_between(0.5, 1.0)		 
	# ****************** click on a tile ****************** 
	tile1 = WebDriverWait(driver, 10).until(
		EC.element_to_be_clickable((By.XPATH ,   '//div[@id="rc-imageselect-target"]/table/tbody/tr[{0}]/td[{1}]'.format(randint(1, dim), randint(1, dim )))) 
		)   
	tile1.click() 
	if (rand2):
		try:
			driver.find_element_by_xpath('//div[@id="rc-imageselect-target"]/table/tbody/tr[{0}]/td[{1}]'.format(randint(1, dim), randint(1, dim))).click()
		except NoSuchElementException:          		
			print('\n\r No Such Element Exception for finding 2nd tile')
   
	 
	#****************** click on submit buttion ****************** 
	driver.find_element_by_id("recaptcha-verify-button").click()
''' * ________________________________________________________________________________________________
'''

# * ---------- SETIINGS ----------
# TODO [ ] Turn settings into class
def getSettings(kwargs): 
	''' 
		Prepwork; fetches config-data & input. Called by googleExtractor()
	'''
	file_name = 'google'
	chunksize = parseSettings(file_name)['chunk_size']
	# ! input_array = (getInputTable(file_name))[['org_num', 'navn']].to_numpy() #![ORIGINAL] temporary disabled B/C input_table might be corrupt by faulty versions
	input_array = fetchData('google_input_table').to_numpy()
	
	''' making adjustments to settings based on **kawrg: "testmode" 
	'''
	if kwargs: #! [OLD] if kwargs.get('testmode', None):
		mode = 'Test Mode'
		tablename = 'google_test_output_table' #? [ALT] tablename = parseTablenames('1881', testmode = True)
		start_limit, end_limit = 50, 150
		input_array = input_array[start_limit : end_limit]
	else:
		mode = 'Publish Mode'
		tablename = 'google_output_table' #? [ALT] tablename = parseTablenames('1881', testmode = False)
		start_limit, end_limit = None, None 				
		input_array = input_array[start_limit : end_limit]

	long_break, short_break = getLongBreak(), getShortBreak()	
	return file_name, chunksize, mode, tablename, start_limit, end_limit, input_array, long_break, short_break

def getLongBreak()-> int:
	''' -> long_break '''
	return 120

def getShortBreak() -> int:
	''' -> short_break '''
	return 2

def driverOptions():
	''' selenium settings for opening invisible webdrivers '''
	options = webdriver.ChromeOptions()
	options.add_experimental_option("excludeSwitches", ["enable-automation"]) # disable the automation bar [part 1]
	options.add_experimental_option('useAutomationExtension', False) # disable the automation bar [part 2]
	options.add_argument("window-size=1920,1080")
	options.add_argument("--headless") # opens window as invisible
	options.add_argument("--disable-gpu") # disable GPU rendering (only software render) 
	options.add_argument('--no-sandbox') # Bypass OS security model	
	options.add_experimental_option('excludeSwitches', ['enable-logging'])  #stops webdriver from printing in console
	options.add_experimental_option("excludeSwitches", ["enable-automation"])
	options.add_experimental_option('excludeSwitches', ['enable-logging'])
	options.add_experimental_option('useAutomationExtension', False)
	options.add_argument('--disable-blink-features=AutomationControlled')

	# options.add_argument(f'--user-agent="{UserAgent().random}"')
	# options.add_argument('--user-agent="Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166"')
	return options
# * ---------- SETIINGS ----------


def infoPrint(nested_input_array, testmode_kwarg):
	'''
		prints useful information about the run and it's settings. Called by googleExtractor()
	'''
	file_name, chunksize, mode, tablename, start_limit, end_limit, input_array, long_break, short_break = getSettings(testmode_kwarg)
	print(f"Running: {mode}")
	print(f"Output_table used: {tablename}")
	print(f"Input_array starts from: [{start_limit}:{end_limit}]")
	print(f"Chunksize: {chunksize}")
	print(f"Input length: {len(input_array)}")
	print(f"Number of chunks: {len(nested_input_array)}")
	print(f"""Break procedure: 
	will take a long break between each chunk; [{str(datetime.timedelta(seconds=long_break))}], 
	and a short break between every iteration; [{str(datetime.timedelta(seconds=short_break))}]""")
	print("\n\n\n")

def introPrint():
	print("_"*62)
	print("                  Starting: Google Extractor                ")
	print("_"*62)
	print()

def outroPrint():
	print("_"*62)
	print("                   Data Extraction Complete.                 ")
	print(f"                  Finished in {round(time.perf_counter() - start, 2)} second(s)                 ")
	print("_"*62)
	print()

def getDriver():
	''' gets chrome driver '''
	return webdriver.Chrome(options = driverOptions())

def makeChunks(input_array, chunksize):
	''' 
		used by proffExtractor, divides input array into chunks. Called by googleExtractor()
	'''
	return [input_array[i:i + chunksize] for i in range(0, len(input_array), chunksize)]  

def linkBuilder(base_url, search_term):
	'''
		builds urls based on search_term. Called by extractionManager()
	'''
	return base_url + search_term + ' maps'

def makeDataframe(status_list):
	''' 
		makes dataframe "google_output_table" from ThreadPoolExecutor output. Called by googleExtractor()
	'''
	df = pd.DataFrame(status_list, columns = ['org_num', 'navn', 'google_profil', 'eier_erklært', 'komplett_profil'])
	return df

def checkGoogleAlarmTrigger(driver):
	html = driver.page_source
	return ('Systemene våre har oppdaget uvanlig trafikk' or 'unnusual traffic') in html

def extractionManager(input_array):
	''' 
		import list 
		NB: remember to make sure it gets imported correctly 
		chunk = [] # consists of 500-1000 company names.
	'''
	org_num = input_array[0]
	search_term = input_array[1]

	base_url = "https://www.google.com/search?q=" 
	driver = getDriver()
	driver.get(linkBuilder(base_url, search_term))
	mainWin = driver.current_window_handle  #* CATCHPA SOLVER
	time.sleep(getShortBreak())
	if checkGoogleAlarmTrigger(driver):
		return None
	try:			 #[try A]	
		if driver.find_element(By.CLASS_NAME, "osrp-blk"):
			verify = driver.find_element(By.CLASS_NAME, "osrp-blk").text
			alt_search_term = search_term
			for ch in [' AS',' ASA', ' AB']:
				if ch in search_term:
					alt_search_term = search_term.replace(ch,"")
			alt_verify = [re.sub(r"[^a-zA-Z0-9]+", ' ', k) for k in verify.split("\n")][0]
			if re.search(search_term, verify, re.IGNORECASE):
				is_reqistered = True
			elif re.search(alt_search_term, verify, re.IGNORECASE):
				is_reqistered = True
			elif re.search(search_term, alt_verify, re.IGNORECASE) or re.search(alt_search_term, alt_verify, re.IGNORECASE):
				is_reqistered = True
			else:
				is_reqistered = 'Usikkert'
			
			try:	#[try B]	
				check = driver.find_element(By.XPATH, '//*[@id="kp-wp-tab-overview"]/div[2]/div/div/div/div/div/div[5]/div/div/div')
				check_info = check.text
				if 'Add missing information' in check_info:
							has_info = False
				elif 'Legg til manglende informasjon' in check_info:
					has_info = False
				else:
					if is_reqistered:
						has_info = True
					else:
						has_info = False
				check_claimed = check.get_attribute('innerHTML')
				if 'cQhrTd' in check_claimed:
					is_claimed = True
				elif 'ndJ4N' in check_claimed:
					is_claimed = False
				else:
					if is_reqistered == False:
						is_claimed = False
					else:
						is_claimed = True

			except NoSuchElementException: 	#[try B]	
				has_info = True
				is_claimed = True

	except NoSuchElementException: 			#[try A]	
		is_reqistered = False
		try:		 #[try C]
			check = driver.find_element(By.XPATH, '//*[@id="kp-wp-tab-overview"]/div[2]/div/div/div/div/div/div[5]/div/div/div')
			check_info = check.text
			if 'Add missing information' in check_info:
						has_info = False
			elif 'Legg til manglende informasjon' in check_info:
				has_info = False
			else:
				if is_reqistered:
					has_info = True
				else:
					has_info = False
			check_claimed = check.get_attribute('innerHTML')
			if 'cQhrTd' in check_claimed:
				is_claimed = True
			elif 'ndJ4N' in check_claimed:
				is_claimed = False
			else:
				if is_reqistered == False:
					is_claimed = False
				else:
					is_claimed = True
		except NoSuchElementException: 		 #[try C]
			has_info = False
			is_claimed = False
	return np.array((org_num, search_term, is_reqistered, is_claimed, has_info), dtype = object)

def googleExtractor(**kwargs):
	'''
		sets up all nessasary functions, 
		then gets list of company names, 
		then iterates through the list via multithreading: claimedStatus().
	'''
	introPrint()
	testmode_kwarg = kwargs.get('testmode', None)
	file_name, chunksize, mode, tablename, start_limit, end_limit, input_array, long_break, short_break = getSettings(testmode_kwarg)
	nested_input_array = makeChunks(input_array, chunksize)
	infoPrint(nested_input_array, testmode_kwarg)
	
	'''! [tqdm ALT 1]'''
	# with tqdm(total = len(nested_input_array)) as pbar: 

	'''! [tqdm ALT 1]'''
	with tqdm(total = len(input_array)) as pbar:
		total_error_count = 0
		for chunk in nested_input_array:
			with ThreadPoolExecutor(max_workers=min(32, (os.cpu_count() or 1) + 4)) as executor:  
				futures = list(tqdm(executor.map(extractionManager, chunk), total = len(chunk)))
				result_list = []
				error_count = []
				for result in futures:
					''' Error handling '''
					if result != "CaptchaTriggered":
						(error_count.append(result) if None in result else result_list.append(result))
					else:
						executor.shutdown(wait=False)
						print("\n\n ERROR: shutdown was triggered!")
						error_count.append(result)
						for f in futures:
							if not f.done():
								f.cancel()
						break

				df = makeDataframe(result_list)
				print(df)
				databaseManager(df, tablename)
				
				'''! [tqdm ALT 1]'''
				# pbar.update(1) 

				'''! [tqdm ALT 2]'''
				pbar.update(chunksize) 

				total_error_count += len(error_count)
				if len(pbar) != len(input_array):
					time.sleep(long_break)
			
	print(f"error count: {total_error_count}")
	outroPrint()

if __name__ == '__main__':
	googleExtractor(testmode=True)
	# googleExtractor(testmode=False)

















#* BACKUPS WORKS REALLY WELL; googleExtractor(), extractionManager() 
""" 
def googleExtractor(**kwargs):
	'''
		sets up all nessasary functions, 
		then gets list of company names, 
		then iterates through the list via multithreading: claimedStatus().
	'''
	introPrint()
	testmode_kwarg = kwargs.get('testmode', None)
	file_name, chunksize, mode, tablename, start_limit, end_limit, input_array, long_break, short_break = getSettings(testmode_kwarg)
	nested_input_array = makeChunks(input_array, chunksize)
	infoPrint(nested_input_array, testmode_kwarg)
	
	'''! [tqdm ALT 1]'''
	# with tqdm(total = len(nested_input_array)) as pbar: 

	'''! [tqdm ALT 1]'''
	with tqdm(total = len(input_array)) as pbar:

		total_error_count = 0
		for chunk in nested_input_array:
			with concurrent.futures.ThreadPoolExecutor(max_workers=min(32, (os.cpu_count() or 1) + 4)) as executor:		
				results = list(tqdm(executor.map(extractionManager, chunk), total = len(chunk)))
				status_list = [status for status in results if status is not None]
				error_count = [status for status in results if status is 	 None]
				df = makeDataframe(status_list)
				print(df)
				databaseManager(df, tablename)
				
				'''! [tqdm ALT 1]'''
				# pbar.update(1) 

				'''! [tqdm ALT 2]'''
				pbar.update(chunksize) 

				total_error_count += len(error_count)
				if len(pbar) != len(input_array):
					time.sleep(long_break)
			
	print(f"error count: {total_error_count}")
	outroPrint()
"""

"""
def extractionManager(input_array):
	''' 
		import list 
		NB: remember to make sure it gets imported correctly 
		chunk = [] # consists of 500-1000 company names.
	'''
	org_num = input_array[0]
	search_term = input_array[1]

	base_url = "https://www.google.com/search?q=" 
	# print(f"{linkBuilder(base_url, search_term)}\n")
	driver = getDriver()
	driver.get(linkBuilder(base_url, search_term))
	mainWin = driver.current_window_handle  #* CATCHPA SOLVER
	

	try:	
		if driver.find_element(By.CLASS_NAME, "osrp-blk"):
			verify = driver.find_element(By.CLASS_NAME, "osrp-blk").text
			alt_search_term = search_term
			for ch in [' AS',' ASA', ' AB']:
				if ch in search_term:
					alt_search_term = search_term.replace(ch,"")
			alt_verify = [re.sub(r"[^a-zA-Z0-9]+", ' ', k) for k in verify.split("\n")][0]
			if re.search(search_term, verify, re.IGNORECASE):
				is_reqistered = True
			elif re.search(alt_search_term, verify, re.IGNORECASE):
				is_reqistered = True
			elif re.search(search_term, alt_verify, re.IGNORECASE) or re.search(alt_search_term, alt_verify, re.IGNORECASE):
				is_reqistered = True
			else:
				is_reqistered = 'Usikkert'
			try:
				check = driver.find_element(By.XPATH, '//*[@id="kp-wp-tab-overview"]/div[2]/div/div/div/div/div/div[5]/div/div/div')
				check_info = check.text
				if 'Add missing information' in check_info:
							has_info = False
				elif 'Legg til manglende informasjon' in check_info:
					has_info = False
				else:
					if is_reqistered:
						has_info = True
					else:
						has_info = False
				check_claimed = check.get_attribute('innerHTML')
				if 'cQhrTd' in check_claimed:
					is_claimed = True
				elif 'ndJ4N' in check_claimed:
					is_claimed = False
				else:
					if is_reqistered == False:
						is_claimed = False
					else:
						is_claimed = True

			except NoSuchElementException:
				has_info = True
				is_claimed = True
	except NoSuchElementException:
		is_reqistered = False
		try:
			check = driver.find_element(By.XPATH, '//*[@id="kp-wp-tab-overview"]/div[2]/div/div/div/div/div/div[5]/div/div/div')
			check_info = check.text
			if 'Add missing information' in check_info:
						has_info = False
			elif 'Legg til manglende informasjon' in check_info:
				has_info = False
			else:
				if is_reqistered:
					has_info = True
				else:
					has_info = False
			check_claimed = check.get_attribute('innerHTML')
			if 'cQhrTd' in check_claimed:
				is_claimed = True
			elif 'ndJ4N' in check_claimed:
				is_claimed = False
			else:
				if is_reqistered == False:
					is_claimed = False
				else:
					is_claimed = True
		except NoSuchElementException:
			has_info = False
			is_claimed = False
			
	return np.array((org_num, search_term, is_reqistered, is_claimed, has_info), dtype = object)
"""