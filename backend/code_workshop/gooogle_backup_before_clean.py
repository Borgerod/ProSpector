
import http
import time; START = time.perf_counter() #Since it also takes time to Import libs, I allways START the timer asap. 
from time import sleep
import re
import os
import csv
import numpy as np
import pandas as pd
import datetime as dt
from tqdm import tqdm
from random import uniform, randint
from concurrent.futures import ThreadPoolExecutor, as_completed
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



'''___ local imports __________
''' 
from file_manager import *
from postgres import databaseManager



''' * ____ CATCHPA SOLVER __________________________________________________________________________
'''
def write_stat(loops: int, time: int):
	with open('stat.csv', 'a', newline='') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',',
								quotechar='"', quoting=csv.QUOTE_MINIMAL)
		spamwriter.writerow([loops, time])  	 
	
def check_exists_by_xpath(xpath, driver) -> bool:
	''' #! NOTABLE CHANGE: added the "driver" param, if any future errrs should occour check here first. 
	'''
	try:
		driver.find_element_by_xpath(xpath)
	except NoSuchElementException:
		return False
	return True
	
def wait_between(a: float, b: float) -> None:
	rand = uniform(a, b) 
	sleep(rand)
 
def dimention(driver: webdriver) -> int: 
	'''
		dimention is 3 by default
	'''
	d = int(driver.find_element_by_xpath('//div[@id="rc-imageselect-target"]/table').get_attribute("class")[-1]);
	return d if d else 3
	
def catchpaSolver(driver: webdriver):
	mainWin = driver.current_window_handle  
	driver.switch_to_frame(driver.find_elements_by_tag_name("iframe")[0])

	'''  
		locate CheckBox  
	'''
	CheckBox = WebDriverWait(driver, 10).until(
			EC.presence_of_element_located((By.ID ,"recaptcha-anchor"))
			) 

	'''
		click CheckBox
	'''
	wait_between(0.5, 0.7)  
	CheckBox.click() 
	

	'''
		back to main window
	'''
	driver.switch_to_window(mainWin)  

	wait_between(2.0, 2.5) 
	'''
		switch to the second iframe by tag name
	'''
	driver.switch_to_frame(driver.find_elements_by_tag_name("iframe")[1])  
	i = 1
	while i < 130:
		print('\n\r{0}-th loop'.format(i))
		'''
			check if checkbox is checked at the 1st frame
		'''
		driver.switch_to_window(mainWin)   
		WebDriverWait(driver, 10).until(
			EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME , 'iframe'))
			)  
		wait_between(1.0, 2.0)
		'''
			saving results into stat file
		'''
		if check_exists_by_xpath('//span[@aria-checked="true"]', driver): 
			import winsound
			winsound.Beep(400,1500)
			write_stat(i, round(time()-START) - 1 )
			break 
			
		driver.switch_to_window(mainWin)   
		
		'''
			To the second frame to solve pictures
		'''
		wait_between(0.3, 1.5) 
		driver.switch_to_frame(driver.find_elements_by_tag_name("iframe")[1]) 
		solve_images(driver)
		i = i + 1
	
def solve_images(driver: webdriver): 
	'''
	 	main procedure to identify and submit picture solution
	'''	
	WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.ID ,"rc-imageselect-target"))
		) 		
	dim = dimention(driver)	

	'''
		check if there is a clicked tile
	'''
	if check_exists_by_xpath('//div[@id="rc-imageselect-target"]/table/tbody/tr/td[@class="rc-imageselect-tileselected"]', driver):
		rand2 = 0
	else:  
		rand2 = 1 	 

	''' 
		 wait before click on tiles, then clicks on a tile  
	'''
	wait_between(0.5, 1.0)
	tile1 = WebDriverWait(driver, 10).until(
		EC.element_to_be_clickable(
			(By.XPATH ,   '//div[@id="rc-imageselect-target"]/table/tbody/tr[{0}]/td[{1}]'.format(randint(1, dim), randint(1, dim )))
			) 
		)   
	tile1.click() 
	if (rand2):
		try:
			driver.find_element_by_xpath('//div[@id="rc-imageselect-target"]/table/tbody/tr[{0}]/td[{1}]'.format(randint(1, dim), randint(1, dim))).click()
		except NoSuchElementException:          		
			print('\n\r No Such Element Exception for finding 2nd tile')
	 
	'''
		 click on submit buttion 
	''' 
	driver.find_element_by_id("recaptcha-verify-button").click()

