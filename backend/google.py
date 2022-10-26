
# todo [ ] move to code_workshop while not running 


''' TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP  TEMP TEMP TEMP TEMP TEMP TEMP TEMP  TEMP TEMP TEMP TEMP TEMP TEMP TEMP  TEMP TEMP TEMP TEMP TEMP TEMP TEMP '''
'''	

#FIXME Rar bug:
	#>	virker som den printer ut  "already exsist" på alle prospektene


#! ____ CURRENT ISSUE _______________________________________________________________________________________________ !#

#! - [1] sqlalchemy.exc.IntegrityError --> Key already exists.
	sqlalchemy.exc.IntegrityError: (psycopg2.errors.UniqueViolation) duplicate key value violates unique constraint "call_list_test_pkey"
	DETAIL:  Key (org_num)=(928293785) already exists.

	[SQL: INSERT INTO call_list_test (org_num, navn, google_profil, eier_bekreftet, komplett_profil, ringe_status, link_til_profil) VALUES (%(org_num)s, %(navn)s, %(google_profil)s, %(eier_bekreftet)s, %(komplett_profil)s, %(ringe_status)s, %(link_til_profil)s)]
	[parameters: {'org_num': 928293785, 'navn': 'VESTAMATIC CRE GMBH', 'google_profil': 'Usikkert', 'eier_bekreftet': True, 'komplett_profil': False, 'ringe_status': False, 'link_til_profil': 'https://www.google.com/search?q=VESTAMATIC CRE GMBH'}]
	(Background on this error at: https://sqlalche.me/e/14/gkpj)
#! ______________________________________________________________________________________________________________ !#





#! ____ ERROR LOG _______________________________________________________________________________________________ !#

- [1] error on line, 192: 
	if not (self.is_registered and self.is_claimed and self.has_info) or self.is_registered == 'Usikkert':
		AttributeError: 'Extraction' object has no attribute 'is_reqistered'
	#* Error suddenly dissapeared for some reason.. ¯\_(ツ)_/¯
	# 	
	# 
	# 
	#  STIAN KJELDSAND         error           False            False         False
- [2] NoSuchElementException: checkClaimedStatus() -> {"method":"xpath","selector":"//*[@id="kp-wp-tab-overview"]//span[2]/span/a"}
		 Skjer på prospekt nr ~8980 
	
#! ______________________________________________________________________________________________________________ !#

#* ____ OVER ALL PLAN FOR REWORK ________________________________________________________________________________ *#

	___ THE ISSUE ___
	Not satisfied with how multithreading is done (in regards to OOP).
		They way Extraction is dependent on ThreadWithReturnValues are confusing to read, 
		and also possibly not nessasary anymore since extracted values does not leave (returned out of) the class anymore. 

	___ THE PLAN ___
	will remodel Extraction, and maybe remove ThreadWithReturnValue:
		Extraction Remodel:
			- Extracted values should be stored in __init__
			- If returning __init__ values are nessasary, then;
				 they should be returned via @property 
			 

#* ______________________________________________________________________________________________________________ *#


'''
''' TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP  TEMP TEMP TEMP TEMP TEMP TEMP TEMP  TEMP TEMP TEMP TEMP TEMP TEMP TEMP  TEMP TEMP TEMP TEMP TEMP TEMP TEMP '''



from gc import freeze
from pprint import pp
import time
from pprint import pprint

from pydantic import Extra 
from SQL.db_query import getTest; START = time.perf_counter() #Since it also takes time to Import libs, I allways START the timer asap. 
import re
import os
import numpy as np
import pandas as pd
import datetime as dt
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
from threading import Thread  
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import ui
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


'''___ local imports __________
'''
from file_manager import *
from recaptcha_solver import Recaptcha as Recaptcha

'''___ TEST IMPORTS __________
'''
from SQL.add_row import getSession
import SQL.db as db


