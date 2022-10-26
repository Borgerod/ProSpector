
# todo [ ] move to code_workshop while not running 


''' TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP  TEMP TEMP TEMP TEMP TEMP TEMP TEMP  TEMP TEMP TEMP TEMP TEMP TEMP TEMP  TEMP TEMP TEMP TEMP TEMP TEMP TEMP '''
'''	
#! STIAN KJELDSAND gives an error because3 of 	ElementNotInteractableException , look into that	



#! ____ ERROR LOG _______________________________________________________________________________________________ !#

- [1] error on line, 192: 
	if not (self.is_registered and self.is_claimed and self.has_info) or self.is_registered == 'Usikkert':
		AttributeError: 'Extration' object has no attribute 'is_reqistered'
	#* Error suddenly dissapeared for some reason.. ¯\_(ツ)_/¯
	# 	
	# 
	# 
	#  STIAN KJELDSAND         error           False            False         False
	
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
             
                

# TODO [ ] NOTE: google sometimes comes with a suggestion when no searchresult is found,
# TODO		e.g. "OLE ALEKSANDER BERGELIEN maps" gave a suggestion on "Bergelien Bygg AS"
# TODO		 implement this to Extraction

#* ______________________________________________________________________________________________________________ *#


'''
''' TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP  TEMP TEMP TEMP TEMP TEMP TEMP TEMP  TEMP TEMP TEMP TEMP TEMP TEMP TEMP  TEMP TEMP TEMP TEMP TEMP TEMP TEMP '''



from pprint import pp
import time
from pprint import pprint 
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

	# def linkBuilder(self, english_res_extention: str, base_url: str, search_term: str) -> str:
	# 	if search_term == 'OLE ALEKSANDER BERGELIEN':
	# 		print(english_res_extention + base_url + search_term + ' maps')
	# 	return english_res_extention + base_url + search_term + ' maps'

	# def prepDriver(self, base_url, search_term):
	# 	driver = self.getDriver()
	# 	english_res_extention = "https://www.google.com/setprefs?sig=0_uH3W1kJTr26Rp8z0zGD-F5RIznI%3D&source=en_ignored_notification&prev="
	# 	driver.get(self.linkBuilder(english_res_extention, base_url, search_term))
		
	# 	driver.current_window_handle  #* CATCHPA SOLVER
	# 	time.sleep(S.getShortBreak)
	# 	return driver
	def linkBuilder(self, base_url: str, search_term: str) -> str:
		# if search_term == 'OLE ALEKSANDER BERGELIEN':
			# print( base_url + search_term + ' maps&hl=en')
		return base_url + search_term + ' maps&hl=en'

	def prepDriver(self, base_url, search_term):
		driver = self.getDriver()
		english_res_extention = "https://www.google.com/setprefs?sig=0_uH3W1kJTr26Rp8z0zGD-F5RIznI%3D&source=en_ignored_notification&prev="
		driver.get(self.linkBuilder( base_url, search_term))
		
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

# class ThreadWithReturnValue(Thread):
# 	def __init__(self, group = None, target = None, name = None, args = (), kwargs = {}):
# 		Thread.__init__(self, group, target, name, args, kwargs)
# 		self._return = None

# 	def run(self):
# 		if self._target is not None:
# 			self._return = self._target(*self._args, **self._kwargs)

# 	def join(self, *args):
# 		Thread.join(self, *args)
# 		return self._return