''' * ________________________________________________________________________________________________
'''

	
def getLongBreak()-> int: # takes a 5 minutes long_break between chunks
	return 300

def getShortBreak() -> int: # takes a 2 sec short_break between chunk items
	return 2

def driverOptions() -> webdriver.ChromeOptions:
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
	return options

def introPrint():
	print("_"*62)
	print("                  Starting: Google Extractor                ")
	print("_"*62)
	print()

def infoPrint(nested_input_array: list[np.ndarray], testmode_kwarg: str):
	'''
		prints useful information about the run and it's settings. Called by googleExtractor()
	'''
	_, chunksize, mode, tablename, start_limit, end_limit, input_array, long_break, short_break = getSettings(testmode_kwarg)
	print(f"Running: {mode}")
	print(f"Output_table used: {tablename}")
	print(f"Input_array starts from: [{start_limit}:{end_limit}]")
	print(f"Chunksize: {chunksize}")
	print(f"Input length: {len(input_array)}")
	print(f"Number of chunks: {len(nested_input_array)}")
	print(f"""Break procedure: 
	will take a long break between each chunk; [{str(dt.timedelta(seconds = long_break))}], 
	and a short break between every iteration; [{str(dt.timedelta(seconds = short_break))}]""")
	print("\n\n\n")

def outroPrint():
	print("_"*62)
	print("                   Data Extraction Complete.                 ")
	print(f"             Finished in {round(time.perf_counter() - START, 2)} second(s) | [{str(dt.timedelta(seconds = round(time.perf_counter() - START)))}]                ")
	print("_"*62)
	print()

def makeChunks(input_array: np.ndarray , chunksize: int) -> list[np.ndarray]:
	return [input_array[i:i + chunksize] for i in range(0, len(input_array), chunksize)]  

def linkBuilder(base_url: str, search_term: str) -> str:
	return base_url + search_term + ' maps'

def getDriver() -> webdriver:
	return webdriver.Chrome(options = driverOptions())

def checkGoogleAlarmTrigger(driver: webdriver) -> bool:
	html = driver.page_source
	return ('Systemene våre har oppdaget uvanlig trafikk' or 'unnusual traffic') in html

def makeDataframe(result_list: list) -> pd.DataFrame:
	return pd.DataFrame(result_list, columns = ['org_num', 'navn', 'google_profil', 'eier_bekreftet', 'komplett_profil', 'ringe_status'])

# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 

def prepDriver(base_url, search_term):
	driver = getDriver()
	# print(f"\n\n{self.base_url}, {self.search_term}\n\n")
	driver.get(linkBuilder(base_url, search_term))
	# driver = driver
	driver.current_window_handle  #* CATCHPA SOLVER
	time.sleep(getShortBreak())
	# self.driver = driver
	return driver

from threading import Thread  
class ThreadWithReturnValue(Thread):
	def __init__(self, group=None, target=None, name=None, args=(), kwargs={}, Verbose=None):
		Thread.__init__(self, group, target, name, args, kwargs)
		self._return = None

	def run(self):
		if self._target is not None:
			self._return = self._target(*self._args, **self._kwargs)

	def join(self, *args):
		Thread.join(self, *args)
		return self._return