def makeChunks(input_array: np.ndarray , chunksize: int) -> list[np.ndarray]:
	return [input_array[i:i + chunksize] for i in range(0, len(input_array), chunksize)]  

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
	def __init__(self, url=None):
		self.url = url
		self.driver = None

	def getDriver(self) -> webdriver:
		return webdriver.Chrome(options = self.getDriverOptions)

	def setUrl(self, new_url):
		self.url = new_url 

	@property
	def getUrl(self) -> str:
		return self.url
	
	def linkBuilder(self, url: str) -> str:
		new_url = url + ' maps&hl=en'
		self.setUrl(new_url)

	def prepDriver(self, url):
		driver = self.getDriver()
		self.linkBuilder(url)
		driver.get(self.url)
		driver.current_window_handle  #* CATCHPA SOLVER
		time.sleep(S.getShortBreak)
		self.driver = driver
		return driver

	# def passDriver(self):


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





# #> ___________________________________ TEST SPLITTED VERSION OF Extraction _____________________________________________________

# #? PARENT CLASS (child to ThreadPoolExecutor)
# # class Extraction(ThreadPoolExecutor):	
# class Extraction:	
# 	def __init__(self):
# 		# self.input_array = input_array
# 		# self.org_num = input_array[0]
# 		# self.navn = input_array[1]
# 		# self.search_term = input_array[1]
# 		self.input_array = None
# 		self.org_num = None
# 		self.navn = None
# 		self.search_term = None
# 		# 
# 		self.google_profil = None
# 		self.eier_bekreftet = None
# 		self.komplett_profil = None
# 		self.ringe_status = False
# 		self.is_claimed = None
# 		self.is_registered = None
# 		self.has_info = None
# 		self.liste_id = None
# 		self.check = None
# 		self.url = None
# 		# self.driver = None
# 		# self.driver = Driver
		
# 		# self.getData(input_array)
# 		# self.V = Verification(input_array)
# 		# self.C = Check(input_array)	
# 		# self.getData()

# 	#TODO [] GET DATA ER ALT FOR STOR !!!!
# 	def getData(self, input_array):
# 	# def getData(self, input_array: np.ndarray) -> np.ndarray or str:
# 	# def getData(self, ) -> np.ndarray or str:
# 		# V = Verification(input_array)
# 		# C = Check(input_array)
# 		''' 
# 			NOTE: input_array = chunks 
# 			gets driver, builds url ,calls captcha solver, tries to find certain elements,
# 			finally returns array of bools or a error string
# 		'''
# 		self.input_array = input_array
# 		self.org_num = input_array[0]
# 		self.search_term = input_array[1]
# 		self.url = "https://www.google.com/search?q=" + self.search_term
# 		# self.driver = Driver.prepDriver(self.url)
		
		
# 		self.V = Verification(self.url, )
# 		# self.V = Verification()
# 		self.C = Check()
# 		# print(self.search_term)
# 		# exit()
# 		# if self.checkGoogleAlarmTrigger(self.driver):
# 		# 	'''
# 		# 		Safty mechanism; 
# 		# 		checks if google's flooding alarms are triggered and blocks accsess to search results, 
# 		# 		if so Extraction will set extracted values for prospects to "CaptchaTriggered" then skip to next
# 		# 	'''
# 		# 	self.alarmTriggerAction()
# 		# 	exit()
# 		# else:
# 		try: 								#! [try A]
# 			self.V.tryVerification()
# 		except NoSuchElementException:      #! [try A]  
# 			try:
# 				self.checkIfSuggestion()
# 			except NoSuchElementException:
# 				self.is_registered = False
			
# 		# #* ____________________________________________________________________________________
# 		'''
# 		sjekker om bedrift er registrert / if is_registered == True
# 		'''
# 		if self.is_registered:
# 			'''
# 			gets overview section from profile
# 			'''
# 			try:
# 				self.setCheck()
# 			except NoSuchElementException:
# 				self.check = None
# 		# _____________________________
# 		'''
# 		sjekker om bedriften har INFO
# 		'''
# 		try:							#? [try B] 
# 			self.checkHasInfo()
# 		except AttributeError: 			#? [try B]
# 			if self.check:
# 				self.has_info = True
# 			else:
# 				self.has_info = False
# 		# _____________________________

