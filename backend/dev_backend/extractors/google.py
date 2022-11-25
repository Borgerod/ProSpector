''' TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP  TEMP TEMP TEMP TEMP TEMP TEMP TEMP  TEMP TEMP TEMP TEMP TEMP TEMP TEMP  TEMP TEMP TEMP TEMP TEMP TEMP TEMP '''
'''	

#> UNDER DEVELOPMENT

'''
''' TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP  TEMP TEMP TEMP TEMP TEMP TEMP TEMP  TEMP TEMP TEMP TEMP TEMP TEMP TEMP  TEMP TEMP TEMP TEMP TEMP TEMP TEMP '''

import time
from typing import Any

from SQL.query import getGoogleInputTable; START = time.perf_counter() #Since it also takes time to Import libs, I allways START the timer asap. 
from typing_extensions import Self

import re
import os
import numpy as np
import datetime as dt
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from sqlalchemy.orm.session import Session

'''___ local imports __________
'''
# from file_manager import *
from utilities.recaptcha_solver import Recaptcha as Recaptcha
# from SQL.db_query import getTest
# from SQL.add_row import getSession
import SQL.db as db

from SQL.insert import Insert

def makeChunks(input_array: np.ndarray , chunksize: int) -> list[np.ndarray]:
	return [input_array[i:i + chunksize] for i in range(0, len(input_array), chunksize)]  

# class Print:
# 	def intro(self):
# 		print("_"*62)
# 		print("                  Starting: Google Extractor                ")
# 		print("_"*62)
# 		print()
	
# 	def info(self, len_nested_input: int):
# 		'''
# 			prints useful information about the run and it's settings. Called by googleExtractor()
# 		'''
# 		_, chunksize, mode, tablename, start_limit, end_limit, _, long_break, short_break = S.getSettings
# 		print(f"Running: {mode}")
# 		print(f"Output_table used: {tablename}")
# 		print(f"Input_array starts from: [{start_limit}:{end_limit}]")
# 		print(f"Chunksize: {chunksize}")
# 		print(f"Input length: {S.getInputArrayLength}")
# 		print(f"Number of chunks: {len_nested_input}")
# 		print(f"""Break procedure: 
# 		will take a long break between each chunk; [{str(dt.timedelta(seconds = long_break))}], 
# 		and a short break between every iteration; [{str(dt.timedelta(seconds = short_break))}]""")
# 		print("\n\n\n")
	
# 	def outro(self):
# 		print("_"*62)
# 		print("                   Data Extraction Complete.                 ")
# 		print(f"             Finished in {round(time.perf_counter() - START, 2)} second(s) | [{str(dt.timedelta(seconds = round(time.perf_counter() - START)))}]                ")
# 		print("_"*62)
# 		print()

class Driver:
	def __init__(self, url:str = None):
		self.url = url
		self.driver = None
		self.short_break = 0.5
		self.long_break = 300

	def getDriver(self) -> webdriver:
		return webdriver.Chrome(options = self.getDriverOptions)

	def setUrl(self, new_url:str) ->Self:
		self.url = new_url 

	@property
	def getUrl(self) -> str:
		return self.url
	
	def linkBuilder(self, url:str) -> Self:
		new_url = url + ' maps&hl=en'
		self.setUrl(new_url)

	def prepDriver(self, url:str) -> Self and webdriver:
		driver = self.getDriver()
		self.linkBuilder(url)
		driver.get(self.url)
		driver.current_window_handle  #* CATCHPA SOLVER
		time.sleep(self.short_break)
		self.driver = driver
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





