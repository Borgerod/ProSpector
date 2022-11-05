# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from fake_useragent import UserAgent
# import time 
# options = Options()
# ua = UserAgent()
# userAgent = ua.random
# print(userAgent)
# options.add_argument(f'user-agent={userAgent}')
# driver = webdriver.Chrome(chrome_options=options, executable_path=r'chromedriver.exe')
# # driver.get("https://www.google.co.in")
# # search.send_keys(search_term+' maps')
# # search.send_keys(Keys.RETURN)
# # driver.get('https://www.google.com/search?q=SMED+TJELLE+AS+maps')
# # time.sleep(10)
# # driver.quit()

# driver.get("https://accounts.google.com/signin/v2/identifier?hl=en&passive=true&continue=https%3A%2F%2Fwww.google.com%2F%3Fgws_rd%3Dssl&ec=GAZAmgQ&flowName=GlifWebSignIn&flowEntry=ServiceLogin");
# # WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@title='reCAPTCHA']")))

# time.sleep(1)
# search = driver.find_element("name", "identifier")
# search.send_keys("mr.borgerood@hotmail.com")
# time.sleep(1)
# button = driver.find_element(By.XPATH, "//span[@jsname = 'bN97Pc']")
# button.click()
# time.sleep(2)


# # driver.findElement(By.name("email")).sendKeys("mr.borgerood@hotmail.com"+Keys.ENTER);
# # time.sleep(2)
# driver.findElement(By.name("password")).send_keys("Orikkel1991"+Keys.ENTER)
# time.sleep(2)

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
import pickle 



# ___ local imports __________
from config import payload, tablenames, settings
from postgres import databaseManager, getInputTable
from file_manager import *
from input_table import inputTable



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
	




# ***** main procedure to identify and submit picture solution	
def solve_images(driver):	
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

def getDriver():
	''' gets chrome driver '''
	return webdriver.Chrome(options = driverOptions())




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

def makeChunks(input_array, chunksize):
	''' 
		used by proffExtractor, divides input array into chunks 
	'''
	return [input_array[i:i+chunksize] for i in range(0, len(input_array), chunksize)]  


def linkBuilder(base_url, search_term):
	return base_url+search_term+' maps'

def extractionManager(input_array):
	''' 
		import list 
		NB: remember to make sure it gets imported correctly 
		chunk = [] # consists of 500-1000 company names.
	'''
	org_num = input_array[0]
	search_term = input_array[1]

	# start = time()	 
	# url='https://www.google.com/search?q=FAGMØBLER HERMAN ANDERSEN AS maps'
	# driver = getDriver()
	# driver.get(url)

	base_url = "https://www.google.com/search?q=" 
	driver = getDriver()
	driver.get(linkBuilder(base_url, search_term))
	mainWin = driver.current_window_handle  
	try:	
		if driver.find_element(By.CLASS_NAME, "osrp-blk"):
			verify = driver.find_element(By.CLASS_NAME, "osrp-blk").text
			alt_search_term = search_term
			for ch in [' AS',' ASA', ' AB']:
				if ch in search_term:
					alt_search_term = search_term.replace(ch,"")
			if re.search(search_term, verify, re.IGNORECASE):
				is_reqistered = True
			elif re.search(alt_search_term, verify, re.IGNORECASE):
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
					is_claimed = False
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
				if is_reqistered:
					is_claimed = True
				else:
					is_claimed = False
		except NoSuchElementException:
			has_info = False
			is_claimed = False
	return np.array((org_num, search_term, is_reqistered, is_claimed, has_info), dtype = object)

def makeDataframe(status_list):
	''' makes dataframe from json '''
	df = pd.DataFrame(status_list, columns = ['org_num', 'navn', 'google_profil', 'eier_erklært', 'komplett_profil'])
	return df