# 		'''
# 		sjekker om bedriften er CLAIMED
# 		'''
# 		try:							#* [try C]
# 			self.checkClaimedStatus()
# 		except AttributeError:  		#* [try C]	
# 			if self.check:
# 				'''
# 					hvis:
# 						- knapp ikke er der
# 						- overview er der
# 				'''
# 				self.is_claimed = True
# 			else:
# 				'''
# 					hvis:
# 						- knapp ikke er der
# 						- overview ikke er der
# 				'''
# 				self.is_claimed = False
# 		'''
# 		sjekker om alle er true eller ikke 
# 		'''	
# 		self.cheeckForTrippelTrue()	

# 	def checkIfSuggestion(self):
# 		'''
# 			Is called when tryVerification() was unsuccsessful.
# 			will look for search suggestions, if found then redirect to suggestion,
# 			then retries tryVerification()
# 		'''
# 		self.driver = Driver.prepDriver(self.url)
# 		ui.WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="L2AGLb"]'))).click()
# 		elems = self.driver.find_element(By.XPATH, '//*[@id="rhs"]/block-component//div[1]/a')
# 		self.url = elems.get_attribute('href')
# 		self.driver.get(self.url)
# 		# V = Verification(self)
# 		self.V.tryVerification()

# 	def cheeckForTrippelTrue(self):
# 		'''
# 			checks if prospect values are: [true, true, true]
# 				if true: [a] ignore
# 				   else: [b] call addRowToDb()
# 		'''
# 		if not (self.is_registered and self.is_claimed and self.has_info) or self.is_registered == 'Usikkert':
# 			session = getSession()
# 			row = db.CallListTest(self.org_num, self.search_term, self.is_registered, self.is_claimed, self.has_info, False, self.url)
# 			self.addRowToDb(row, session)

# 	def addRowToDb(self, row, session):
# 		'''
# 			will [a] try to add row to db, 
# 			  or [b] replace row if "a" was unsuccsessfull.
# 		'''
# 		try:
# 			session.add(row)
# 			session.commit()
# 		except:
# 			session.rollback()
# 			session.query(db.CallListTest).filter_by(org_num = self.org_num).delete()

# 	def alarmTriggerAction(self):
# 		self.is_registered, self.is_claimed, self.has_info, = "CaptchaTriggered", "CaptchaTriggered", "CaptchaTriggered"

# 	def checkGoogleAlarmTrigger(self, driver: webdriver) -> bool:
# 		html = driver.page_source
# 		return ('Systemene våre har oppdaget uvanlig trafikk' or 'unnusual traffic') in html

# #? CHILD CLASS TO Extraction
# class Verification(Extraction):

# 	def __init__(self, url):
# 		self.url = url 
# 		self.driver = None

# 	def tryVerification(self) -> None:
# 		'''
# 			Tries to verify if company is registered, with multiple search variations. 
# 			=> sets self.is_registered
# 		'''
# 		self.driver = Driver.prepDriver(self.url)
# 		if self.getVerify():
# 			verify = self.getVerify()
# 			self.C.checkRegistered(verify, self.getAltVerify(verify), self.getAltSearchTerms())	

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
	
# 	def setCheck(self):
# 		#TODO change setCheck() to SetCheck()
# 		'''
# 			Changed getOverview to setCheck
# 		'''
# 		# self.check = self.driver.find_element(By.XPATH, '//*[@id="kp-wp-tab-overview"]/div[2]/div/div/div/div/div/div[5]/div/div/div') #! IKKE FJERN DENNE
# 		self.check = self.driver.find_element(By.XPATH, '//*[@id="kp-wp-tab-overview"]')

# # #? CHILD CLASS TO Extraction
# class Check(Extraction):
# 	# def __init__(self, input_array):
# 	# 	super().__init__(input_array)
# 		# Extraction.__init__(self, input_array)
		
# 	def checkRegistered(self, verify, alt_verify, alt_search_term):
# 		if re.search(self.search_term, verify, re.IGNORECASE):
# 			self.is_registered = True
# 		elif re.search(alt_search_term, verify, re.IGNORECASE):
# 			self.is_registered = True
# 		elif re.search(self.search_term, alt_verify, re.IGNORECASE) or re.search(alt_search_term, alt_verify, re.IGNORECASE):
# 			self.is_registered = True
# 		else:
# 			self.is_registered = 'Usikkert'		

