import time; start = time.perf_counter() #Since it also takes time to Import libs, I allways start the timer asap. 
import os
import re
import string
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
from inspect import currentframe, getframeinfo
import json
import psycopg2
from psycopg2.extras import Json
from sqlalchemy import create_engine
from tqdm import tqdm
import pandas as pd 
import requests 
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd 
import json
import psycopg2
from psycopg2.extras import Json
from sqlalchemy import create_engine
import concurrent.futures
from tqdm import tqdm

''' ____ LOCAL IMPORTS ____________ '''
# from postgres import databaseManager, cleanUp, fetchData
# from config import payload, tablenames, settings
# from brreg import datasetEditor, jsonDataframe



# def updateAPI(base_url, testmode, tablename):
# 	url = f'{base_url}dato={getLastUpdate(tablename)}T00:00:00.000Z'
# 	url = 'https://data.brreg.no/enhetsregisteret/api/oppdateringer/enheter?dato=2022-08-09T00:00:00.000Z' #FIXME: [TEMP] while testing
# 	last_update = checkLastUpdate()
# 	json_str = getRequest(url)
# 	import pprint
# 	pprint.pprint(json_str)

# 	# total_elements = gettotalElements(json_str)
# 	if gettotalElements(json_str) > 10000:
# 		actionDecider(table_exist = False, testmode, tablename)
# 		pass	#or break

# 	current_page = getCurrentpage(json_str)
# 	next_page = getnext_page(current_page)
# 	total_pages = getMaxpages(json_str)

# 	#? next_url = json_str['_embedded']['_links']['next']   #Not Sure if fast enough

# 	# ! EDIT THESE 
# 	data = getData(json)
# 	df = makeDataframe(data)
# 	df = datasetEditor(df)
# 	return df, total_pages, current_page, next_page




# # FIXME: TEMP WHILE TESTING
# def getLastUpdate(tablename):
# 	update_tracker = {
# 	'brreg_table': '2022-08-10',
# 	'gulesider_table': '2022-08-10',
# 	'google_table': '2022-08-10',
# 	'input_table': '2022-08-10',
# 	}
# 	return update_tracker[tablename]

# last_update_date = getLastUpdate(tablename)

# def update_timestamp(tablename):
# 	timestamp = dt.now().isoformat()
# 	print(timestamp)
# 	print(dt.now())
# 	print(dt.today())
# 	print(dt.today().strftime('%Y-%m-%d'))
# 	'''
# 		GET update_tracker
# 	'''
# # update_timestamp(tablename='brreg_table')


# def checkLastUpdate(tablename): #TODO: Finish this.
# 	'''
# 		checks for last date a update occoured, 
# 		returns parameter "oppdateringsid"
# 	'''
# 	# iso_format''
# 	update_tracker = getUpdateTracker()

# 	last_update = update_tracker[tablename]  
# 	today = dt.now().strftime('%Y-%m-%d')

# 	if last_update < today:
		

# 	'''
# 		the date i need:
# 		2022-08-09T00:00:00.000Z --> ISO-8601 
# 	'''
# 	return last_update
# # checkLastUpdate(tablename = 'brreg_table')







# ''' FIXME link builder test
# '''
# table_exist = False #bool if table exsist or not 
# if table_exist:
# 	action = 'oppdateringer/enheter'
# else:
# 	action = 'enheter/lastned'

# base_url = f'https://data.brreg.no/enhetsregisteret/api/{action}'

# basic_update_url = 'https://data.brreg.no/enhetsregisteret/api/oppdateringer/enheter'
# downlaod_url = 'https://data.brreg.no/enhetsregisteret/api/enheter/lastned'



# ''' FIXME - TEST OF BRREG.PY:
# 	- checking if it reads json-file -> export to database correctly  
# '''

# def brreg_downloader(): #* --- WHAT IS BEING TESTED 
# 	tablename = 'brreg_table' #FIXME --> [TEMP] while testing
# 	# json_file_name = 'enheter_alle_snippet.json.gz' #FIXME --> DATASET SNIPPET [TEMP] while testing
# 	json_file_name = 'enheter_alle.json.gz' #FIXME --> FULL DATASET [TEMP] while testing
# 	# total_elements = gettotalElements() 
# 	# ?  [TEMP CUT OUT] readDataset() [might not be needed]
# 		# print("reading dataset..")
# 		# data = readDataset(json_file = json_file_name)
# 		# print("    reading complete")
	
