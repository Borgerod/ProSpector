
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
from concurrent.futures import ThreadPoolExecutor
from threading import Thread  
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
	d = int(driver.find_element_by_xpath('//div[@id="rc-imageselect-target"]/table').get_attribute("class")[-1])
	# d = int(driver.find_element_by_xpath('//div[@id="rc-imageselect-target"]/table').get_attribute("class")[-1]); #! Litt usikker på hvorfor den hadde";" endret men ikke fjernet
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

def makeChunks(input_array: np.ndarray , chunksize: int) -> list[np.ndarray]:
	return [input_array[i:i + chunksize] for i in range(0, len(input_array), chunksize)]  

def makeDataframe(result_list: list) -> pd.DataFrame:
	return pd.DataFrame(result_list, columns = ['org_num', 'navn', 'google_profil', 'eier_bekreftet', 'komplett_profil', 'ringe_status'])

class Print:
	def intro(self):
		print("_"*62)
		print("                  Starting: Google Extractor                ")
		print("_"*62)
		print()
	
	def info(self, len_nested_input: int):
		'''
		prints useful information about the run and it's settings. Called by googleExtractor()
		'''
		_, chunksize, mode, tablename, start_limit, end_limit, _, long_break, short_break = S.getSettings
		print(f"Running: {mode}")
		print(f"Output_table used: {tablename}")
		print(f"Input_array starts from: [{start_limit}:{end_limit}]")
		print(f"Chunksize: {chunksize}")
		print(f"Input length: {S.getInputArrayLength}")
		print(f"Number of chunks: {len_nested_input}")
		print(f"""Break procedure: 
		will take a long break between each chunk; [{str(dt.timedelta(seconds = long_break))}], 
		and a short break between every iteration; [{str(dt.timedelta(seconds = short_break))}]""")
		print("\n\n\n")
	
	def outro(self):
		print("_"*62)
		print("                   Data Extraction Complete.                 ")
		print(f"             Finished in {round(time.perf_counter() - START, 2)} second(s) | [{str(dt.timedelta(seconds = round(time.perf_counter() - START)))}]                ")
		print("_"*62)
		print()

class Driver:

	def getDriver(self) -> webdriver:
		return webdriver.Chrome(options = self.getDriverOptions)

	def linkBuilder(self, base_url: str, search_term: str) -> str:
		return base_url + search_term + ' maps'

	def prepDriver(self, base_url, search_term):
		driver = self.getDriver()
		driver.get(self.linkBuilder(base_url, search_term))
		driver.current_window_handle  #* CATCHPA SOLVER
		time.sleep(S.getShortBreak)
		return driver

	@property
	def getDriverOptions(self) -> webdriver.ChromeOptions:
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