# 	def checkHasInfo(self) -> None:
# 		'''
# 			=> sets self.has_info
# 		'''
# 		check_info = self.check.text
# 		if 'Add missing information' in check_info or 'Legg til manglende informasjon' in check_info:
# 			self.has_info = False
# 		elif self.is_registered:
# 			self.has_info = True
# 		else:
# 			self.has_info = False

# 	def checkClaimedStatus(self) -> None:
# 		'''
# 			=> sets self.is_claimed
# 		'''
# 		check_claimed = self.check.get_attribute('innerHTML')
# 		if 'cQhrTd' in check_claimed:
# 			self.is_claimed = True
# 		else: 
# 			try: 
# 				self.driver.find_element(By.XPATH, '//*[@id="kp-wp-tab-overview"]//span[2]/span/a')
# 			except NoSuchElementException:
# 				try:
# 					self.driver.find_element(By.XPATH,'//*[@id="kp-wp-tab-overview"]/div[2]/div/div/div/div/div/div/div[5]/div/div/div/div[1]/a')
# 				except:
# 					print(f"ERROR WITH: {self.search_term}")
# 			if 'cQhrTd' in self.check.get_attribute('innerHTML'):
# 				self.is_claimed = True
# 			else: 
# 				self.is_claimed = False


# # #> HVA SOM IKKE ER NØDVENDIG
# # ''' #! DEPRICATED / DISABLED FOR NOW  '''
# # # # def retry_click(self, number_of_retries, wait_before_reclick):
# # # # 	'''
# # # # 	Is called if clicking suggestion-button was unsucsessfull;
# # # # 	will retry the click untill either [a] succsess or [b] "number_of_retries" exceeded
# # # # 	'''
# # # # 	while number_of_retries > 0:
# # # # 		time.sleep(wait_before_reclick)
# # # # 		try:
# # # # 			ui.WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#rhs > block-component > div > div.dG2XIf.Wnoohf.OJXvsb > div > div > div > div.ifM9O > div > div > div.EfDVh.wDYxhc.NFQFxe > div > a'))).click()
# # # # 			break
# # # # 		except:
# # # # 			pass
# # # #		number_of_retries = number_of_retries - 1


# class Driver(Extraction):
# 	def __init__(self, url=None):
# 		self.url = url
# 		self.driver = None

# 	def getDriver(self) -> webdriver:
# 		return webdriver.Chrome(options = self.getDriverOptions)

# 	def setUrl(self, new_url):
# 		self.url = new_url 

# 	@property
# 	def getUrl(self) -> str:
# 		return self.url
	
# 	def linkBuilder(self, url: str) -> str:
# 		new_url = url + ' maps&hl=en'
# 		self.setUrl(new_url)

# 	def prepDriver(self, url):
# 		driver = self.getDriver()
# 		self.linkBuilder(url)
# 		driver.get(self.url)
# 		driver.current_window_handle  #* CATCHPA SOLVER
# 		time.sleep(S.getShortBreak)
# 		self.driver = driver
# 		return driver

# 	# def passDriver(self):


# 	@property
# 	def getDriverOptions(self) -> webdriver.ChromeOptions:
# 		options = webdriver.ChromeOptions()
# 		options.add_experimental_option("excludeSwitches", ["enable-automation"]) # disable the automation bar [part 1]
# 		options.add_experimental_option('useAutomationExtension', False) # disable the automation bar [part 2]
# 		options.add_argument("window-size=1920,1080")
# 		options.add_argument("--headless") # opens window as invisible
# 		options.add_argument("--disable-gpu") # disable GPU rendering (only software render) 
# 		options.add_argument('--no-sandbox') # Bypass OS security model	
# 		options.add_experimental_option('excludeSwitches', ['enable-logging'])  #stops webdriver from printing in console
# 		options.add_experimental_option("excludeSwitches", ["enable-automation"])
# 		options.add_experimental_option('excludeSwitches', ['enable-logging'])
# 		options.add_experimental_option('useAutomationExtension', False)
# 		options.add_argument('--disable-blink-features=AutomationControlled')
# 		return options