class Extration(ThreadPoolExecutor):	
# class Extration:	
	def __init__(self, input_array):#, google_profil, eier_bekreftet, komplett_profil, ringe_status, liste_id):
		self.org_num = input_array[0]
		self.navn = input_array[1]
		# self.org_num = org_num
		# self.navn = navn
		self.google_profil = None
		self.eier_bekreftet = None
		self.komplett_profil = None
		self.ringe_status = False
		self.liste_id = None
		self.check = None
		self.getData(input_array)


	def getData(self, input_array: np.ndarray) -> np.ndarray or str:
		''' 
			NOTE: input_array = chunks 
			gets driver, builds url ,calls captcha solver, tries to find certain elements,
			finally returns array of bools or a error string
		'''
		self.setOrgNumAndSearchTerm(input_array)
		driver = Driver.prepDriver("https://www.google.com/search?q=" , self.search_term)
		if self.checkGoogleAlarmTrigger(driver):
			'''
				Safty mechanism; 
				checks if google's flooding alarms are triggered and blocks accsess to search results, 
				if so Extraction will set extracted values for prospects to "CaptchaTriggered" then skip to next
				# todo [ ] it should also throw an error or otherwisse stop the process. or maybe set a pause-timer on 24 hours. 
			'''
			self.alarmTriggerAction()
			
		else:
			self.driver = driver
			# body = self.driver.find_element(By.TAG_NAME("Body")).get_attribute("innerHTML")
			# body = self.driver.find_element(By.TAG_NAME("Body"))
			# 
			
			# if self.search_term == 'OLE ALEKSANDER BERGELIEN':
				# body = self.driver.find_element(By.CLASS_NAME, "nGydZ").get_attribute("innerHTML") 

				# body = self.driver.find_element(By.CLASS_NAME, "TQc1id hSOk2e rhstc4").get_attribute("innerHTML") 
				# body = self.driver.find_element(By.XPATH, './/*[@id="rhs"]/block-component').get_attribute("innerHTML") 
				# body = self.driver.find_element(By.CSS_SELECTOR, )
				# url = driver.find_element_by_xpath('//a[@href="'+url+'"]')
				
				# '''
				# 	setning: 	Bergelien Bygg AS
				# 	Href: 		/search?q=Bergelien+Bygg+AS+Building+firm+in+Veggli&si=AC1wQDCb48pJOhjniU-CPpWXcWQCAuOVlcIjSvs_FGbLklR5diRIgw2TlZZpOBe5gWxXFjciO4rMvDSv6aTTIyeXG8v40Ssm-ChMqSz8my2aJ76BN_w-cKBE_grudZzY3z-r5nKMWSKJP6MvXMOOafnChZDbPzWO3AY-wZQfgaT5YGtsOtYRb0AvOeAfg5gfdDywEb9TVOzx&sa=X&ved=2ahUKEwjCgaKbxfb6AhWrSfEDHeR1BD4Q6RN6BAg4EAE

				# 	MULIG LØSNING:
				# 	url extention for å få engelsk resultat:
				# 	/setprefs?sig=0_uH3W1kJTr26Rp8z0zGD-F5RIznI%3D&source=en_ignored_notification&prev=
				# 	https://www.google.com/search?q=OLE+ALEKSANDER+BERGELIEN+maps&hl=en
				# '''

				##! _______________________________ KEEP THIS_________________________________
				
				
				# from selenium.webdriver.common.action_chains import ActionChains
				# accept_button = driver.find_element(By.XPATH, '//*[@id="L2AGLb"]')
				# ActionChains(driver).move_to_element(accept_button).perform()
				# accept_button.click()
				# time.sleep(1)
				# # 
				# # a = self.driver.find_element(By.CLASS_NAME, 'M3LVze')
				# # print(a.get_attribute("outerHTML"))
				# # print(a.get_attribute("innerHTML"))
				# # print(a.text)
				# suggestion = self.driver.find_element(By.CLASS_NAME, 'M3LVze').click()
				##! _______________________________ KEEP THIS_________________________________

			try: 								#! [try A]
				self.tryVerification()
			except NoSuchElementException:      #! [try A]  
				try:
					self.checkIfSuggestion()
				except NoSuchElementException:
					self.is_registered = False
			# print(f"{self.search_term} ==> {self.is_registered}")
				# self.checkAlternatives()
				# self.is_registered = False
				
		#* ____________________________________________________________________________________
		'''
		sjekker om bedrift er registrert / if is_registered == True
		'''
		if self.is_registered:
			'''
			gets overview section from profile
			'''
			try:
				self.setOverview()
			except NoSuchElementException:
				self.check = None
		# _____________________________
		'''
		sjekker om bedriften har INFO
		'''
		try:							#? [try B] 
			self.checkHasInfo()
		except AttributeError: 			#? [try B]
			if self.check:
				self.has_info = True
			else:
				self.has_info = False
		# _____________________________

		'''
		sjekker om bedriften er CLAIMED
		'''
		try:							#* [try C]
			self.checkClaimedStatus()
		except AttributeError:  		#* [try C]	
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
		# print(f"{self.search_term} => {self.is_claimed}\n")
		# * ____________________________________________________________________________________





		'''
		sjekker om alle er true eller ikke 
		'''	
		self.cheeckForTrippelTrue()


	def checkIfSuggestion(self):
		try:
			# accept_button = self.driver.find_element(By.XPATH, '//*[@id="L2AGLb"]')
			# ActionChains(self.driver).move_to_element(accept_button).perform()
			accept_button = ui.WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(By.XPATH, '//*[@id="L2AGLb"]'))
			accept_button.click()
			time.sleep(1)
		except:
			time.sleep(5)
			accept_button = self.driver.find_element(By.XPATH, '//*[@id="L2AGLb"]')
			ActionChains(self.driver).move_to_element(accept_button).perform()
			accept_button.click()
			time.sleep(1)
		try:
			self.driver.find_element(By.CLASS_NAME, 'M3LVze').click()
			self.tryVerification()
		except ElementNotInteractableException:
			try:
				time.sleep(5)
				# self.driver.find_element(By.CLASS_NAME, 'M3LVze').click()
				# self.tryVerification()
				self.checkIfSuggestion()
			except ElementNotInteractableException:
				print(f"except ElementNotInteractableException occored for {self.search_term}")
				# self.is_registered = False
				self.is_registered = "error"
			# print("error occoured: ElementNotInteractableException")
			# self.checkIfSuggestion()
		



	def checkAlternatives(self):
		'''
			checks the "See results about" suggestion, 
			before deciding if is_registerede is false or not. 
		'''

		# See results about
		# if self.search_term == 'OLE ALEKSANDER BERGELIEN':
			# element = self.driver.find_element(By.CLASS_NAME, "GyAeWb").text
			
			# Bergelien Bygg AS
			# check_claimed = self.check.get_attribute('outerHTML')
			# element = self.driver.find_element(By.CLASS_NAME, "g VjDLd wF4fFd g-blk")
			# body = self.driver.FindElement(By.ByTagName("Body"))

			# element = self.driver.find_element(By.CLASS_NAME, "TQc1id hSOk2e rhstc4")
			# TQc1id hSOk2e rhstc4
			# pprint.pprint(body)
		# try:
		# 	html = self.driver.page_source
		# 	if 'See results about' in html:
		# 		print(f"{self.search_term} => {True}\n")
		# 	else:
		# 		print(f"{self.search_term} => {False}\n")
			
		
		# 	# element = self.driver.find_element(By.CLASS_NAME, "TQc1id hSOk2e rhstc4").text
		# 	# print(f"{self.search_term} => {element}\n")
		# 	# self.driver.find_element(By.XPATH, '//*[@id="rhs"]/block-component/div/div[1]/div/div/div/div[1]/div/div/div[2]/div/a')
		# except:
		# 	print(f"{self.search_term} => found no classname\n")
		# try:
		# 	element = self.driver.find_element(By.CLASS_NAME, "xpdopen")
		# 	print(f"{self.search_term} => {element}\n")
		# 	# self.driver.find_element(By.XPATH, '//*[@id="rhs"]/block-component/div/div[1]/div/div/div/div[1]/div/div/div[2]/div/a')
		# except:
		# 	print(f"{self.search_term} => found no classname\n")
		# try:
		# 	element = self.driver.find_element(By.XPATH, '//*[@id="rhs"]')
		# 	print(f"{self.search_term} => {element}\n")
		# except:
		# 	print(f"{self.search_term} => found no xpath\n")
		# self.is_registered = False
		# //*[@id="rhs"]/block-component/div/div[1]/div/div/div/div[1]/div/div/div[2]/div/a


	def cheeckForTrippelTrue(self):
		'''
			checks if prospect values are: [true, true, true]
				will ignore if true, else it adds to DB.
		'''
		if not (self.is_registered and self.is_claimed and self.has_info) or self.is_registered == 'Usikkert':
			# print(pd.DataFrame([self.org_num, self.navn, self.is_registered, self.is_claimed, self.has_info]))
			session = getSession()
			#! TEMP WHILE TESTING 
			try:
				row = db.CallListTest(self.org_num, self.search_term, self.is_registered, self.is_claimed, self.has_info, False)
				# row = db.CallList(self.org_num, self.search_term, self.is_registered, self.is_claimed, self.has_info, False)
				#error - IntegrityError:
				session.add(row)
				session.commit()
			except:
				print(f"{self.search_term} already exsist")
		#! TEMP while testing
		else:
			print(f"NOTE: {self.search_term} was trippel true")

	#! deprecated 
	# def setTableName(self, tablename):
	# 	self.tablename = tablename
		
	def setOrgNumAndSearchTerm(self, input_array: np.ndarray) -> None:
		self.org_num = input_array[0]
		self.search_term = input_array[1]
	
	def alarmTriggerAction(self):
		self.is_registered, self.is_claimed, self.has_info, = "CaptchaTriggered", "CaptchaTriggered", "CaptchaTriggered"

	def tryVerification(self) -> None:
		'''
			Tries to verify if company is registered, with multiple search variations. 
			=> sets self.is_registered
		'''
		try:
			if self.getVerify():
				verify = self.getVerify()
				self.checkRegistered(verify, self.getAltVerify(verify), self.getAltSearchTerms())	
		except ElementNotInteractableException:
			time.sleep(1)
			self.tryVerification()
		# except NoSuchElementException:
		# 	self.is_registered = False

			# print(f""" 
			# ERROR WITH {self.searchterm}:
			# 	ElementNotInteractableException exception triggered, 
			# 	url: {}
			# """)

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
		elif self.driver.find_element(By.XPATH, '//*[@id="kp-wp-tab-overview"]//span[2]/span/a'):
			if 'cQhrTd' in self.check.get_attribute('innerHTML'):
				self.is_claimed = True
			else: 
				self.is_claimed = False

	def setOverview(self):	
		'''
			Changed getOverview to setOverview
		'''
		# self.check = self.driver.find_element(By.XPATH, '//*[@id="kp-wp-tab-overview"]/div[2]/div/div/div/div/div/div[5]/div/div/div') #! IKKE FJERN DENNE
		self.check = self.driver.find_element(By.XPATH, '//*[@id="kp-wp-tab-overview"]')


	def checkGoogleAlarmTrigger(self, driver: webdriver) -> bool:
		html = driver.page_source
		return ('Systemene våre har oppdaget uvanlig trafikk' or 'unnusual traffic') in html

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
			print("HAS KWARGS")
			self.mode = 'Test Mode'
			self.tablename = 'call_list_test'
			self.start_limit, self.end_limit = 8800, 8810
		else:
			print("HAS NO KWARGS")
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
	print(S.getSettings)
	print(Settings().getTablename)


	nested_input_array = makeChunks(input_array, chunksize)
	Print.info(len(nested_input_array))
	with ThreadPoolExecutor(max_workers=min(32, (os.cpu_count() or 1) + 4)) as executor: 
		for chunk in nested_input_array:
			_ = list(tqdm(executor.map(Extration, chunk), total = len(chunk)))

	#! TEMP WHILE TESTING
	# with tqdm(total = len(nested_input_array)) as pbar1: 
	# 	with tqdm(total = len(input_array)) as pbar2:
	# 		with ThreadPoolExecutor(max_workers=min(32, (os.cpu_count() or 1) + 4)) as executor: 
	# 			for chunk in nested_input_array:
	# 				_ = list(tqdm(executor.map(Extration, chunk), total = len(chunk)))
	# 				pbar2.update(chunksize) 	
	# 				pbar1.update(1)
		
		##!: DISABLING LONG BREAK
		# if len(pbar1) != len(nested_input_array):
		# 	time.sleep(long_break)
	
	print()
	print(getTest())
	print()
	Print.outro()

if __name__ == '__main__':
	S = Settings()
	Print = Print() 
	Driver = Driver()
	# googleExtractor(testmode = True)
	googleExtractor(testmode = False)
	


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
		_ = list(tqdm(executor.map(Extration, chunk), total = len(chunk)))
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
	AttributeError: "Extration" object has no attribute "is_reqistered"	
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
