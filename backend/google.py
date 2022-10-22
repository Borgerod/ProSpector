''' #* TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP  TEMP TEMP TEMP TEMP TEMP TEMP TEMP  TEMP TEMP TEMP TEMP TEMP TEMP TEMP  TEMP TEMP TEMP TEMP TEMP TEMP TEMP '''
'''	



#! ____ ERROR LOG _______________________________________________________________________________________________ !#

- [1] error on line, 192: 
	if not (self.is_registered and self.is_claimed and self.has_info) or self.is_registered == 'Usikkert':
		AttributeError: 'Extration' object has no attribute 'is_reqistered'
	#* Error suddenly dissapeared for some reason.. ¯\_(ツ)_/¯
	# 			
#! ______________________________________________________________________________________________________________ !#



'''
''' #* TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP  TEMP TEMP TEMP TEMP TEMP TEMP TEMP  TEMP TEMP TEMP TEMP TEMP TEMP TEMP  TEMP TEMP TEMP TEMP TEMP TEMP TEMP '''

import time; START = time.perf_counter() #Since it also takes time to Import libs, I allways START the timer asap. 
import re
import os
import numpy as np
import pandas as pd
import datetime as dt
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
from threading import Thread  
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from sqlalchemy.orm import Session

'''___ local imports __________
'''
from file_manager import *
from postgres import cleanUp, databaseManager, googleDatabaseManager
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
	def __init__(self, group = None, target = None, name = None, args = (), kwargs = {}):
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
		self.rowData = None

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
			try: 								#! [try A]
				self.tryVerification()
				try:							#? [try B] 
					check = self.getOverview()
					self.checkHasInfo(check)
					self.checkClaimedStatus(check)
				except NoSuchElementException:  #? [try B]    
					self.has_info = True
					self.is_claimed = True
			
			except NoSuchElementException:      #! [try A]    
				self.is_registered = False
				try:							#* [try C]
					check = self.getOverview()
					self.checkHasInfo(check)
					self.checkClaimedStatus(check)
				except NoSuchElementException:  #* [try C]
					self.has_info = False
					self.is_claimed = False	
			self.cheeckForTrippelTrue()
			
			# result_list = [self.org_num, self.search_term, self.is_registered, self.is_claimed, self.has_info, False]
			# df = makeDataframe([result_list])
			# print(f"{df}")
			# time.sleep(0.1)
			# databaseManager(df, S.getTablename, to_user_api = True)
			#! _______________TEMP: WHILE TESTING _______________
			# googleDatabaseManager(df, S.getTablename, to_user_api = True)
			# return df
	# 		self.setRowData(df)
	
	# def setRowData(self, df):
	# 	self.rowData = df

	# @property
	# def getRowData(self):
	# 	return self.rowData 
	#! ____________________________________________________________  

		# TODO: [ ] add function that;  Removes prospects from "call_list" that is [true, true, true]
	def cheeckForTrippelTrue(self):
		'''
			checks if prospect values are: [true, true, true]
				will ignore if true, else it adds to DB.
		'''
		if not (self.is_registered and self.is_claimed and self.has_info) or self.is_registered == 'Usikkert':
			session = getSession()
			row = db.CallList(self.org_num, self.search_term, self.is_registered, self.is_claimed, self.has_info, False)
			session.add(row)
			session.commit()

	def setTableName(self, tablename):
		self.tablename = tablename
		
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
		if self.getVerify():
			verify = self.getVerify()
			self.checkRegistered(verify, self.getAltVerify(verify), self.getAltSearchTerms())
	
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

	def checkHasInfo(self, check) -> None:
		'''
			=> sets self.has_info
		'''
		check_info = check.text
		if 'Add missing information' in check_info or 'Legg til manglende informasjon' in check_info:
			self.has_info = False
		elif self.is_registered:
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
		elif self.is_registered:
			self.is_claimed = True
		else:
			self.is_claimed = False

	def getOverview(self, ) -> any:
		return self.driver.find_element(By.XPATH, '//*[@id="kp-wp-tab-overview"]/div[2]/div/div/div/div/div/div[5]/div/div/div')

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
			# self.start_limit, self.end_limit = 330, 335
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
	# testmode_kwarg = kwargs.get('testmode', None)
	# _, chunksize, _, tablename, _, _, input_array, long_break, _= getSettings(testmode_kwarg)
	
	S.setSettings(**kwargs)
	_, chunksize, _, _, _, _, input_array, long_break, _ = S.getSettings
	print(S.getSettings)
	print(Settings().getTablename)

	# #! ___________ TEMP: WHILE TESTING ______________________
	# input_array = np.array([
	# 	[812338862, 'Saval B.V.'],
    #    	[812372262, 'OMV PETROM S.A.'],
	# 	[812398652, 'HÅRSTRÅET AS'],
    #    	[812479792, 'WORKFORCE INTERNATIONAL CONTRACTORS LTD'],
    #    	[925294853, 'THW INSTRUMENTATION LTD'],
    #    	[925296236, 'NORDIC SAFETY ENGINEERING AS'],
    #    	[925305405, 'HÅVARDSHOLM MASKIN AS'],
    #    	[925310336, 'U.S. DIRECT E-COMMERCE LIMITED'],
    #    	[925315923, 'OLE CHRISTIAN ELVERHØY'],
    #    	[925321974, 'EIDET DRIFT AS'],
    #    	[925322490, 'TRAVEL HOLDING AS'],
	# 	])
	# # master_df = pd.DataFrame(columns = ['org_num', 'navn', 'google_profil', 'eier_bekreftet', 'komplett_profil', 'ringe_status'])
	# #! _______________________________________________________

	nested_input_array = makeChunks(input_array, chunksize)
	Print.info(len(nested_input_array))


	#! TEMP: DISABLING TQDM
	# with ThreadPoolExecutor(max_workers=min(32, (os.cpu_count() or 1) + 4)) as executor: 
	# 	for chunk in nested_input_array:
	# 		_ = list(tqdm(executor.map(Extration, chunk), total = len(chunk)))

	with tqdm(total = len(nested_input_array)) as pbar1: 
		with tqdm(total = len(input_array)) as pbar2:
			with ThreadPoolExecutor(max_workers=min(32, (os.cpu_count() or 1) + 4)) as executor: 
				for chunk in nested_input_array:
					_ = list(tqdm(executor.map(Extration, chunk), total = len(chunk)))
					pbar2.update(chunksize) 	
					pbar1.update(1)
					# df = Extration.getRowData() 				#! TEMP: WHILE TESTING
					# master_df = pd.concat(master_df, df) 		#! TEMP: WHILE TESTING
			# print("\n")											#! TEMP: WHILE TESTING
		# #! TEMP: DISABLING LONG BREAK
		# if len(pbar1) != len(nested_input_array):
		# 	time.sleep(long_break)
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