# #> _______________________________________________________________________________________________________________________________


#! ___________________________________ OLD VERSION OF Extraction ______________________________________________________________

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

	# def getData(self, input_array: np.ndarray) -> np.ndarray or str:
	# 	''' 
	# 		NOTE: input_array = chunks 
	# 		gets driver, builds url ,calls captcha solver, tries to find certain elements,
	# 		finally returns array of bools or a error string
	# 	'''
	# 	self.url = "https://www.google.com/search?q=" + self.search_term
	# 	self.driver = Driver.prepDriver(self.url)
	# 	if self.checkGoogleAlarmTrigger(self.driver):
	# 		'''
	# 			Safty mechanism; 
	# 			checks if google's flooding alarms are triggered and blocks accsess to search results, 
	# 			if so Extraction will set extracted values for prospects to "CaptchaTriggered" then skip to next
	# 		'''
	# 		self.alarmTriggerAction()
	# 		exit()
	# 	else:
	# 		try: 								#! [try A]
	# 			self.tryVerification()
	# 		except NoSuchElementException:      #! [try A]  
	# 			try:
	# 				self.checkIfSuggestion()
	# 			except NoSuchElementException:
	# 				self.is_registered = False
			
	# 	#* ____________________________________________________________________________________
	# 	'''
	# 	sjekker om bedrift er registrert / if is_registered == True
	# 	'''
	# 	if self.is_registered:
	# 		'''
	# 		gets overview section from profile
	# 		'''
	# 		try:
	# 			self.setCheck()
	# 		except NoSuchElementException:
	# 			self.check = None
	# 	# _____________________________
	# 	'''
	# 	sjekker om bedriften har INFO
	# 	'''
	# 	try:							#? [try B] 
	# 		self.checkHasInfo()
	# 	except AttributeError: 			#? [try B]
	# 		if self.check:
	# 			self.has_info = True
	# 		else:
	# 			self.has_info = False
	# 	# _____________________________

	# 	'''
	# 	sjekker om bedriften er CLAIMED
	# 	'''
	# 	try:							#* [try C]
	# 		self.checkClaimedStatus()
	# 	except AttributeError:  		#* [try C]	
	# 		if self.check:
	# 			'''
	# 				hvis:
	# 					- knapp ikke er der
	# 					- overview er der
	# 			'''
	# 			self.is_claimed = True
	# 		else:
	# 			'''
	# 				hvis:
	# 					- knapp ikke er der
	# 					- overview ikke er der
	# 			'''
	# 			self.is_claimed = False
	# 	'''
	# 	sjekker om alle er true eller ikke 
	# 	'''	
	# 	self.cheeckForTrippelTrue()	


	def getData(self, input_array: np.ndarray) -> np.ndarray or str:
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

	def tryVerification(self):
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
		
	def tryCheck(self):	
		'''
		gets overview section from profile
		'''
		try:
			self.setCheck()
		except NoSuchElementException:
			self.check = None

	def tryInfo(self):
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

	def tryClaimed(self):
		'''
		sjekker om bedriften er CLAIMED
		'''
		try:							
			self.checkClaimedStatus()
		except AttributeError:  		
			if self.check:
				'''
					hvis:
						- knapp ikke er der
						- overview er der
				'''
				self.is_claimed = True
			else:
				'''
					hvis:
						- knapp ikke er der
						- overview ikke er der
				'''
				self.is_claimed = False

	def checkIfSuggestion(self):
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

	def cheeckForTrippelTrue(self):
		'''
			checks if prospect values are: [true, true, true]
				if true: [a] ignore
				   else: [b] call addRowToDb()
		'''
		if not (self.is_registered and self.is_claimed and self.has_info) or self.is_registered == 'Usikkert':
			session = getSession()
			row = db.CallListTest(self.org_num, self.search_term, self.is_registered, self.is_claimed, self.has_info, False, self.url)
			self.addRowToDb(row, session)

	def addRowToDb(self, row, session):
		'''
			will [a] try to add row to db, 
			  or [b] replace row if "a" was unsuccsessfull.
		'''
		try:
			session.add(row)
			session.commit()
		except:
			session.rollback()
			session.query(db.CallListTest).filter_by(org_num = self.org_num).delete()

	def alarmTriggerAction(self):
		self.is_registered, self.is_claimed, self.has_info, = "CaptchaTriggered", "CaptchaTriggered", "CaptchaTriggered"

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
				
	def checkRegistered(self, verify, alt_verify, alt_search_term):
		if re.search(self.search_term, verify, re.IGNORECASE):
			self.is_registered = True
		elif re.search(alt_search_term, verify, re.IGNORECASE):
			self.is_registered = True
		elif re.search(self.search_term, alt_verify, re.IGNORECASE) or re.search(alt_search_term, alt_verify, re.IGNORECASE):
			self.is_registered = True
		else:
			self.is_registered = 'Usikkert'		

	def checkHasInfo(self) -> None:
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

	def checkClaimedStatus(self) -> None:
		'''
			=> sets self.is_claimed
		'''
		check_claimed = self.check.get_attribute('innerHTML')
		if 'cQhrTd' in check_claimed:
			self.is_claimed = True
		else: 
			try: 
				self.driver.find_element(By.XPATH, '//*[@id="kp-wp-tab-overview"]//span[2]/span/a')
			except NoSuchElementException:
				try:
					self.driver.find_element(By.XPATH,'//*[@id="kp-wp-tab-overview"]/div[2]/div/div/div/div/div/div/div[5]/div/div/div/div[1]/a')
				except:
					print(f"ERROR WITH: {self.search_term}")
			if 'cQhrTd' in self.check.get_attribute('innerHTML'):
				self.is_claimed = True
			else: 
				self.is_claimed = False

	def setCheck(self):	
		'''
			NOTE: Changed setOverview to setCheck
		'''
		# self.check = self.driver.find_element(By.XPATH, '//*[@id="kp-wp-tab-overview"]/div[2]/div/div/div/div/div/div[5]/div/div/div') #! IKKE FJERN DENNE
		self.check = self.driver.find_element(By.XPATH, '//*[@id="kp-wp-tab-overview"]')

	def checkGoogleAlarmTrigger(self, driver: webdriver) -> bool:
		html = driver.page_source
		return ('Systemene våre har oppdaget uvanlig trafikk' or 'unnusual traffic') in html