class ThreadWithReturnValue(Thread):
	def __init__(self, group=None, target=None, name=None, args=(), kwargs={}):
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
		# _________________________________
		self.verify = None
		self.alt_verify = None
		self.search_term = search_term
		self.verify = None
		self.alt_verify = None
		self.alt_search_term = None
		self.check = None
		# _________________________________
		self.is_reqistered = False

	def getData(self, input_array: np.ndarray) -> np.ndarray or str:
		''' 
			gets driver, builds url ,calls captcha solver, tries to find certain elements,
			finally returns array of bools or a error string
		'''
		self.setOrgNumAndSearchTerm(input_array)
		driver = Driver.prepDriver("https://www.google.com/search?q=" , self.search_term)
		if self.checkGoogleAlarmTrigger(driver):
			self.alarmTriggerAction()
		else:
			self.driver = driver
			try:								#! [try A]
				if self.setVerify():							
				# if self.vertify:
					self.checkRegistered()								
					# self.tryVerification()
				try:							#? [try B] 
					self.setOverview()
					self.checkHasInfo(self.check)
					self.checkClaimedStatus(self.check)
				except NoSuchElementException:  #? [try B]    
					self.has_info = True
					self.is_claimed = True
			
			except NoSuchElementException:      #! [try A]    
				self.is_reqistered = False
				try:							#* [try C]
					self.setOverview()
					self.checkHasInfo(self.check)
					self.checkClaimedStatus(self.check)
				except NoSuchElementException:  #* [try C]
					self.has_info = False
					self.is_claimed = False	
			result_list = [self.org_num, self.search_term, self.is_reqistered, self.is_claimed, self.has_info, False]
			df = makeDataframe([result_list])
			print(df)
			# databaseManager(df, Settings().getTablename, to_user_api=True)

	def setTableName(self, tablename):
		self.tablename = tablename
		
	def setOrgNumAndSearchTerm(self, input_array: np.ndarray) -> None:
		self.org_num = input_array[0]
		self.search_term = input_array[1]
	
	def setVerify(self):
		self.verify = self.driver.find_element(By.CLASS_NAME, "osrp-blk").text

	def setOverview(self, ) -> any:
		self.check =  self.driver.find_element(By.XPATH, '//*[@id="kp-wp-tab-overview"]/div[2]/div/div/div/div/div/div[5]/div/div/div')



	# def setAltSearchTerms(self):
	# 	self.alt_search_term = [self.search_term.replace(ch,"") for ch in [' AS',' ASA', ' AB'] if ch in self.search_term]
		# for ch in [' AS',' ASA', ' AB']:
		# 	if ch in self.search_term:
		# 		self.alt_search_term = self.search_term.replace(ch,"")

	# def setAltVerify(self):
	# 	self.alt_verify = [re.sub(r"[^a-zA-Z0-9]+", ' ', k) for k in self.verify.split("\n")][0]


	def alarmTriggerAction(self):
		self.is_reqistered, self.is_claimed, self.has_info, = "CaptchaTriggered", "CaptchaTriggered", "CaptchaTriggered"

	# def tryVerification(self) -> None:
	# 	'''
	# 		Tries to verify if company is registered, with multiple search variations. 
	# 		=> sets self.is_reqistered
	# 	'''
	# 	if self.getVerify():
	# 		verify = self.getVerify()
	# 		self.checkRegistered(verify, self.getAltVerify(verify), self.getAltSearchTerms())
	
	# def getAltSearchTerms(self):
	# 	alt_search_term = self.search_term
	# 	for ch in [' AS',' ASA', ' AB']:
	# 		if ch in alt_search_term:
	# 			alt_search_term = alt_search_term.replace(ch,"")
	# 	return alt_search_term
	
	# def getAltVerify(self, verify):
	# 	return [re.sub(r"[^a-zA-Z0-9]+", ' ', k) for k in verify.split("\n")][0]

	# def getVerify(self):
	# 	return self.driver.find_element(By.CLASS_NAME, "osrp-blk").text

	def setAltVerify(self):
		self.alt_verify = [re.sub(r"[^a-zA-Z0-9]+", ' ', k) for k in self.verify.split("\n")][0]
	
	def setAltSearchTerms(self):
		for ch in [' AS',' ASA', ' AB']:
			if ch in self.search_term:
				self.alt_search_term = self.search_term.replace(ch,"")

	def getLowerCaseList(self):
		return [
				list(map(str.lower, [self.verify, self.alt_verify])), 
				list(map(str.lower, [self.search_term, self.alt_search_term]))
				]

	def checkRegistered(self):
		self.is_reqistered = (True if any(x in self.getLowerCaseList()[0] for x in self.getLowerCaseList()[1]) else False)		
	
	# def checkRegistered(self):
	# 	verifications =[self.verify, self.alt_verify]
	# 	search_terms = [self.search_term, self.alt_search_term]

	# 	if re.search(search_terms, verifications, re.IGNORECASE):
	# 		self.is_reqistered = True
	# 	else:
	# 		self.is_reqistered = 'Usikkert'

		# if re.search(self.search_term, self.verify, re.IGNORECASE):
		# 	self.is_reqistered = True
		# elif re.search(self.alt_search_term, self.verify, re.IGNORECASE):
		# 	self.is_reqistered = True
		# elif re.search(self.search_term, self.alt_verify, re.IGNORECASE) or re.search(self.alt_search_term, self.alt_verify, re.IGNORECASE):
		# 	self.is_reqistered = True
		# else:
		# 	self.is_reqistered = 'Usikkert'

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

	# def getOverview(self, ) -> any:
	# 	return self.driver.find_element(By.XPATH, '//*[@id="kp-wp-tab-overview"]/div[2]/div/div/div/div/div/div[5]/div/div/div')


	def checkGoogleAlarmTrigger(self, driver: webdriver) -> bool:
		html = driver.page_source
		return ('Systemene våre har oppdaget uvanlig trafikk' or 'unnusual traffic') in html