# 	print("making dataframe..")
# 	data = json_file_name #FIXME --> [TEMP] while testing
# 	df = jsonDataframe(data)
# 	print(df)
# 	print("    dataframe complete")
# 	print()

# 	print("editing dataframe..")
# 	df = datasetEditor(df)
# 	print(df)
# 	print("    editing complete")
# 	print()
	
# 	print("uploading to database..")
# 	databaseManager(df, tablename)
# 	print('    upload complete')
# 	print()

# 	print(f'Display results:\n\n{df}\n\n')
# 	db_table = fetchData(tablename)
# 	print(db_table)	
# 	print()

# 	# cleanup; check for duplicates

# 	# missing values; 
# 	# TODO need if statement for when database is empty

# 	print(f'|				   Finished in: {round(time.perf_counter() - start, 2)} second(s)				  |')

# ''' checking backup database for referance'''
# # db_table = fetchData('brreg_table_backup')
# # print(db_table)



# ''' ! OUTPUT FROM [DATASET SNIPPET]
# 		making dataframe..
# 		   organisasjonsnummer                                               navn                                  organisasjonsform  ... underTvangsavviklingEllerTvangsopplosning  maalform links
# 		0            922924368  - A THOUSAND WORDS - ØDEGÅRDEN GJERRUD TRANSLA...  {'kode': 'ENK', 'beskrivelse': 'Enkeltpersonfo...  ...                                     False    Bokmål    []

# 		[1 rows x 17 columns]
# 		    dataframe complete

# 		editing dataframe..
# 		     org_num                                               navn registreringsdato  mva_registrert  ...  konkurs  under_avvikling  under_tvangsavvikling_eller_oppløsning  maalform
# 		0  922924368  - A THOUSAND WORDS - ØDEGÅRDEN GJERRUD TRANSLA...        2019-06-19            True  ...    False            False                                   False    Bokmål

# 		[1 rows x 12 columns]
# 		    editing complete

# 		|                                  Finished in: 0.67 second(s)                            |
# '''

# ''' ! OUTPUT FROM [FULL DATASET]
# '''

# def diff_check():
# 	''' TEST DESC:
# 		 checks for differences between two dataframes.
# 		 represents "table from database" and "df from extractors"
# 	'''
# 	# make df1 and df2, then concat:
# 	df1 = pd.DataFrame({'org_num':[10,20,30,40],'B':['x','x','x','x']})	#* represents: DATABASE TABLE
# 	df2 = pd.DataFrame({'org_num':[10, 20],'B':['x', 'x']})				#* represents: EXTRACTOR DF 
# 	df = pd.concat([df1, df2])
# 	print(f'concated df:')
# 	print(df)
# 	print("_____")
	
# 	# checks for diff's based on column org_num
# 	diff_bool_series = df.duplicated(subset=['org_num'], keep=False) # pandas Series containing true/false for each row 
# 	print('diff_bool_series:')
# 	print(diff_bool_series)
# 	print(type(diff_bool_series))
# 	print("______")

# 	# create a new df containing all missing columns 
# 	missing_df = df[-diff_bool_series]  # DF containing all missing for each row 
# 	print(df)
# 	print("______")

# 	# Checking if df contains differences, if so --> prints a warning & list of missing org_num 
# 	if False in diff_bool_series:
# 		print('Error: imported DF contains missing elements.\n   displaying "org_num" for all missing values:')
# 		for i, bool_ in enumerate(diff_bool_series):
# 			missing_org_num = []
# 			if bool_ is False:
# 				org_num = df.iloc[i]['org_num']
# 				print(org_num)
# 				missing_org_num.append(org_num)
# 	else: 
# 		print('Succsess: imported DF contains NO missing element.')	

# # ''' ___ PART 1, BBREG API ____________________________________________________ '''

# 	# ## OLD GETREQUEST()
# 	# # def getRequest():
# 	# # 	url = 'https://data.brreg.no/enhetsregisteret/api/enheter/?page=3&size=20' #-i -X GET
# 	# # 	r = requests.get(url, timeout=10)
# 	# # 	json = r.json()
# 	# # 	return json