class Extration(ThreadPoolExecutor):	
	def __init__(self, i):
		t = Thread(target=self.getData(i))
		t.start()
		org_num = self.org_num
		search_term = self.search_term
		driver = self.driver
		has_info = self.has_info
		is_claimed = self.is_claimed
		is_reqistered = self.is_reqistered
	# def __init__(self):
		
	# 	# self.org_num = None
	# 	# self.search_term = None
	# 	# # self.driver = None
	# 	# self.base_url = "https://www.google.com/search?q=" 
	# 	# self.has_info = False
	# 	# self.is_claimed = False
	# 	# self.is_reqistered = False
	# 	# self.call_status = False
	# 	org_num = self.org_num
	# 	search_term = self.search_term
	# 	driver = self.driver
	# 	has_info = self.has_info
	# 	is_claimed = self.is_claimed
	# 	is_reqistered = self.is_reqistered

	def getData(self, input_array: np.ndarray,) -> np.ndarray or str:
		''' 
			gets driver, builds url ,calls captcha solver, tries to find certain elements,
			finally returns array of bools or a error string
		'''
		# print(input_array)
		self.setOrgNumAndSearchTerm(input_array)
		# print(f"\n{self.org_num}, {self.search_term}\n")
		# driver = self.prepDriver()
		driver = prepDriver("https://www.google.com/search?q=" , self.search_term)
		# driver = prepDriver(self.base_url, self.search_term)
		# print(f"\n{self.org_num}, {self.search_term}\n")
		# print(driver)
		if checkGoogleAlarmTrigger(driver):
			self.alarmTriggerAction()
		else:
			self.driver = driver
			# self.extract(driver)
			try: 								#! [try A]
				self.tryVerification()
				try:							#? [try B] 
					# self.tryB()
					check = self.getOverview()
					self.checkHasInfo(check)
					self.checkClaimedStatus(check)
				except NoSuchElementException:  #? [try B]    
					self.has_info = True
					self.is_claimed = True
			
			except NoSuchElementException:      #! [try A]    
				self.is_reqistered = False
				try:							#* [try C]
					# self.tryC()
					check = self.getOverview()
					self.checkHasInfo(check)
					self.checkClaimedStatus(check)
				except NoSuchElementException:  #* [try C]
					self.has_info = False
					self.is_claimed = False	
			result_list = [self.org_num, self.search_term, self.is_reqistered, self.is_claimed, self.has_info, False]
			# return result_list
			df = makeDataframe([result_list])
			# print(df)
			# databaseManager(df, tablename = 'call_list_test', to_user_api = True)
			# return self.org_num, self.search_term, self.is_reqistered, self.is_claimed, self.has_info, False			
			# return np.array((self.org_num, self.search_term, self.is_reqistered, self.is_claimed, self.has_info, self.call_status), dtype = object) 
	
	def setOrgNumAndSearchTerm(self, input_array: np.ndarray) -> None:
		self.org_num = input_array[0]
		self.search_term = input_array[1]
		
		# print(input_array[0], input_array[1])
	

	# def setBaseUrl(self):
	# 	self.base_url =  
	# 	# return

	# def prepDriver(self):
	# 	driver = getDriver()
	# 	# print(f"\n\n{self.base_url}, {self.search_term}\n\n")
	# 	driver.get(linkBuilder(self.base_url, self.search_term))
	# 	driver = driver
	# 	driver.current_window_handle  #* CATCHPA SOLVER
	# 	time.sleep(getShortBreak())
	# 	# self.driver = driver
	# 	return driver
	
	def alarmTriggerAction(self):
		self.is_reqistered, self.is_claimed, self.has_info, = "CaptchaTriggered", "CaptchaTriggered", "CaptchaTriggered"

	def tryVerification(self) -> None:
		'''
			Tries to verify if company is registered, with multiple search variations. 
			=> sets self.is_reqistered
		'''
		if self.getVerify():
			verify = self.getVerify()
			alt_verify = self.getAltVerify(verify)
			alt_search_term = self.getAltSearchTerms()
			self.checkRegistered(verify, alt_verify, alt_search_term)
	
	def getAltSearchTerms(self):
		alt_search_term = self.search_term
		for ch in [' AS',' ASA', ' AB']:
			if ch in alt_search_term:
				alt_search_term = alt_search_term.replace(ch,"")
		return alt_search_term
	
	def getAltVerify(self, verify):
		return [re.sub(r"[^a-zA-Z0-9]+", ' ', k) for k in verify.split("\n")][0]
	
	def getVerify(self):
		return self.driver.find_element(By.CLASS_NAME, "osrp-blk").text
		# return self.driver.find_element(By.CLASS_NAME, "osrp-blk").text

				
	def checkRegistered(self, verify, alt_verify, alt_search_term):
		if re.search(self.search_term, verify, re.IGNORECASE):
			self.is_reqistered = True
		elif re.search(alt_search_term, verify, re.IGNORECASE):
			self.is_reqistered = True
		elif re.search(self.search_term, alt_verify, re.IGNORECASE) or re.search(alt_search_term, alt_verify, re.IGNORECASE):
			self.is_reqistered = True
		else:
			self.is_reqistered = 'Usikkert'			

	def checkHasInfo(self, check) -> None:
		'''
			=> sets self.has_info
		'''
		check_info = check.text
		if 'Add missing information' in check_info or 'Legg til manglende informasjon' in check_info:
			self.has_info = False
		elif self.is_reqistered:
			self.has_info = True
		else:
			self.has_info = False

	def checkClaimedStatus(self, check):
		'''
			=> sets self.is_claimed
		'''
		check_claimed = check.get_attribute('innerHTML')
		if 'cQhrTd' in check_claimed or 'ndJ4N' in check_claimed:
			self.is_claimed = True
		elif self.is_reqistered:
			self.is_claimed = True
		else:
			self.is_claimed = False

	def getOverview(self, ) -> any:
		return self.driver.find_element(By.XPATH, '//*[@id="kp-wp-tab-overview"]/div[2]/div/div/div/div/div/div[5]/div/div/div')