class Settings:
	def __init__(self):
		self.mode = None
		self.tablename = None
		self.start_limit = None
		self.end_limit = None
		self.file_name = 'google'
		self.chunksize = parseSettings(self.file_name)['chunk_size']
		self.long_break = self.getLongBreak
		self.short_break = self.getShortBreak
		self.input_array = None
		self.len_input_array = None
	
	def setSettings(self, **kwargs):
		if kwargs.get('testmode', None):
			print("HAS KWARGS")
			self.mode = 'Test Mode'
			self.tablename = 'call_list_test'
			self.start_limit, self.end_limit = 330, 335
		else:
			print("HAS NO KWARGS")
			self.mode = 'Publish Mode'
			self.tablename = 'call_list'
			self.start_limit, self.end_limit = 7099, None 
		self.setInputArray()
			
	def setInputArray(self):
		'''
			internal method, not to be called
		'''
		input_array = fetchData('google_input_table').to_numpy()
		if self.start_limit or self.end_limit:
			self.input_array = input_array[self.start_limit : self.end_limit]
		else: 
			self.input_array = input_array
		self.setInputArrayLength()

	def setInputArrayLength(self):
		self.len_input_array = len(self.input_array)

	@property
	def getLongBreak(self)-> int: 
		return 300 # 5 minutes

	@property
	def getShortBreak(self) -> int:
		return 2 # 2 seconds

	@property
	def getTablename(self) -> str:
		return self.tablename

	@property
	def getSettings(self)-> tuple[str, int, str, str, int, int, np.ndarray, int, int]:
		return self.file_name, self.chunksize, self.mode, self.tablename, self.start_limit, self.end_limit, self.input_array, self.long_break, self.short_break

	@property
	def getInputArray(self) ->  np.ndarray:
		return self.input_array

	@property
	def getInputArrayLength(self) -> int:
		return self.len_input_array

def googleExtractor(**kwargs: str):
	'''
		runs setup, then gets array of company names, then iterates through the list via ThreadPoolExecutor: extractionManager()
		stops process if Captcha is triggered, finally sends a df of results to database.
	'''
	Print.intro()
	# testmode_kwarg = kwargs.get('testmode', None)
	# _, chunksize, _, tablename, _, _, input_array, long_break, _= getSettings(testmode_kwarg)
	
	S.setSettings(**kwargs)
	_, chunksize, _, tablename, _, _, input_array, long_break, _ = S.getSettings
	print(S.getSettings)


	nested_input_array = makeChunks(input_array, chunksize)
	Print.info(len(nested_input_array))

	with tqdm(total = len(nested_input_array)) as pbar1: 
		with tqdm(total = len(input_array)) as pbar2:
			with ThreadPoolExecutor(max_workers=min(32, (os.cpu_count() or 1) + 4)) as executor: 
				for chunk in nested_input_array:
					futures = list(tqdm(executor.map(Extration, chunk), total=len(chunk)))
					# list(tqdm(executor.map(Extration, chunk), total=len(chunk)))
					pbar2.update(chunksize) 	
					pbar1.update(1)
		if len(pbar1) != len(nested_input_array):
			time.sleep(long_break)
	Print.outro()

if __name__ == '__main__':
	S = Settings()
	Print = Print() 
	Driver = Driver()
	googleExtractor(testmode = True)
	
	# # googleExtractor(testmode = False)













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
	