#! _______________________________________________________________________________________________________________________________





class Settings:
	def __init__(self):
		self.mode = None
		self.tablename = None
		self.start_limit = None
		self.end_limit = None
		self.input_array = None
		self.len_input_array = None
		self.file_name = self.getFileName
		self.long_break = self.getLongBreak
		self.short_break = self.getShortBreak
		self.chunksize = parseSettings(self.file_name)['chunk_size']
	
	def setSettings(self, **kwargs):
		if kwargs.get('testmode', None):
			self.mode = 'Test Mode'
			self.tablename = 'call_list_test'
			# self.start_limit, self.end_limit = 8950, 8960
			# self.start_limit, self.end_limit = 8700, 9000
			self.start_limit, self.end_limit = 8804, 8805
		else:
			self.mode = 'Publish Mode'
			self.tablename = 'call_list'
			self.start_limit, self.end_limit = 8800, None

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
	def getFileName(self)-> str: 
		return 'google' # 5 minutes

	@property
	def getLongBreak(self)-> int: 
		return 300 # 5 minutes

	@property
	def getShortBreak(self) -> float:
		return 0.5 # 2 seconds

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
	S.setSettings(**kwargs)
	_, chunksize, _, _, _, _, input_array, long_break, _ = S.getSettings
	print(S.setSettings())

	nested_input_array = makeChunks(input_array, chunksize)
	Print.info(len(nested_input_array))


	with ThreadPoolExecutor(max_workers=min(32, (os.cpu_count() or 1) + 4)) as executor: 
		for input_array in nested_input_array:
			_ = list(tqdm(executor.map(Extraction, input_array), total = len(input_array)))

	## TEMP WHILE TESTING
	# with tqdm(total = len(nested_input_array)) as pbar1: 
	# 	with tqdm(total = len(input_array)) as pbar2:
	# 		with ThreadPoolExecutor(max_workers=min(32, (os.cpu_count() or 1) + 4)) as executor: 
	# 			for chunk in nested_input_array:
	# 				_ = list(tqdm(executor.map(Extraction, chunk), total = len(chunk)))
	# 				pbar2.update(chunksize) 	
	# 				pbar1.update(1)
		
	print()
	print(getTest())
	print()
	Print.outro()