# TODO [ ] Turn settings into class
def getSettings(kwargs) -> list: 
	file_name = 'google'
	chunksize = parseSettings(file_name)['chunk_size']
	input_array = fetchData('google_input_table').to_numpy()
	if kwargs: #! [OLD] if kwargs.get('testmode', None):
		mode = 'Test Mode'
		tablename = 'call_list_test'
		start_limit, end_limit = 330, 450
		input_array = input_array[start_limit : end_limit]
	else:
		mode = 'Publish Mode'
		tablename = 'call_list'
		start_limit, end_limit = 7099, None 
		# start_limit, end_limit = None, None 				
		input_array = input_array[start_limit : end_limit]

	long_break, short_break = getLongBreak(), getShortBreak()	
	return file_name, chunksize, mode, tablename, start_limit, end_limit, input_array, long_break, short_break


def googleExtractor(**kwargs: str):
	'''
		runs setup, then gets array of company names, then iterates through the list via ThreadPoolExecutor: extractionManager()
		stops process if Captcha is triggered, finally sends a df of results to database.
	'''
	introPrint()
	testmode_kwarg = kwargs.get('testmode', None)
	_, chunksize, _, tablename, _, _, input_array, long_break, _= getSettings(testmode_kwarg)

	nested_input_array = makeChunks(input_array, chunksize)
	infoPrint(nested_input_array, testmode_kwarg)

	# E = Extration()

	# for chunk in nested_input_array:
	# 	with tqdm(total = len(nested_input_array)) as pbar1: 
	# 		with tqdm(total = len(input_array)) as pbar2:
	# 			total_error_count = 0
	# 			with ThreadPoolExecutor(max_workers=min(32, (os.cpu_count() or 1) + 4)) as executor: 
	# 				with tqdm(total = len(chunk)) as pbar3:
	# 					# futures = [executor.submit(extractionManager, i) for i in chunk]
	# 					futures = [executor.submit(E.getData, i) for i in chunk]
	# 					# result_list = []
	# 					# error_count = []
	# 					for future in as_completed(futures):
	# 						pbar3.update(1)  
	# 						# result = future.result()
	# 						# (error_count.append(result) if None in result else result_list.append(result))					
	# 					pbar1.update(1)
	# 					pbar2.update(chunksize) 					

	# 	# df = makeDataframe(result_list)
	# 	# print(f"\n{df}")



	with tqdm(total = len(nested_input_array)) as pbar1: 
		with tqdm(total = len(input_array)) as pbar2:
			with ThreadPoolExecutor(max_workers=min(32, (os.cpu_count() or 1) + 4)) as executor: 
				for chunk in nested_input_array:
					futures = list(tqdm(executor.map(Extration, chunk), total=len(chunk)))
					# list(tqdm(executor.map(Extration, chunk), total=len(chunk)))
					pbar2.update(chunksize) 	
					pbar1.update(1)

	# with tqdm(total = len(nested_input_array)) as pbar1: 
	# 	with ThreadPoolExecutor(max_workers=min(32, (os.cpu_count() or 1) + 4)) as executor: 
	# 		for chunk in nested_input_array:
	# 			futures = list(tqdm(executor.map(Extration, chunk), total=len(chunk)))
	# 			pbar1.update(1)

		if len(pbar1) != len(nested_input_array):
			time.sleep(long_break)
	outroPrint()