# 	# # NEW GETREQUEST()
# 	# def getRequest(next_page):
# 	# 	url = f'https://data.brreg.no/enhetsregisteret/api/enheter/?page={next_page}&size=20' #-i -X GET
# 	# 	r = requests.get(url, timeout = 10)
# 	# 	json = r.json()
# 	# 	return json


# 	# def getpage(json):
# 	# 	page =  json['page']
# 	# 	return page

# 	# def getMaxpages(page):
# 	# 	''' 
# 	# 		gets the total number of pages from JSON, 
# 	# 		used for breaking the loop 
# 	# 	'''
# 	# 	total_pages = page['totalPages']
# 	# 	return total_pages


# 	# def gettotalElements(page):
# 	# 	''' 
# 	# 		gets the total number of elements (Companies) from JSON, 
# 	# 		used for supervising & calculations
# 	# 	'''
# 	# 	total_elements = page['totalElements']
# 	# 	return total_elements

# 	# def main():
# 	# 	next_page=0
# 	# 	json = getRequest(next_page)
# 	# 	page = getpage(json)
# 	# 	print(getMaxpages(page))
# 	# 	print((gettotalElements(page)))
# 	# 	'''
# 	# 	totalElements: 1078364
# 	# 	maxPages: 53919
# 	# 	'''


# 	# if __name__ == '__main__':
# 	# 	main()

# # ''' ____ EXPERIMENTAL: Self Referance  ____________________________'''

# 	# def getLineNumber():
# 	# 	''' gets current line number --> linenumberpath '''
# 	# 	return currentframe().f_back.f_lineno

# 	# def getFilePath():
# 	# 	''' gets current filepath --> filepath '''
# 	# 	return getframeinfo(currentframe()).filename

# 	# def getRelativePath():
# 	# 	''' gets relative filepath for current file --> shortpath '''
# 	# 	return '/'.join(map(str,getFilePath().split('\\')[-2:]))

# 	# def getFileName():
# 	# 	''' gets filename for current file --> filename '''
# 	# 	return re.split("[/,.]+", getRelativePath())[1]

# # ''' ____ [NEW] EXPERIMENTAL: parse tablename & settings  ____________________________'''

# 	# def parseTablenames(file_name):
# 	# 	''' parses file specific tablename from settings --> settings'''
# 	# 	return tablenames[file_name]


# 	# def parseSettings(file_name):
# 	# 	''' parses file specific settings from settings --> settings'''
# 	# 	return settings[f'{file_name}_settings']

# #''' _________________________  MAIN _________________________'''
# 	# def main():
# 	# 	# NOTE: for some interesting dynamics -> consider using getRelativePath() from EXPERIMENTAL: Self Referance. 
# 	# 	file_name = getFileName()
# 	# 	# file_name = 'google' #self reference for parsing the correct settings

# 	# 	# calling parsers 
# 	# 	tablename = parseTablenames(file_name)
# 	# 	settings = parseSettings(file_name)
# 	# 	# specific parsing of settings:
# 	# 	chunk_size = settings['chunk_size']
# 	# 	print(chunk_size)
# 	# 	print(tablename)
# 	# 	print(settings)

# 	# if __name__ == '__main__':
# 	# 	main()
				
unit = {"organisasjonsnummer":"929616359",
		"navn":"VITAL JESSHEIM AS",
		"organisasjonsform":{"kode":"AS","beskrivelse":"Aksjeselskap","_links":{"self":{"href":"https://data.brreg.no/enhetsregisteret/api/organisasjonsformer/AS"}}},
		"registreringsdatoEnhetsregisteret":"2022-08-09",
		"registrertIMvaregisteret":false,
		"antallAnsatte":0,
		"forretningsadresse":{"land":"Norge","landkode":"NO","postnummer":"7020","poststed":"TRONDHEIM","adresse":["Mogstads vei 12A"],"kommune":"TRONDHEIM","kommunenummer":"5001"},
		"stiftelsesdato":"2022-07-31",
		"institusjonellSektorkode":{"kode":"2100","beskrivelse":"Private aksjeselskaper mv."},
		"registrertIForetaksregisteret":true,
		"registrertIStiftelsesregisteret":false,
		"registrertIFrivillighetsregisteret":false,
		"konkurs":false,"underAvvikling":false,
		"underTvangsavviklingEllerTvangsopplosning":false,
		"maalform":"Bokmål",
		"_links":{"self":{"href":"https://data.brreg.no/enhetsregisteret/api/enheter/929616359"}}}