if __name__ == '__main__':
	S = Settings()
	Print = Print() 
	Driver = Driver()
	googleExtractor(testmode = True)
	# googleExtractor(testmode = False)
	


##! ___ FULL ERROR LOGS __________________________

''' #! [1] AttributeError in Extraction class 
	______________________________________________________________
					Starting: Google Extractor
	______________________________________________________________

	HAS NO KWARGS
	("google", 50, "Publish Mode", "call_list", 8800, None, array([[928293785, "VESTAMATIC CRE GMBH"],
		[928294633, "OFFERLINDS MEKANISKA AB"],
		[928294838,
			"DRAGSNES SECURITY -SELVFORSVAR OG KONFLIKTHÅNDTERING"],
		...,
		[999665497, "ANNE KARI ØDEGÅRD"],
		[999665896, "BAUNEN FISK OG VILT AS"],
		[999666612, "FYSIOTERAPI RENATE MEIJER"]], dtype=object), 300, 0.5)
	None
	Running: Publish Mode
	Output_table used: call_list
	Input_array starts from: [8800:None]
	Chunksize: 50
	Input length: 11978
	Number of chunks: 240
	Break procedure:
					will take a long break between each chunk; [0:05:00],
					and a short break between every iteration; [0:00:00.500000]


	24%|███████████████████████████████████████████████▊                                                                                                                                                       | 12/50 [00:03<00:12,  3.08it/s]
	0%|                                                                                                                                                                                                             | 0/11978 [00:26<?, ?it/s]
	0%|                                                                                                                                                                                                               | 0/240 [00:26<?, ?it/s]
	Traceback (most recent call last):
	File "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/backend/google.py", line 385, in <module>
		googleExtractor(testmode = False)
	File "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/backend/google.py", line 369, in googleExtractor
		_ = list(tqdm(executor.map(Extraction, chunk), total = len(chunk)))
	File "C:/Users/Big Daddy B/AppData/Local/Programs/Python/Python310/lib/site-packages/tqdm/std.py", line 1195, in __iter__
		for obj in iterable:
	File "C:/Users/Big Daddy B/AppData/Local/Programs/Python/Python310/lib/concurrent/futures/_base.py", line 621, in result_iterator
		yield _result_or_cancel(fs.pop())
	File "C:/Users/Big Daddy B/AppData/Local/Programs/Python/Python310/lib/concurrent/futures/_base.py", line 319, in _result_or_cancel
		return fut.result(timeout)
	File "C:/Users/Big Daddy B/AppData/Local/Programs/Python/Python310/lib/concurrent/futures/_base.py", line 458, in result
		return self.__get_result()
	File "C:/Users/Big Daddy B/AppData/Local/Programs/Python/Python310/lib/concurrent/futures/_base.py", line 403, in __get_result
		raise self._exception
	File "C:/Users/Big Daddy B/AppData/Local/Programs/Python/Python310/lib/concurrent/futures/thread.py", line 58, in run
		result = self.fn(*self.args, **self.kwargs)
	File "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/backend/google.py", line 116, in __init__
		t = Thread(target=self.getData(i))
	File "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/backend/google.py", line 150, in getData
		self.cheeckForTrippelTrue()
	File "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/backend/google.py", line 176, in cheeckForTrippelTrue
		if not (self.is_reqistered and self.is_claimed and self.has_info) or self.is_reqistered == "Usikkert":
	AttributeError: "Extraction" object has no attribute "is_reqistered"	
'''

'''#! [ ] --Empty error log
'''

##! ______________________________________________



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