if __name__ == '__main__':
	googleExtractor(testmode = True)
	# googleExtractor(testmode = False)













''' TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP  TEMP TEMP TEMP TEMP TEMP TEMP TEMP  TEMP TEMP TEMP TEMP TEMP TEMP TEMP  TEMP TEMP TEMP TEMP TEMP TEMP TEMP '''
'''							
*							_____ WHERE I LEFT OF _____
-						[--.--.----]

!						__ISSUE:___
- 						captchaTrigger does not break the whole process properly. 

*						_____ EXTRACTION RECORD _______
-						Skraper 200 enheter --> 	   77.52 second(s) (after changes) | => (1000 enheter) : 00:06:27 | [0.388 s/enh]
-						Skraper 600 enheter -->  	  165.02 second(s)				   | => (1000 enheter) : 00:04:35 | [0.275 s/enh]
												[old] 232.41 second(s)
												[old] 334.99 second(s)

*						_____ ESTIMATIONS _______
*						Estimated length of google_input_list (output_list): 	10.000 rows / [10000]
*						Estimated total extraction time: 						[01:04:36] / 64.6 minutes

! 						LIMIT FOR CaptchaTrigger is: 700 units
						TODO [ ] should increase break_time or repace break procedure to make a big break before 700 units 

						TODO [ ] figure out how long the "cool down" time is after google captcha has been triggered
						TODO [ ] figure out optinal breaktime for not triggerring google captcha


'''
''' TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP  TEMP TEMP TEMP TEMP TEMP TEMP TEMP  TEMP TEMP TEMP TEMP TEMP TEMP TEMP  TEMP TEMP TEMP TEMP TEMP TEMP TEMP '''


#! _____________________________________ OLD EXTRACTION MANAGER ________________________________________________________________________________________________

# def extractionManager(input_array: np.ndarray) -> np.ndarray or str :
	# ''' 
	# 	gets driver, builds url ,calls captcha solver, tries to find certain elements,
	# 	finally returns array of bools or a error string
	# '''
	# org_num = input_array[0]
	# search_term = input_array[1]

	# base_url = "https://www.google.com/search?q=" 
	# driver = getDriver()
	# driver.get(linkBuilder(base_url, search_term))
	# driver.current_window_handle  #* CATCHPA SOLVER
	# time.sleep(getShortBreak())
	

	# # TODO [ ] Clean this awfull mess of a if-try-tree
	# if checkGoogleAlarmTrigger(driver):
	# 	is_reqistered, is_claimed, has_info, = "CaptchaTriggered", "CaptchaTriggered", "CaptchaTriggered"
	# 	call_status = False
	# 	return np.array((org_num, search_term, is_reqistered, is_claimed, has_info, call_status), dtype = object)
	# else:
	# 	try:			 #[try A]	
	# 		if driver.find_element(By.CLASS_NAME, "osrp-blk"):
	# 			verify = driver.find_element(By.CLASS_NAME, "osrp-blk").text
	# 			alt_search_term = search_term
	# 			for ch in [' AS',' ASA', ' AB']:
	# 				if ch in search_term:
	# 					alt_search_term = search_term.replace(ch,"")
	# 			alt_verify = [re.sub(r"[^a-zA-Z0-9]+", ' ', k) for k in verify.split("\n")][0]
	# 			try: 
	# 				if re.search(search_term, verify, re.IGNORECASE):
	# 					is_reqistered = True
	# 				elif re.search(alt_search_term, verify, re.IGNORECASE):
	# 					is_reqistered = True
	# 				elif re.search(search_term, alt_verify, re.IGNORECASE) or re.search(alt_search_term, alt_verify, re.IGNORECASE):
	# 					is_reqistered = True
	# 				else:
	# 					is_reqistered = 'Usikkert'
	# 			except:
	# 				print(f"ERROR with: {search_term}")

				
	# 			try:	#[try B]	
	# 				check = driver.find_element(By.XPATH, '//*[@id="kp-wp-tab-overview"]/div[2]/div/div/div/div/div/div[5]/div/div/div')
	# 				check_info = check.text
	# 				if 'Add missing information' in check_info:
	# 							has_info = False
	# 				elif 'Legg til manglende informasjon' in check_info:
	# 					has_info = False
	# 				else:
	# 					if is_reqistered:
	# 						has_info = True
	# 					else:
	# 						has_info = False
	# 				check_claimed = check.get_attribute('innerHTML')
	# 				if 'cQhrTd' in check_claimed:
	# 					is_claimed = True
	# 				elif 'ndJ4N' in check_claimed:
	# 					is_claimed = False
	# 				else:
	# 					if is_reqistered == False:
	# 						is_claimed = False
	# 					else:
	# 						is_claimed = True

	# 			except NoSuchElementException: 	#[try B]	
	# 				has_info = True
	# 				is_claimed = True

	# 	except NoSuchElementException: 			#[try A]	
	# 		is_reqistered = False
	# 		try:		 #[try C]
	# 			check = driver.find_element(By.XPATH, '//*[@id="kp-wp-tab-overview"]/div[2]/div/div/div/div/div/div[5]/div/div/div')
	# 			check_info = check.text
	# 			if 'Add missing information' in check_info:
	# 						has_info = False
	# 			elif 'Legg til manglende informasjon' in check_info:
	# 				has_info = False
	# 			else:
	# 				if is_reqistered:
	# 					has_info = True
	# 				else:
	# 					has_info = False
	# 			check_claimed = check.get_attribute('innerHTML')
	# 			if 'cQhrTd' in check_claimed:
	# 				is_claimed = True
	# 			elif 'ndJ4N' in check_claimed:
	# 				is_claimed = False
	# 			else:
	# 				if is_reqistered == False:
	# 					is_claimed = False
	# 				else:
	# 					is_claimed = True
	# 		except NoSuchElementException: 		 #[try C]
	# 			has_info = False
	# 			is_claimed = False
	# 	call_status = False
	# 	return np.array((org_num, search_term, is_reqistered, is_claimed, has_info, call_status), dtype = object)