# UNIT JSON
{"organisasjonsnummer":"995420678",
"navn":"MAGNA Tomasz Zmudka",
"organisasjonsform":{"kode":"ENK",
					"beskrivelse":"Enkeltpersonforetak",
					"_links":{"self":{"href":"https://data.brreg.no/enhetsregisteret/api/organisasjonsformer/ENK"}}},
"slettedato":"2022-08-09",
"_links":{"self":{"href":"https://data.brreg.no/enhetsregisteret/api/enheter/995420678"}}}


{'_embedded': {'oppdaterteEnheter': [{'_links': {'enhet': {'href': 'https://data.brreg.no/enhetsregisteret/api/enheter/995420678'}},
                                      'dato': '2022-08-09T04:01:36.478Z',
                                      'endringstype': 'Sletting',
                                      'oppdateringsid': 15184180,
                                      'organisasjonsnummer': '995420678'},


                                     {'_links': {'enhet': {'href': 'https://data.brreg.no/enhetsregisteret/api/enheter/915210678'}},
                                      'dato': '2022-08-09T04:01:36.478Z',
                                      'endringstype': 'Sletting',
                                      'oppdateringsid': 15184182,
                                      'organisasjonsnummer': '915210678'},
                                     {'_links': {'enhet': {'href': 'https://data.brreg.no/enhetsregisteret/api/enheter/925437115'}},
                                      'dato': '2022-08-09T04:01:36.478Z',
                                      'endringstype': 'Sletting',
                                      'oppdateringsid': 15184184,
                                      'organisasjonsnummer': '925437115'},
                                     {'_links': {'enhet': {'href': 'https://data.brreg.no/enhetsregisteret/api/enheter/967219517'}},
                                      'dato': '2022-08-09T04:01:36.479Z',
                                      'endringstype': 'Sletting',
                                      'oppdateringsid': 15184186,
                                      'organisasjonsnummer': '967219517'},
                                     {'_links': {'enhet': {'href': 'https://data.brreg.no/enhetsregisteret/api/enheter/992591188'}},
                                      'dato': '2022-08-09T04:01:36.479Z',
                                      'endringstype': 'Sletting',
                                      'oppdateringsid': 15184188,
                                      'organisasjonsnummer': '992591188'},
                                     {'_links': {'enhet': {'href': 'https://data.brreg.no/enhetsregisteret/api/enheter/993623830'}},
                                      'dato': '2022-08-09T04:01:36.479Z',
                                      'endringstype': 'Sletting',
                                      'oppdateringsid': 15184190,
                                      'organisasjonsnummer': '993623830'},
                                     {'_links': {'enhet': {'href': 'https://data.brreg.no/enhetsregisteret/api/enheter/927017687'}},
                                      'dato': '2022-08-09T04:01:36.479Z',
                                      'endringstype': 'Sletting',
                                      'oppdateringsid': 15184191,
                                      'organisasjonsnummer': '927017687'},
                                     {'_links': {'enhet': {'href': 'https://data.brreg.no/enhetsregisteret/api/enheter/926695649'}},
                                      'dato': '2022-08-09T04:01:36.479Z',
                                      'endringstype': 'Sletting',
                                      'oppdateringsid': 15184192,
                                      'organisasjonsnummer': '926695649'},
                                     {'_links': {'enhet': {'href': 'https://data.brreg.no/enhetsregisteret/api/enheter/928983137'}},
                                      'dato': '2022-08-09T04:01:36.479Z',
                                      'endringstype': 'Endring',
                                      'oppdateringsid': 15184194,
                                      'organisasjonsnummer': '928983137'},
                                     {'_links': {'enhet': {'href': 'https://data.brreg.no/enhetsregisteret/api/enheter/994784749'}},
                                      'dato': '2022-08-09T04:01:36.482Z',
                                      'endringstype': 'Endring',
                                      'oppdateringsid': 15184195,
                                      'organisasjonsnummer': '994784749'},
                                     {'_links': {'enhet': {'href': 'https://data.brreg.no/enhetsregisteret/api/enheter/920850022'}},
                                      'dato': '2022-08-09T04:01:36.487Z',
                                      'endringstype': 'Endring',
                                      'oppdateringsid': 15184197,
                                      'organisasjonsnummer': '920850022'},
                                     {'_links': {'enhet': {'href': 'https://data.brreg.no/enhetsregisteret/api/enheter/911600323'}},
                                      'dato': '2022-08-09T04:01:36.492Z',
                                      'endringstype': 'Sletting',
                                      'oppdateringsid': 15184201,
                                      'organisasjonsnummer': '911600323'},
                                     {'_links': {'enhet': {'href': 'https://data.brreg.no/enhetsregisteret/api/enheter/919083352'}},
                                      'dato': '2022-08-09T04:01:36.492Z',
                                      'endringstype': 'Sletting',
                                      'oppdateringsid': 15184203,
                                      'organisasjonsnummer': '919083352'},
                                     {'_links': {'enhet': {'href': 'https://data.brreg.no/enhetsregisteret/api/enheter/919622016'}},
                                      'dato': '2022-08-09T04:01:36.492Z',
                                      'endringstype': 'Sletting',
                                      'oppdateringsid': 15184205,
                                      'organisasjonsnummer': '919622016'},
                                     {'_links': {'enhet': {'href': 'https://data.brreg.no/enhetsregisteret/api/enheter/921441827'}},
                                      'dato': '2022-08-09T04:01:36.492Z',
                                      'endringstype': 'Sletting',
                                      'oppdateringsid': 15184207,
                                      'organisasjonsnummer': '921441827'},
                                     {'_links': {'enhet': {'href': 'https://data.brreg.no/enhetsregisteret/api/enheter/925089478'}},
                                      'dato': '2022-08-09T04:01:36.492Z',
                                      'endringstype': 'Sletting',
                                      'oppdateringsid': 15184209,
                                      'organisasjonsnummer': '925089478'},
                                     {'_links': {'enhet': {'href': 'https://data.brreg.no/enhetsregisteret/api/enheter/927838796'}},
                                      'dato': '2022-08-09T04:01:36.492Z',
                                      'endringstype': 'Sletting',
                                      'oppdateringsid': 15184211,
                                      'organisasjonsnummer': '927838796'},
                                     {'_links': {'enhet': {'href': 'https://data.brreg.no/enhetsregisteret/api/enheter/914165318'}},
                                      'dato': '2022-08-09T04:01:58.645Z',
                                      'endringstype': 'Endring',
                                      'oppdateringsid': 15184213,
                                      'organisasjonsnummer': '914165318'},
                                     {'_links': {'enhet': {'href': 'https://data.brreg.no/enhetsregisteret/api/enheter/969630613'}},
                                      'dato': '2022-08-09T04:01:58.649Z',
                                      'endringstype': 'Endring',
                                      'oppdateringsid': 15184215,
                                      'organisasjonsnummer': '969630613'},
                                     {'_links': {'enhet': {'href': 'https://data.brreg.no/enhetsregisteret/api/enheter/919399023'}},
                                      'dato': '2022-08-09T04:01:58.651Z',
                                      'endringstype': 'Endring',
                                      'oppdateringsid': 15184217,
                                      'organisasjonsnummer': '919399023'}]},
 '_links': {'first': {'href': 'https://data.brreg.no/enhetsregisteret/api/oppdateringer/enheter?dato=2022-08-09T00:00:00.000Z&page=0&size=20'},
            'last': {'href': 'https://data.brreg.no/enhetsregisteret/api/oppdateringer/enheter?dato=2022-08-09T00:00:00.000Z&page=412&size=20'},
            'next': {'href': 'https://data.brreg.no/enhetsregisteret/api/oppdateringer/enheter?dato=2022-08-09T00:00:00.000Z&page=1&size=20'},
            'self': {'href': 'https://data.brreg.no/enhetsregisteret/api/oppdateringer/enheter?dato=2022-08-09T00:00:00.000Z'}},
 'page': {'number': 0, 'size': 20, 'totalElements': 8249, 'totalPages': 413}}