def getSettings(kwargs):
	''' 
		Prepwork; fetches config-data & propriate input 
	'''
	file_name = 'google'
	chunksize = parseSettings(file_name)['chunk_size']
	# ! input_array = (getInputTable(file_name))[['org_num', 'navn']].to_numpy() #![ORIGINAL] temporary disabled B/C input_table might be corrupt by faulty versions
	input_array = fetchData('google_input_table').to_numpy()
	''' 
		making adjustments to settings based on **kawrg: "testmode" 
	'''
	if kwargs: # if kwargs.get('testmode', None):
		mode = 'Test Mode'
		tablename = 'test_output_table' #? [ALT] tablename = parseTablenames('1881', testmode = True)
		start_limit, end_limit = None, 20
		input_array = input_array[start_limit : end_limit]
	else:
		mode = 'Publish Mode' #? [ALT]: mode = 'Final Mode'
		tablename = 'output_table' #? [ALT] tablename = parseTablenames('1881', testmode = False)
		start_limit, end_limit = None, None 				#TEMP while testing 
		input_array = input_array[start_limit : end_limit]	
	return file_name, chunksize, mode, tablename, start_limit, end_limit, input_array

def printSettingsInfo(nested_input_array, testmode_kwarg):
	file_name, chunksize, mode, tablename, start_limit, end_limit, input_array = getSettings(testmode_kwarg)
	print(f"Running: {mode}")
	print(f"output_table used: {tablename}")
	print(f"Input_array starts from: [{start_limit}:{end_limit}]")
	print(f"chunksize: {chunksize}")
	print(f"input length: {len(input_array)}")
	print(f"number of chunks: {len(nested_input_array)}")
	print("\n\n\n")

# * ORIGINAL - disabled while testing
def googleExtractor(**kwargs):
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

	# ''' fetching data from config '''
	# file_name = getFileName()	# fetches name of current file 
	# tablename = parseTablenames(file_name) # fetches the appropriate tablename for current file
	# settings = parseSettings(file_name)	# fetches the appropriate settings for current file
	# chunksize = settings['chunk_size']
	# # input_array = fetchData('output_table').to_numpy()
	
	testmode_kwarg = kwargs.get('testmode', None)
	file_name, chunksize, mode, tablename, start_limit, end_limit, input_array = getSettings(testmode_kwarg)
	nested_input_array = makeChunks(input_array, chunksize) # divides input_array into chunks 
	printSettingsInfo(nested_input_array, testmode_kwarg)

	# print(f'full input_array: {len(input_array)}')
	
	# nested_input_array = makeChunks(input_array, chunksize)
	# print(f'current run uses {len(nested_input_array)}')
	# print(f'current run uses {len(nested_input_array[0])}')
	# print(f'example; first element in the first chunk: {nested_input_array[0][0]}')
	print(f'number of workers in use {min(32, (os.cpu_count() or 1) + 4)}')

	# for chunk in nested_input_array:
		# results = extractionManager(chunk)

	# with tqdm(total = len(nested_input_array)) as pbar:
	# 	for chunk in nested_input_array:
	# 		# with concurrent.futures.ThreadPoolExecutor() as executor:
	# 		with concurrent.futures.ThreadPoolExecutor(max_workers=min(32, (os.cpu_count() or 1) + 4)) as executor:
	# 				results = executor.map(extractionManager, chunk)
	# 				for df in results:
	# 					if df is None:
	# 						pass
	# 					else:
	# 						print(df)
	# 						# databaseManager(df, tablename)
	# 		pbar.update(1)
	


	with tqdm(total = len(nested_input_array)) as pbar: 
		for chunk in nested_input_array:
			with concurrent.futures.ThreadPoolExecutor(max_workers=min(32, (os.cpu_count() or 1) + 4)) as executor:
				results = executor.map(extractionManager, chunk)
				results = list(tqdm(executor.map(extractionManager, chunk), total = len(chunk)))
				status_list = [status for status in results if status is not None]	
				df = makeDataframe(status_list)
				print(df)
				databaseManager(df, tablename)
				pbar.update(1)


	print("_"*62)
	print("                   Data Extraction Complete.                 ")
	print(f"                  Finished in {round(time.perf_counter() - start, 2)} second(s)                 ")
	print("_"*62)
	print()

if __name__ == '__main__':
	googleExtractor(testmode=True)
	# googleExtractor(testmode=False)