class Extraction(ThreadPoolExecutor):	
	def __init__(self, input_array):
		self.org_num = input_array[0]
		self.navn = input_array[1]
		self.search_term = input_array[1]
		self.google_profil = None
		self.eier_bekreftet = None
		self.komplett_profil = None
		self.ringe_status = False
		self.is_claimed = None
		self.is_registered = None
		self.has_info = None
		self.liste_id = None
		self.check = None
		self.url = None
		self.getData(input_array)

	def getData(self, input_array: np.ndarray) -> None:
			''' 
				NOTE: input_array = chunks 
				gets driver, builds url ,calls captcha solver, tries to find certain elements,
				finally returns array of bools or a error string
			'''
			self.url = "https://www.google.com/search?q=" + self.search_term
			self.driver = Driver.prepDriver(self.url)
			if self.checkGoogleAlarmTrigger(self.driver):
				'''
					Safty mechanism; 
					checks if google's flooding alarms are triggered and blocks accsess to search results, 
					if so Extraction will set extracted values for prospects to "CaptchaTriggered" then skip to next
				'''
				self.alarmTriggerAction()
				exit()
			else:
				self.tryVerification()
			'''
			sjekker om bedrift er registrert / if is_registered == True
			'''
			if self.is_registered:
				self.tryCheck()
			self.tryInfo()
			self.tryClaimed()
			self.cheeckForTrippelTrue()	

	def alarmTriggerAction(self) -> list[Self]:
		self.is_registered, self.is_claimed, self.has_info, = "CaptchaTriggered", "CaptchaTriggered", "CaptchaTriggered"

	def checkGoogleAlarmTrigger(self, driver: webdriver) -> bool:
		html = driver.page_source
		return ('Systemene våre har oppdaget uvanlig trafikk' or 'unnusual traffic') in html


	def tryVerification(self) -> None or Self:
		try: 								
			'''
				Tries to verify if company is registered, with multiple search variations. 
				=> sets self.is_registered
			'''
			if self.getVerify():
				verify = self.getVerify()
				self.checkRegistered(verify, self.getAltVerify(verify), self.getAltSearchTerms())			
		except NoSuchElementException:      
			try:
				self.checkIfSuggestion()
			except NoSuchElementException:
				self.is_registered = False

	def getVerify(self) -> Self:
		return self.driver.find_element(By.CLASS_NAME, "osrp-blk").text

	def getAltVerify(self, verify:str) -> str:
		return [re.sub(r"[^a-zA-Z0-9]+", ' ', k) for k in verify.split("\n")][0]
				
	def getAltSearchTerms(self) -> str:
		alt_search_term = self.search_term
		for ch in [' AS',' ASA', ' AB']:
			if ch in alt_search_term:
				alt_search_term = alt_search_term.replace(ch,"")
		return alt_search_term
	
	def checkRegistered(self, verify:str, alt_verify:str, alt_search_term:str) -> Self:
		if re.search(self.search_term, verify, re.IGNORECASE):
			self.is_registered = True
		elif re.search(alt_search_term, verify, re.IGNORECASE):
			self.is_registered = True
		elif re.search(self.search_term, alt_verify, re.IGNORECASE) or re.search(alt_search_term, alt_verify, re.IGNORECASE):
			self.is_registered = True
		else:
			self.is_registered = 'Usikkert'		

	def checkIfSuggestion(self) -> Self:
		'''
			Is called when tryVerification() was unsuccsessful.
			will look for search suggestions, if found then redirect to suggestion,
			then retries tryVerification()
		'''
		ui.WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="L2AGLb"]'))).click()
		elems = self.driver.find_element(By.XPATH, '//*[@id="rhs"]/block-component//div[1]/a')
		self.url = elems.get_attribute('href')
		self.driver.get(self.url)
		self.tryVerification()


	def tryCheck(self) -> None or Self:	
		'''
		gets overview section from profile
		'''
		try:
			self.setCheck()
		except NoSuchElementException:
			self.check = None

	def setCheck(self) -> Self:	
		'''
			NOTE: Changed setOverview to setCheck
		'''
		# self.check = self.driver.find_element(By.XPATH, '//*[@id="kp-wp-tab-overview"]/div[2]/div/div/div/div/div/div[5]/div/div/div') #! IKKE FJERN DENNE
		self.check = self.driver.find_element(By.XPATH, '//*[@id="kp-wp-tab-overview"]')


	def tryInfo(self) -> None or Self:
		'''
		sjekker om bedriften har INFO
		'''
		try:							
			self.checkHasInfo()
		except AttributeError: 			
			if self.check:
				self.has_info = True
			else:
				self.has_info = False

	def checkHasInfo(self) -> Self:
		'''
			=> sets self.has_info
		'''
		check_info = self.check.text
		if 'Add missing information' in check_info or 'Legg til manglende informasjon' in check_info:
			self.has_info = False
		elif self.is_registered:
			self.has_info = True
		else:
			self.has_info = False


	def tryClaimed(self) -> None or Self:
		'''
		Tries to check if google progile is claimed, with the exception being:
			- if "Own this business?" button is not present,
			and/or 
			- if google profile is present or not.
			
			----------------------
			| Note: 			 |
			| [o] -> present     | 
			| [x] -> NOT present |
			----------------------
		'''
		try:							
			self.checkClaimedStatus()
		except AttributeError:  		
			if self.check:
				''' is_claimed = True, if:
					 - [x] button
					 - [o] profile
				'''
				self.is_claimed = True
			else:
				''' is_claimed = False, if:
					 - [x] button
					 - [x] profile
				'''
				self.is_claimed = False
	
	def checkClaimedStatus(self) -> Self:
		''' => sets self.is_claimed
			Tries to locate "Own this business?" button and which button-type:

			"own this business?" button has different xpaths & class names for when the business is claimed or not.
				claimed: 
					- xpath; '//*[@id="kp-wp-tab-overview"]/div[2]/div/div/div/div/div/div/div[5]/div/div/div/div[1]/a'
					- class_name; 'cQhrTd'
				unclaimed: 
					- xpath; '//*[@id="kp-wp-tab-overview"]//span[2]/span/a'
					- class_name; 'ndJ4N'
		'''
		
		''' 
		first it gets the innerHTML and searches for 'cQhrTd' 
		'''
		check_claimed = self.check.get_attribute('innerHTML')
		if 'cQhrTd' in check_claimed:
			self.is_claimed = True
		else: 
			'''
			if not, it will try to look for alternatives
			'''
			try: 
				''' Alt 1; UNCLAIMED
					looks for "own this business?" by Xpath
				'''
				self.driver.find_element(By.XPATH, '//*[@id="kp-wp-tab-overview"]//span[2]/span/a')
			except NoSuchElementException:
				try:
					''' Alt 2; CLAIMED
						looks for "own this business?" by Xpath
					'''
					self.driver.find_element(By.XPATH,'//*[@id="kp-wp-tab-overview"]/div[2]/div/div/div/div/div/div/div[5]/div/div/div/div[1]/a')
				except:
					''' Alt 3; FOUND NEITHER
					'''
					print(f"ERROR WITH: {self.search_term}")
			''' 
			if ALT 1 or 2 was found, then it confirms the class_name.
				If exception occours, the check fails and raises "AttributeError" for "tryClaimed()"
			'''
			if 'cQhrTd' in self.check.get_attribute('innerHTML'):
				''' class_name = 'cQhrTd' => CLAIMED '''
				self.is_claimed = True
			else: 
				''' class_name = 'ndJ4N' => UNCLAIMED '''
				self.is_claimed = False

	def cheeckForTrippelTrue(self) -> None:
		'''
			checks if prospect values are: [true, true, true]
				if true: [a] ignore
				   else: [b] call addRowToDb()
		'''
		if not (self.is_registered and self.is_claimed and self.has_info) or self.is_registered == 'Usikkert':
			Insert.toCallList(self.org_num, self.search_term, self.is_registered, self.is_claimed, self.has_info, False, self.url)

from multiprocessing import Pool


Driver = Driver()
class GoogleExtractor:
	def __init__(self) -> None:
		self.chunksize = 50
		self.org_num = None
		self.navn = None
		self.search_term = None
		self.google_profil = None
		self.eier_bekreftet = None
		self.komplett_profil = None
		self.ringe_status = False
		self.is_claimed = None
		self.is_registered = None
		self.has_info = None
		self.liste_id = None
		self.check = None
		self.url = None
		# self.getData(input_array)


	def worker(self, array_item) -> None:
		self.org_num = array_item[0]
		self.navn = array_item[1]
		self.search_term = array_item[1]
		self.url = "https://www.google.com/search?q=" + self.search_term 
		self.extractPage()		

	def runExtraction(self) -> None:
		'''
			runs setup, then gets array of company names, then iterates through the list via ThreadPoolExecutor: extractionManager()
			stops process if Captcha is triggered, finally sends a df of results to database.
		'''
		input_array = getGoogleInputTable().to_numpy()
		nested_input_array = makeChunks(input_array, self.chunksize)

		with Pool() as pool:
			list(tqdm(pool.imap_unordered(self.worker, input_array), total = len(input_array)))
