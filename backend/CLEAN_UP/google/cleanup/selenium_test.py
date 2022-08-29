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
	- [ ] bytt ut CSV  med database
	- [ ] changge main according to "IMPORTANT"
	- [ ] import list from csv-data 
	- [ ] include "org num" in data output for easier indexing. 
	- [ ] 

'''


def getDriver():
	''' gets chrome driver '''
	return webdriver.Chrome(options = driverOptions())

def driverOptions():
	''' settings for selenium '''
	options = webdriver.ChromeOptions()
	# options.add_experimental_option("excludeSwitches", ["enable-automation"])
	# options.add_experimental_option('useAutomationExtension', False)
	# options.add_argument("--no-startup-window")
	return options

# def worker(chunk):
# 	''' 
# 		import list 
# 		NB: remember to make sure it gets imported correctly 
# 		chunk = [] # consists of 500-1000 company names.
# 	'''
	
# 	''' generate driver for this worker'''
# 	base_url = "https://www.google.com/" 
# 	# driver = getDriver()
# 	# driver.get(base_url)

# 	# ''' bypass cookie-consent  '''
# 	# WebDriverWait(driver, 0).until(EC.element_to_be_clickable((By.XPATH, './/*[@id="W0wltc"]'))).click()
# 	driver=""
# 	''' initiate scraper '''
# 	claimedStatus(chunk, driver)


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
	return np.array((org_num, search_term, is_unreqistered, is_unclaimed), dtype = object)
	# saveData(np.array((search_term, org_num, is_unreqistered, is_unclaimed), dtype = object))

# def saveData(status):
# 	'''
# 		check if path exist,
# 		then makes a datafrasme from data, 
# 		then reads -> concat -> save dataframe for each iteration
# 	'''
# 	if os.path.exists('../_output_data/google_maps_data.csv'):
# 		df_old = pd.read_csv('../_output_data/google_maps_data.csv')
# 	else:
# 		df_old = pd.DataFrame(columns = ['bedrift', 'google Uregistrert', 'google Uerklært'])
# 	df = pd.DataFrame([status[1:]], columns = ['bedrift', 'google Uregistrert', 'google Uerklært'])
# 	df_final = pd.concat([df_old,df], axis=0)
# 	df_final = df_final.drop_duplicates()
# 	df_final.to_csv('../_output_data/google_maps_data.csv', index = False)
# 	# print(f'google data for {status[0]} was succsessfullly saved.')


# def getInputChunks():
# 	'''
# 	imports proff_data.csv from the proff folder, then;
# 	returns a numpy arrray of ['bedrift'] & ['org num'] from gulesider_data.csv
# 	'''
# 	input_df = pd.read_csv('../_output_data/gulesider_data.csv')
# 	input_df = input_df[['bedrift', 'org num']][:15]
# 	return list(input_df.to_numpy())


def getInputChunks(conn):
	''' fetches old_df from database '''
	tablename = 'brreg_table'
	curr = getCursor(conn)  
	curr.execute(f"SELECT * FROM {tablename};") 
	input_data = curr.fetchall()
	column_names  = [desc[0] for desc in curr.description]
	input_df = pd.DataFrame(input_data, columns = column_names)
	input_df = input_df[['org_num', 'navn']][:1] #for testing
	inputs = input_df.to_numpy()
	curr.close()
	conn.close()
	return inputs



# def apiManager(current_page):
# 	'''
# 		Manages the api from "Brønnøysynd registeret"
# 	'''
# 	json = getRequest(current_page)
# 	'''pages'''
# 	page = getpage(json)
# 	toal_pages = getMaxpages(page)
# 	current_page = getCurrentpage(page)	
# 	next_page = getnext_page(current_page)

# 	'''data'''
# 	data = getData(json)
	
# 	df = makeDataframe(data)
# 	df = datasetEditor(df)
# 	return df, toal_pages, current_page, next_page

def makeDataframe(status):
	''' makes dataframe from json '''
	df = pd.DataFrame([status], columns = ['bedrift', 'navn', 'google Uregistrert', 'google Uerklært'])
	
	# df = pd.DataFrame([status[1:]], columns = ['bedrift', 'google Uregistrert', 'google Uerklært'])
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

	status = claimedStatus(chunk, driver)
	df = makeDataframe(status)
	return df
	# pass 

''' ___ PART 2, POSTGRES  ____________________________________________________ '''

payload = { 'dbname'   : 'media_vest',
			'host'     : 'localhost',
			'user'     : 'postgres',
			'password' : 'Orikkel1991',
			'tablename': 'google_table',  }