#! _____________________________________________________________________________________________________________________________________




















# class Extration:	
# 	def __init__(self, input_array: np.ndarray,):
# 		self.org_num = input_array[0]
# 		self.search_term = input_array[1]
# 		self.driver = self.prepDriver()
# 		self.base_url = self.getBaseUrl()
# 		self.has_info = False
# 		self.is_claimed = False
# 		self.is_reqistered = False
# 		self.call_status = False

# 	def getBaseUrl(self):
# 		return "https://www.google.com/search?q=" 

# 	def prepDriver(self):
# 		driver = getDriver()
# 		driver.get(linkBuilder(self.getBaseUrl(), self.search_term))
# 		driver.current_window_handle  #* CATCHPA SOLVER
# 		time.sleep(getShortBreak())
# 		return driver
	
# 	# def setOrgNumAndSearchTerm(self, input_array):
# 	# 	self.org_num = input_array[0]
# 	# 	self.search_term = input_array[1]



# 	def alarmTriggerAction(self):
# 		self.is_reqistered, self.is_claimed, self.has_info, = "CaptchaTriggered", "CaptchaTriggered", "CaptchaTriggered"
# 		# return np.array((self.org_num, self.search_term, self.is_reqistered, self.is_claimed, self.has_info, self.call_status), dtype = object)

# 	# def extract(self, driver):
# 	# 	'''
# 	# 	Try A
# 	# 	'''
# 	# 	try: 								#! [try A]
# 	# 		self.tryA()
# 	# 		try:							#? [try B] 
# 	# 			self.tryB()
# 	# 		except NoSuchElementException:  #? [try B]    
# 	# 			self.has_info = True
# 	# 			self.is_claimed = True
		
# 	# 	except NoSuchElementException:      #! [try A]    
# 	# 		self.is_reqistered = False
# 	# 		try:							#* [try C]
# 	# 			self.tryC()
# 	# 		except NoSuchElementException:  #* [try C]
# 	# 			self.has_info = False
# 	# 			self.is_claimed = False	
# 	# 	return np.array((self.org_num, self.search_term, self.is_reqistered, self.is_claimed, self.has_info, self.call_status), dtype = object) 


