import os
import string
import time 
import pandas as pd
import numpy as np
from os import path
from tqdm import tqdm
import concurrent.futures
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



'''
IMPORTANT:
	webdriver kan ikke ha multithreading i seg, 
	så du må endre på formelen slik at den åpner en ny webdriver for hver thread, 
	evt kan du dele opp listen i chunks så hver webdriver har 
	X antall bedrifter å arbeide med før den lukkes ned. 

 NOTE: 
 	Har problemer med chunks og multithreading
 	Har problemer med ?? -> nå vil ikke dataen bli lagret men virker som den finner det.


	TODO: 
	- [ ] changge main according to "IMPORTANT"
	- [ ] import list from csv-data 
	- [ ] include "org num" in data output for easier indexing. 
	- [ ] 

'''


def getDriver():
	return webdriver.Chrome(options = driverOptions())

def driverOptions():
	options = webdriver.ChromeOptions()
	options.add_experimental_option("excludeSwitches", ["enable-automation"])
	options.add_experimental_option('useAutomationExtension', False)
	# options.add_argument("--window-size=%s" % "1920,1080")
	# chrome_options.add_argument("--headless")
	options.add_argument("--no-startup-window")

	return options


def worker(chunk):
	''' import list 
		NB: remember to make sure it gets imported correctly '''
	# chunk = [] # consists of 500-1000 company names. 
	
	''' generate driver for this worker'''
	base_url = "https://www.google.com/" 
	driver = getDriver()
	driver.get(base_url)

	''' bypass cookie-consent  '''
	WebDriverWait(driver, 0).until(EC.element_to_be_clickable((By.XPATH, './/*[@id="W0wltc"]'))).click()
	
	''' initiate scraper '''
	claimedStatus(chunk, driver)


def claimedStatus(chunk, driver):
	'''
		get the google page for the searchword, 
		then checks if the searchword is a registered business, 
		and if it is unclaimed.
		returns a np.array to saveData() for each iteration
	'''
	# company_list = chunk[0]
	# org_num_list = chunk[1]
	# print(company_list)
	# print(org_num_list)
	# for row in chunk:
	# 	search_term = row[0]
	# 	org_num = row[1]
	# 	print(search_term)
	# 	print(org_num)
	# 	print("_"*100)

	search_term = chunk[0]
	org_num = chunk[1]
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
	saveData(np.array((search_term, org_num, is_unreqistered, is_unclaimed), dtype = object))

def saveData(status):
	'''
		check if path exist,
		then makes a datafrasme from data, 
		then reads -> concat -> save dataframe for each iteration
	'''
	print(status)
	if os.path.exists('../_output_data/google_maps_data.csv'):
		df_old = pd.read_csv('../_output_data/google_maps_data.csv')
	else:
		df_old = pd.DataFrame(columns = ['bedrift', 'google Uregistrert', 'google Uerklært'])
	df = pd.DataFrame([status], columns = ['bedrift', 'google Uregistrert', 'google Uerklært'])
	df_final = pd.concat([df_old,df], axis=0)
	df_final = df_final.drop_duplicates()
	df_final.to_csv('../_output_data/google_maps_data.csv', index = False)
	print(f'google data for {status[0]} was succsessfullly saved.')


def getInputChunks():
	'''
	imports proff_data.csv from the proff folder, then;
	returns a numpy arrray of ['bedrift'] & ['org num'] from gulesider_data.csv
	'''
	input_df = pd.read_csv('../_output_data/gulesider_data.csv')
	
	input_df = input_df[['bedrift', 'org num']][:15]
	return list(input_df.to_numpy())



def main():
	'''
		sets up all nessasary functions, 
		then gets list of company names, 
		then iterates through the list via multithreading: claimedStatus().
	'''

	''' gets the list of companies, divided into chunks '''
	chunks = getInputChunks() 

	# with tqdm(total = len(companies)) as pbar:
	with concurrent.futures.ThreadPoolExecutor() as executor:
		results = executor.map(worker, chunks)
		# for result in results:
				# pbar.update(1)
main()


''' OLD MAIN'''
# def main():
# 	'''
# 		sets up all nessasary functions, 
# 		then gets list of company names, 
# 		then iterates through the list via multithreading: claimedStatus().
# 	'''
# 	base_url = "https://www.google.com/" 
# 	driver = getDriver()
# 	driver.get(base_url)
# 	''' bypass cookie-consent  '''
# 	WebDriverWait(driver, 0).until(EC.element_to_be_clickable((By.XPATH, './/*[@id="W0wltc"]'))).click()
# 	''' TEMP LIST for testing '''
# 	companies = [	'Felleskatalogen AS',
# 					'mcdonalds torgallmenningen',
# 					'Focus Media AS',
# 					'Filatelistisk Forlag AS',
# 					'Ringlets Forlag Tor Egil Kvalnes',
# 					'IT Media',
# 					'Tut for Top20 DA',
# 					'Mobilportalen DA',
# 					'Reisenett AS',
# 					'Tess SÃ¸rÃ¸st AS',
# 					'Landvik Historielag',
# 					'Tump ANS',
# 					'Ambulanse-Norge',
# 					'Reiseguidenno DA',
# 					'Nettstart DA',					]
# 	for company_name  in companies:
# 		claimedStatus(company_name, driver)
# 	driver.close()
# # main()