import json
import psycopg2
from psycopg2.extras import Json
from sqlalchemy import create_engine

''' ___ PREP _______________________________________________ '''
def parseConfig():
	''' returns parsed payload from config file '''
	dbname = payload['dbname']
	host = payload['host']
	user = payload['user']
	password = payload['password']
	tablename = payload['tablename']
	return dbname, host, user, password, tablename

def getCursor(conn):
	''' returns postgres cursor '''
	return conn.cursor()

def getConnection():
	''' connects to database '''
	return psycopg2.connect(
		dbname = dbname, 
		host = host, 
		user = user, 
		password = password)

def insertData(df):
	''' 
		inserts final dataframe to database, 
		creates new table if table it does not exsist, else it updates
	'''
	conn = getConnection()
	curr = getCursor(conn)
	dbname, host, user, password, tablename = parseConfig()
	engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:5432/{dbname}')
	df.to_sql(f'{tablename}', engine, if_exists = 'replace', index = False)

def fetchData(conn, tablename):
	''' fetches old_df from database '''
	dbname, host, user, password, tablename = parseConfig()
	curr = getCursor(conn)  
	curr.execute(f"SELECT * FROM {tablename};") 
	old_data = curr.fetchall()
	column_names  = [desc[0] for desc in curr.description]
	old_df = pd.DataFrame(old_data, columns = column_names)
	curr.close()
	conn.close()
	return old_df
  
def concatData(df, old_df):
	''' Concat old_df from database with new df from api request '''
	df.set_index(['org_num'],  inplace = True)
	try: 
		df.drop('org_num', axis = 1, inplace=True)
	except KeyError:
		pass
	old_df.set_index(old_df['org_num'].squeeze(), inplace = True)
	try: 
		old_df.drop('org_num', axis = 1, inplace=True)
	except KeyError:
		print("KeyError: old_df['org_num']")
	df = pd.concat((df, old_df), axis = 0)
	df = df.groupby(df.index).last().reset_index()
	return df

def databaseManager(df):
	''' manage database '''
	try:
		conn = getConnection()
		old_df = fetchData(conn, tablename)
	except:
		print("table does not exsist")
	try: 
		df = concatData(df, old_df)
	except:
		print("unable to concat") 
	insertData(df)	


# def saveData(status):
# 	'''
# 		check if path exist,
# 		then makes a datafrasme from data, 
# 		then reads -> concat -> save dataframe for each iteration
# 	'''
# 	if os.path.exists('../_output_data/google_maps_data.csv'):
# 		df_old = pd.read_csv('../_output_data/google_maps_data.csv')
# 	else:
# 		df_old = pd.DataFrame(columns = ['bedrift', 'google Uregistrert', 'google Uerklært'])
# 	df = pd.DataFrame([status[1:]], columns = ['bedrift', 'google Uregistrert', 'google Uerklært'])
# 	df_final = pd.concat([df_old,df], axis=0)
# 	df_final = df_final.drop_duplicates()
# 	df_final.to_csv('../_output_data/google_maps_data.csv', index = False)
# 	# print(f'google data for {status[0]} was succsessfullly saved.')



if __name__ == '__main__':
	# print("_"*91)
	# print("|											  |")
	# print("|			Starting: GOOGLE Extractor 			  |")
	# print("|											  |")
	# print("_"*91)
	# print()

	''' preperations: parse config, connect to database and connect to api manager '''
	dbname, host, user, password, tablename = parseConfig()
	conn = getConnection()
	
	input_df = getInputChunks(conn)
	# print(input_df)
	chunks = [input_df] # TEMP
	for chunk in chunks:
		# print(chunk)
		# break
		with concurrent.futures.ThreadPoolExecutor() as executor:
				results = executor.map(extractionManager, chunk)
				for result in results:
					print(result)
					databaseManager(result)	


	# print("																		"+"_"*91)
	# print("																		|											  |")
	# print("																		|				   Data Extraction Complete. 				  |")
	# print("																		|											  |")
	# print("																		"+"_"*91)
	# print()			






# def main():
# 	'''
# 		sets up all nessasary functions, 
# 		then gets list of company names, 
# 		then iterates through the list via multithreading: claimedStatus().
# 	'''

# 	''' gets the list of companies, divided into chunks '''
# 	chunks = getInputChunks() 
# 	# # with tqdm(total = len(chunks)) as pbar:
# 	with concurrent.futures.ThreadPoolExecutor() as executor:
# 		results = executor.map(worker, chunks)
# 		for result in results:
# 			databaseManager(result)
# 	# 				# pbar.update(1)

# main()