# 	def tryVerification(self) -> None:
# 		# if self.driver.find_element(By.CLASS_NAME, "osrp-blk"):
# 		'''
# 			Tries to verify if company is registered, with multiple search variations. 
# 			=> sets self.is_reqistered
# 		'''
# 		if self.getVerify():
# 			verify = self.getVerify()
# 			alt_verify = self.getAltVerify(verify)
# 			alt_search_term = self.getAltSearchTerms()
# 			self.checkRegistered(verify, alt_verify, alt_search_term)
	
# 	# def tryB(self,) -> None:
# 	# 	check = self.getOverview()
# 	# 	self.checkHasInfo(check)
# 	# 	self.checkClaimedStatus(check)
	
# 	# def tryC(self,) -> None:
# 	# 	check = self.getOverview()
# 	# 	self.checkHasInfo(check)
# 	# 	self.checkClaimedStatus(check)

# 	def getAltSearchTerms(self):
# 		alt_search_term = self.search_term
# 		for ch in [' AS',' ASA', ' AB']:
# 			if ch in alt_search_term:
# 				alt_search_term = alt_search_term.replace(ch,"")
# 		return alt_search_term
	
# 	def getAltVerify(self, verify):
# 		return [re.sub(r"[^a-zA-Z0-9]+", ' ', k) for k in verify.split("\n")][0]
	
# 	def getVerify(self):
# 		return self.driver.find_element(By.CLASS_NAME, "osrp-blk").text

				
# 	def checkRegistered(self, verify, alt_verify, alt_search_term):
# 		if re.search(self.search_term, verify, re.IGNORECASE):
# 			self.is_reqistered = True
# 		elif re.search(alt_search_term, verify, re.IGNORECASE):
# 			self.is_reqistered = True
# 		elif re.search(self.search_term, alt_verify, re.IGNORECASE) or re.search(alt_search_term, alt_verify, re.IGNORECASE):
# 			self.is_reqistered = True
# 		else:
# 			self.is_reqistered = 'Usikkert'			

# 	def checkHasInfo(self, check) -> None:
# 		'''
# 			=> sets self.has_info
# 		'''
# 		check_info = check.text
# 		if 'Add missing information' in check_info or 'Legg til manglende informasjon' in check_info:
# 			self.has_info = False
# 		elif self.is_reqistered:
# 			self.has_info = True
# 		else:
# 			self.has_info = False

# 	def checkClaimedStatus(self, check):
# 		'''
# 			=> sets self.is_claimed
# 		'''
# 		check_claimed = check.get_attribute('innerHTML')
# 		if 'cQhrTd' in check_claimed or 'ndJ4N' in check_claimed:
# 			self.is_claimed = True
# 		elif self.is_reqistered:
# 			self.is_claimed = True
# 		else:
# 			self.is_claimed = False

# 	def getOverview(self, ) -> any:
# 		return self.driver.find_element(By.XPATH, '//*[@id="kp-wp-tab-overview"]/div[2]/div/div/div/div/div/div[5]/div/div/div')
	
# 	def getData(self, input_array: np.ndarray,) -> np.ndarray or str:
# 		''' 
# 			gets driver, builds url ,calls captcha solver, tries to find certain elements,
# 			finally returns array of bools or a error string
# 		'''
# 		driver = self.prepDriver()
# 		if checkGoogleAlarmTrigger(driver):
# 			self.alarmTriggerAction()
# 		else:
# 			# self.extract(driver)
# 			try: 								#! [try A]
# 				self.tryVerification()
# 				try:							#? [try B] 
# 					# self.tryB()
# 					check = self.getOverview()
# 					self.checkHasInfo(check)
# 					self.checkClaimedStatus(check)
# 				except NoSuchElementException:  #? [try B]    
# 					self.has_info = True
# 					self.is_claimed = True
			
# 			except NoSuchElementException:      #! [try A]    
# 				self.is_reqistered = False
# 				try:							#* [try C]
# 					# self.tryC()
# 					check = self.getOverview()
# 					self.checkHasInfo(check)
# 					self.checkClaimedStatus(check)
# 				except NoSuchElementException:  #* [try C]
# 					self.has_info = False
# 					self.is_claimed = False	
# 		return np.array((self.org_num, self.search_term, self.is_reqistered, self.is_claimed, self.has_info, self.call_status), dtype = object) 
	
