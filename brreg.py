'''* TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP 
-							
-							_____ WHERE I LEFT OF _____
-						[10.08.22]
-						About to make an Update function 
-						ATM it seems like i need two seperate functions for "download whole dataset" and "update dataset"
-						

						! ISSUE:
						- in updateDataBase(tablename, settings, testmode,  action):
						- unable to do json = getRequest(url)

- TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP '''

import time; start = time.perf_counter() #Since it also takes time to Import libs, I allways start the timer asap. 
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

# ___ local imports __________
from config import payload, tablenames, settings
from postgres import databaseManager, cleanUp, fetchData, checkForTable, postLastUpdate
from file_manager import *

import json
import gzip
import pandas as pd 
import pprint
import ast


'''
TODO LIST:
	- [X] create downloader function 
	- [X] implement postgres code 
	- [ ] check if current version works 
	- [ ] Make Update function 
	- [ ] make documentation on "RUNDOWN OF THE PROGRAM", including what postgres.py does
	- [ ] make documentation on "NOTABLE FLAWS"
'''


''' * ____ API REQUEST ___________________________
'''
def getRequest(url):
	''' simple get request based on next_page -> json_dict '''
	# url = f'https://data.brreg.no/enhetsregisteret/api/enheter/?page=0&size=20'
	return (requests.get(url, timeout = 10)).json()

def getMaxpages(json_str):
	''' 
		gets the total number of pages from JSON, 
		used for breaking the loop 
	'''
	total_pages = json_str['page']['totalPages']
	return total_pages

def getCurrentpage(json_str):
	''' gets the current json_str from JSON -> current_page'''
	return json_str['page']['number']

def getnext_page(current_page):
	''' makes next_page from current_page '''
	return current_page + 1

def gettotalElements(json_str):
	''' 
		Not used in code.
		gets the total number of elements (Companies) from JSON, 
		used for supervising & calculations
		-> total_elements
	'''
	return json_str['page']['totalElements']

def getData(json):
	''' gets data from JSON '''
	data = json['_embedded']['oppdaterteEnheter']
	return data	

def makeDataframe(data):
	''' makes dataframe from json '''
	df = pd.json_normalize(data)
	return df

''' * ____ API REQUEST ___________________________
'''


# FIXME: [TEMP DISABLED] UpdateDataBase()
# def apiManager(current_page):
	# '''
	# 	Manages the api from "Brønnøysynd registeret"
	# '''
	# tablename = getTableName()
	# json = getRequest(current_page)
	# '''pages'''
	# # page = getpage(json)
	# page = getpage(json, current_page) #FIXME --> TEMP while testing
	# total_pages = getMaxpages(page)
	# current_page = getCurrentpage(page)	
	# next_page = getnext_page(current_page)

	# '''data'''
	# # data = getData(json)
	# # df = makeDataframe(data)
	# # df = datasetEditor(df)


	# # TODO: Consider using for loop, e.g. for i in total_pages:
	# next_result = 0
	# while next_result == 0:
	# 	try:
	# 		databaseManager(df, tablename)
	# 		next_result = 1
	# 	# ! REMEBER: you must  account for the api limit 
	# 	except:
	# 		continue
	# 	break
	# return df, total_pages, current_page, next_page

# ! MOVED TO POSTGRES.PY
	# def checkLastUpdate(): #TODO: Finish this.
	# 	# '''
	# 	# 	checks for last date a update occoured, 
	# 	# 	returns parameter "oppdateringsid"
	# 	# '''
	# 	# last_update = None  #Date 


	# 	# # select relfilenode from pg_class where relname = 'test';

	# 	# return last_update


def getLastUpdate(tablename):
	df = fetchData(tablename = 'update_tracker')
	return dt.strptime( df.to_dict()[tablename][0])


def manageUpdateData(unit):
	'''
		parse relevant data from unit
	'''
	url = unit['_links']['enhet']['href']
	change_type = unit['endringstype']
	org_num = unit['organisasjonsnummer']

	''' LIST OF CHANGE_TYPE:
		- Ny
		- Endring
		- Sletting
		- Fjernet
	'''	
	if change_type == 'Ukjent':
		addUnit(org_num, url)
	if change_type == 'Ny':
		addUnit(org_num, url)
	if change_type == 'Endring':
		addUnit(org_num, url)
	if change_type == 'Sletting':
		Command.deleteUnit(org_num)
	if change_type == 'Fjernet':
		Command.deleteUnit(org_num)

class Command:
	
	def addUnit(org_num, url):
		data = getRequest(url)
		df = datasetEditor(jsonDataframe(data))
		df = df.drop('_links.self.href', axis = 1)
		databaseManager(df, tablename = getTableName())

	def deleteUnit(org_num):
		# TODO: [INSERT SQLALCHEMY OR PSYCOG2 CODE]
		deleteData(org_num, tablename = getTableName())

	#! replaced with addUnit()
	# def changeUnit(org_num, url):
		# # TODO: [INSERT SQLALCHEMY OR PSYCOG2 CODE]
		# data = getRequest(url)
		# df = datasetEditor(jsonDataframe(data))
		# df = df.drop('_links.self.href', axis = 1)
		# databaseManager(df, tablename = getTableName())






def updateAPI(base_url, page_num, tablename):
	print(f'MOCK "updateAPI": {page_num}')
	# url = f'{base_url}dato={getLastUpdate(tablename)}T00:00:00.000Z&page={page_num}&size=20'
	# # url = 'https://data.brreg.no/enhetsregisteret/api/oppdateringer/enheter?dato=2022-08-09T00:00:00.000Z' #FIXME: [TEMP] while testing
	# last_update = checkLastUpdate()
	# json_str = getRequest(url)
	# # import pprint
	# # pprint.pprint(json_str)

	# units = list(json_str['_embedded']['oppdaterteEnheter'])

	# # ? not sure which of these i need yet
	# current_page = getCurrentpage(json_str)
	# next_page = getnext_page(current_page)
	# total_pages = getMaxpages(json_str)
	
	# ''' Loop, rest of the pages '''
	# with concurrent.futures.ThreadPoolExecutor() as executor:
	# 	list(executor.map(manageUpdateData, units))





	


	# #? next_url = json_str['_embedded']['_links']['next']   #Not Sure if fast enough

	# # ! EDIT THESE 
	# manageUpdateData(json_str)
	# # df = makeDataframe(data)
	# # df = datasetEditor(df)





	# # databaseManager(df, tablename)

	# '''* update-url examples:
	# 	get all updates (today):
	# 		'https://data.brreg.no/enhetsregisteret/api/oppdateringer/enheter'
		
	# 	*	[USing THIS ONE] get all updates after a certain date:
	# 		'https://data.brreg.no/enhetsregisteret/api/oppdateringer/enheter?dato=2010-01-03T00:00:00.000Z'
		
	# 	get all updates after a certain update_time 
	# 		'https://data.brreg.no/enhetsregisteret/api/oppdateringer/enheter?oppdateringsid=2'
	# '''

	# # ? not sure if loop is needed 
	# 	# ''' TODO: implement if statement: 
	# 	# 	- if totalElements > 10000:
	# 	# 	-	actionDecider(table_exist=False, testmode, tablename)
	# 	# '''

	# 	# # * [NEW LOOP]
	# 	# for i in range(0, total_pages-1):
	# 	# 	databaseManager(df, tablename)


	# 	# # TODO: [OLD LOOP] Consider using for loop, e.g. for i in total_pages:
	# 	# next_result = 0
	# 	# while next_result == 0:
	# 	# 	try:
	# 	# 		databaseManager(df, tablename)
	# 	# 		next_result = 1
	# 	# 	# ! REMEBER: you must  account for the api limit 
	# 	# 	except:
	# 	# 		continue
	# 	# 	break	
	# return df, total_pages, current_page, next_page




def updateDataBase(tablename, settings, testmode,  action):
	# total_elements = gettotalElements() #[usage: tqdm & loop(could be)] gets total elements of dataset from api
	print("_"*91)
	if testmode:
		print("|			Updating: Brønnøysund Register (TESTMODE) 			  |")
	else:
		print("|			Updating: Brønnøysund Register 			  |")
	print("_"*91)
	print()		
	url = f'https://data.brreg.no/enhetsregisteret/api/{action}'

	
	# ''' first run '''
	# df, total_pages, current_page, next_page = apiManager(current_page = 0)

	# #? not sure if needed 
	# 	# ''' temporary code for testing '''
	# 	# if testmode == "on":
	# 	# 	total_pages = 1

	# ''' makes list of all page numbers '''
	# all_pages = np.arange(0, )
	



	json = getRequest(url)
	import pprint
	pprint(json)
	# max_pages =  getMaxpages()
	# print(max_pages)
	# print(f'amount of pages to scrape = {len(all_pages)}')

	# print(f"amount of elements to scrape = {gettotalElements(json_str)}")






	# if gettotalElements(json_str) > 10000:
	# 	actionDecider(table_exist = False, testmode=testmode, tablename=tablename)
	# else:
	# 	''' Loop, rest of the pages '''
	# 	with concurrent.futures.ThreadPoolExecutor() as executor:
	# 		list(tqdm(executor.map(updateAPI, all_pages, tablename), total = all_pages[-1] ))
	
	# print("cleaning database..")
	# cleanUp()
	# print("    cleaning complete")

	# print("_"*91)
	# print(f"|			Update Complete. 			  |")
	# print(f"|			Finished in {round(time.perf_counter() - start, 2)} second(s)				  |")
	# print("_"*91)
	# print()

''' * ____ DOWNLOAD JSONFILE _____________________
'''
def downloadJSON(json_file_name, url):
	with open('enheter_alle.json.gz', 'wb') as out_file:
		content = requests.get(url, stream=True).content
		out_file.write(content)

# TODO : example of download with TQDM
# def download_file(url, filename):
    # """
    # Helper method handling downloading large files from `url` to `filename`. Returns a pointer to `filename`.
    # """
    # chunkSize = 1024
    # r = requests.get(url, stream=True)
    # with open(filename, 'wb') as f:
    #     pbar = tqdm( unit="B", total=int( r.headers['Content-Length'] ) )
    #     for chunk in r.iter_content(chunk_size=chunkSize): 
    #         if chunk: # filter out keep-alive new chunks
    #             pbar.update (len(chunk))
    #             f.write(chunk)
    # return filename

''' * ____  MAKE DATAFRAME  _______________________
'''
def jsonDataframe(data):
	''' normalized json data and makes dataframe '''
	try: 
		return pd.read_json(data)
	except:									#! this might be unnessasary 
		return pd.json_normalize(data)		#! this might be unnessasary

def datasetEditor(df):
	'''
		drops columns not in keep_list, then renames columns from BRREG dataset  
	'''
	keep_list = np.array([	'organisasjonsnummer', 'navn', 'registreringsdatoEnhetsregisteret',
							'registrertIMvaregisteret', 'antallAnsatte', 'stiftelsesdato',
							'registrertIForetaksregisteret', 'registrertIStiftelsesregisteret',
							'registrertIFrivillighetsregisteret', 'sisteInnsendteAarsregnskap',
							'konkurs', 'underAvvikling',
							'underTvangsavviklingEllerTvangsopplosning', 'maalform',
							'organisasjonsform.kode', 'organisasjonsform.beskrivelse',
							'organisasjonsform._links.self.href', 'naeringskode1.beskrivelse',
							'naeringskode1.kode', 'forretningsadresse.land',
							'forretningsadresse.landkode', 'forretningsadresse.postnummer',
							'forretningsadresse.poststed', 'forretningsadresse.adresse',
							'forretningsadresse.kommune', 'forretningsadresse.kommunenummer',
							'institusjonellSektorkode.kode', 'institusjonellSektorkode.beskrivelse',
							'_links.self.href', 'postadresse.land', 'postadresse.landkode',
							'postadresse.postnummer', 'postadresse.poststed', 'postadresse.adresse',
							'postadresse.kommune', 'postadresse.kommunenummer', 'hjemmeside',])
	df = df[df.columns.intersection(keep_list)]
	return df.rename(columns = {	'organisasjonsnummer':'org_num',
									'navn':'navn',
									'registreringsdatoEnhetsregisteret':'registreringsdato',
									'registrertIMvaregisteret':'mva_registrert',
									'antallAnsatte':'antall_ansatte',
									'registrertIForetaksregisteret':'foretaks_registeret',
									'registrertIStiftelsesregisteret':'stiftelses_registeret',
									'registrertIFrivillighetsregisteret':'frivillighets_registeret',
									'konkurs':'konkurs',
									'underAvvikling':'under_avvikling',
									'underTvangsavviklingEllerTvangsopplosning':'under_tvangsavvikling_eller_oppløsning',
									'organisasjonsform.kode':'organisasjonsform_kode',
									'organisasjonsform.beskrivelse':'organisasjonsform_beskrivelse',
									'naeringskode1.beskrivelse':'naeringskode1_beskrivelse',
									'naeringskode1.kode':'naeringskode1_kode',
									'forretningsadresse.land':'land',
									'forretningsadresse.landkode':'landkode',
									'forretningsadresse.postnummer':'postnummer',
									'forretningsadresse.poststed':'poststed',
									'forretningsadresse.adresse':'adresse',
									'forretningsadresse.kommune':'kommune',
									'forretningsadresse.kommunenummer':'kommunenummer',
									'institusjonellSektorkode.kode':'sektorkode_kode',
									'institusjonellSektorkode.beskrivelse':'sektorkode_beskrivelse',
									'hjemmeside':'hjemmeside',
									'stiftelsesdato':'stiftelsesdato',
									'sisteInnsendteAarsregnskap':'siste_innsendt_årsregnskap',})


# FIXME: [TEMP DISABLED] 


# [TRASH]
	# 	# df = updateAPI(url)
	# 	# print(f'{df}\n')	
	# 	# print("    dataframe complete")
	# 	# print()


	# 	# ''' * ANNBEFALING FRA BRREG IHT OPPDATERING
	# 	# 	Vi anbefaler følgende bruk: Filtrer på dato for første gangs uthenting, slik at man unngår enheter tidligere enn eventuell siste kopi. 
	# 	# 	Filtrer så på updateid for å hente neste sett av resultater. (Her kan man trygt bruke updateid+1). 
	# 	# 	Page+size kan benyttes for mer presis navigering i en updateid- eller dato-spørring.
		
	# 	# 	PAGINERING
	# 	# 		Det er mulig å filtrere og bla gjennom resultatsettet via page+size, dato og/eller updateid, men med visse begrensninger. 
	# 	# 		(Page+1)*size kan ikke overskride 10 000 og det kan finnes flere elementer med samme dato. Updateid kan bare forekomme en gang, 
	# 	# 		men disse er gjenbrukt på tvers av underenheter og enheter og kan ha gap på flere tusen id’er.
	# 	# '''


	# 	# print("making dataframe..")
	# 	# data = json_file_name #FIXME --> [TEMP] while testing
	# 	# df = jsonDataframe(data = json_file_name)
	# 	# print(f'{df}\n')	
	# 	# print("    dataframe complete")
	# 	# print()

	# 	# print("editing dataframe..")
	# 	# df = datasetEditor(df)
	# 	# print(f'{df}\n')	
	# 	# print("    editing complete")
	# 	# print()
		
	# 	# print("uploading to database..")
	# 	# databaseManager(df, tablename)
	# 	# print('    upload complete')
	# 	# print()

	# 	# print(f'Display results:\n\n{df}\n\n')
	# 	# db_table = fetchData(tablename)
	# 	# print(f'{db_table}\n')	
	# 	# print()

	# 	# # cleanup; check for duplicates
	# 	# # TODO: insert this 
	# 	# print("_"*91)
	# 	# print(f"|			Update Complete. 			  |")
	# 	# print(f"|			Finished in {round(time.perf_counter() - start, 2)} second(s)				  |")
	# 	# print("_"*91)
	# 	# print()


def downloadWholeDataset(tablename, testmode, json_file_name, action):
	print("_"*91)
	if testmode:
		print("|			Starting: Brønnøysund Register Extractor (TESTMODE) 			  |")
	else:
		print("|			Starting: Brønnøysund Register Extractor 			  |")
	print("_"*91)
	print()	

	#! [not in use] [usage: tqdm]
	# total_elements = gettotalElements() # gets total elements of dataset from api 
	url = f'https://data.brreg.no/enhetsregisteret/api/{action}'
	
	#FIXME --> [TEMP] DISABLED  while testing
	# print("downloading file..")
	# downloadJSON(json_file_name, url)
	# print("    downloading complete") 

	print("making dataframe..")
	df = jsonDataframe(data = json_file_name)
	print(f'{df}\n')	
	print("    dataframe complete")
	print()

	print("editing dataframe..")
	df = datasetEditor(df)
	print(f'{df}\n')	
	print("    editing complete")
	print()
	
	print("uploading to database..")
	databaseManager(df, tablename)
	print('    upload complete')
	print()

	print(f'Display results:\n\n{df}\n\n')
	db_table = fetchData(tablename)
	print(f'{db_table}\n')	
	print()

	# cleanup; check for duplicates
	# TODO: insert this 
	print("cleaning database..")
	cleanUp()
	print("    cleaning complete")
	
	# missing values; 
	# TODO: need if statement for when database is empty

	print("_"*91)
	print(f"|			Update Complete. 			  |")
	print(f"|			Finished in {round(time.perf_counter() - start, 2)} second(s)				  |")
	print("_"*91)
	print()

def actionDecider(table_exist, testmode, tablename):
	if table_exist:
		settings = parseSettings(getFileName())	#fetches the appropriate settings for current file
		updateDataBase(tablename, settings, testmode, action = 'enheter/lastned')
		# print(" STAND-IN for updateDataBase() ")		
	else:
		downloadWholeDataset(tablename, testmode, json_file_name, action = 'oppdateringer/enheter')

# TODO: should be exported to file_manager.py
def getTableName():
	return parseTablenames(getFileName())

''' * ____  MAIN  ________________________________
'''
def brregExtractor(testmode):
	# current_file_name = getFileName()	# fetches name of current file 
	tablename = getTableName() # fetches the appropriate tablename for current file

	''' Decide wether to download or update
		Checks if table exsist, then builds the propriate url for api '''
	if testmode:
		json_file_name = 'enheter_alle_snippet.json.gz'
	else: 
		json_file_name = 'enheter_alle.json.gz'
	
	''' Decide wether to download or update
		Checks if table exsist, then builds the propriate url for api '''
	table_exist = checkForTable(tablename) 
	actionDecider(table_exist, testmode, tablename)
	# postLastUpdate(tablename)




# FIXME: [TEMP] while testing
if __name__ == '__main__':			# FIXME: STAND IN FOR main() in main.py
	brregExtractor(testmode = False)

















''' [OLD] '''
	# total_elements = gettotalElements() # gets total elements of dataset from api 
	# json_file_name = 'enheter_alle.json.gz' #FIXME --> TEMP while testing
	# # FIXME [DISABLED while testing] downloadJSON()
	# 	# print("downloading file..")
	# 	# downloadJSON(json_file_name)	# DISABLED
	# 	# print("    downloading complete")
	# # ?  [TEMP CUT OUT] readDataset() [might not be needed]
	# 	# print("reading dataset..")
	# 	# data = readDataset(json_file = json_file_name)
	# 	# print("    reading complete")
	

	# print("making dataframe..")
	# data = json_file_name #FIXME --> TEMP while testing
	# df = jsonDataframe(data)
	# print(df)
	# print("    dataframe complete")
	

	# print("uploading to database..")
	# databaseManager(df, tablename)
	# print('    upload complete')


	# # ?  [TEMP CUT OUT] cleanUp() [might not be needed]
	# 	# print("cleaning table..")
	# 	# cleanUp(tablename)
	# 	# print("    cleaning complete")
	

	# print(f'Display results:\n\n{df}\n\n')
	# db_table = fetchData(tablename)
	# print(db_table)	
	# print(f'|				   Finished in: {round(time.perf_counter() - start, 2)} second(s)				  |')

 # OUTPUT FROM CURRENT RUN [11.08.2022]:
		# C:\Users\Big Daddy B\OneDrive\GitHub\Mediavest_Scraper_bot>python brreg.py
		# False
		# enheter_alle.json.gz
		# checking if brreg_table exists:
		#     table; brreg_table exist
		# table_exists = True
		#  STAND-IN for updateDataBase()

		# C:\Users\Big Daddy B\OneDrive\GitHub\Mediavest_Scraper_bot>python brreg.py
		# False
		# enheter_alle.json.gz
		# checking if brreg_table exists:
		#     Error: table brreg_table does not exist
		# table_exists = False
		# ___________________________________________________________________________________________
		# |                       Starting: Brønnøysund Register Extractor                          |
		# ___________________________________________________________________________________________

		# making dataframe..
		#          organisasjonsnummer                                               navn                                  organisasjonsform  ... frivilligMvaRegistrertBeskrivelser  overordnetEnhet naeringskode3
		# 0                  922924368  - A THOUSAND WORDS - ØDEGÅRDEN GJERRUD TRANSLA...  {'kode': 'ENK', 'beskrivelse': 'Enkeltpersonfo...  ...                                NaN              NaN           NaN
		# 1                  911963582                - TTT- WINES TORE EUGEN KRISTIANSEN  {'kode': 'ENK', 'beskrivelse': 'Enkeltpersonfo...  ...                                NaN              NaN           NaN
		# 2                  988539473                              -EBE- DATA Eyolf Berg  {'kode': 'ENK', 'beskrivelse': 'Enkeltpersonfo...  ...                                NaN              NaN           NaN
		# 3                  913460197                                          -MINUS AS  {'kode': 'AS', 'beskrivelse': 'Aksjeselskap', ...  ...                                NaN              NaN           NaN
		# 4                  922936919                 -VEIEN- MED ANITA HELLEBØ-STOREIDE  {'kode': 'ENK', 'beskrivelse': 'Enkeltpersonfo...  ...                                NaN              NaN           NaN
		# ...                      ...                                                ...                                                ...  ...                                ...              ...           ...
		# 1077928            998858135                                    OLAV LILLESKARE  {'kode': 'ENK', 'beskrivelse': 'Enkeltpersonfo...  ...                                NaN              NaN           NaN
		# 1077929            995928825                                         POLYBOS AS  {'kode': 'AS', 'beskrivelse': 'Aksjeselskap', ...  ...                                NaN              NaN           NaN
		# 1077930            996001997                                    PRESTEGÅRDEN AS  {'kode': 'AS', 'beskrivelse': 'Aksjeselskap', ...  ...     [Utleier av bygg eller anlegg]              NaN           NaN
		# 1077931            998195675  RAYMA AGENTURER, SUKKERSPINNBODEN.NO RAYMOND M...  {'kode': 'ENK', 'beskrivelse': 'Enkeltpersonfo...  ...                                NaN              NaN           NaN
		# 1077932            999590985                                    SAKURA SUSHI AS  {'kode': 'AS', 'beskrivelse': 'Aksjeselskap', ...  ...                                NaN              NaN           NaN

		# [1077933 rows x 25 columns]

		#     dataframe complete

		# editing dataframe..
		#            org_num                                               navn registreringsdato  mva_registrert  ...  maalform             hjemmeside  stiftelsesdato  siste_innsendt_årsregnskap
		# 0        922924368  - A THOUSAND WORDS - ØDEGÅRDEN GJERRUD TRANSLA...        2019-06-19            True  ...    Bokmål                    NaN             NaN                         NaN
		# 1        911963582                - TTT- WINES TORE EUGEN KRISTIANSEN        2013-05-25           False  ...    Bokmål                    NaN             NaN                         NaN
		# 2        988539473                              -EBE- DATA Eyolf Berg        2005-08-20           False  ...    Bokmål       www.ebe-data.com             NaN                         NaN
		# 3        913460197                                          -MINUS AS        2014-04-03            True  ...    Bokmål                    NaN      2014-03-05                      2020.0
		# 4        922936919                 -VEIEN- MED ANITA HELLEBØ-STOREIDE        2019-06-21           False  ...    Bokmål                    NaN             NaN                         NaN
		# ...            ...                                                ...               ...             ...  ...       ...                    ...             ...                         ...
		# 1077928  998858135                                    OLAV LILLESKARE        2012-09-20            True  ...   Nynorsk                    NaN             NaN                         NaN
		# 1077929  995928825                                         POLYBOS AS        2010-10-23            True  ...    Bokmål                    NaN      2010-10-01                      2021.0
		# 1077930  996001997                                    PRESTEGÅRDEN AS        2010-09-30           False  ...    Bokmål  www.tuneprestegard.no      2010-09-01                      2019.0
		# 1077931  998195675  RAYMA AGENTURER, SUKKERSPINNBODEN.NO RAYMOND M...        2012-04-02           False  ...    Bokmål                    NaN             NaN                         NaN
		# 1077932  999590985                                    SAKURA SUSHI AS        2013-01-28           False  ...    Bokmål                    NaN      2013-01-01                      2019.0

		# [1077933 rows x 15 columns]

		#     editing complete

		# uploading to database..
		#     upload complete

		# Display results:

		#            org_num                                               navn registreringsdato  mva_registrert  ...  maalform             hjemmeside  stiftelsesdato  siste_innsendt_årsregnskap
		# 0        922924368  - A THOUSAND WORDS - ØDEGÅRDEN GJERRUD TRANSLA...        2019-06-19            True  ...    Bokmål                    NaN             NaN                         NaN
		# 1        911963582                - TTT- WINES TORE EUGEN KRISTIANSEN        2013-05-25           False  ...    Bokmål                    NaN             NaN                         NaN
		# 2        988539473                              -EBE- DATA Eyolf Berg        2005-08-20           False  ...    Bokmål       www.ebe-data.com             NaN                         NaN
		# 3        913460197                                          -MINUS AS        2014-04-03            True  ...    Bokmål                    NaN      2014-03-05                      2020.0
		# 4        922936919                 -VEIEN- MED ANITA HELLEBØ-STOREIDE        2019-06-21           False  ...    Bokmål                    NaN             NaN                         NaN
		# ...            ...                                                ...               ...             ...  ...       ...                    ...             ...                         ...
		# 1077928  998858135                                    OLAV LILLESKARE        2012-09-20            True  ...   Nynorsk                    NaN             NaN                         NaN
		# 1077929  995928825                                         POLYBOS AS        2010-10-23            True  ...    Bokmål                    NaN      2010-10-01                      2021.0
		# 1077930  996001997                                    PRESTEGÅRDEN AS        2010-09-30           False  ...    Bokmål  www.tuneprestegard.no      2010-09-01                      2019.0
		# 1077931  998195675  RAYMA AGENTURER, SUKKERSPINNBODEN.NO RAYMOND M...        2012-04-02           False  ...    Bokmål                    NaN             NaN                         NaN
		# 1077932  999590985                                    SAKURA SUSHI AS        2013-01-28           False  ...    Bokmål                    NaN      2013-01-01                      2019.0

		# [1077933 rows x 15 columns]


		#            org_num                                               navn registreringsdato  mva_registrert  ...  maalform             hjemmeside  stiftelsesdato  siste_innsendt_årsregnskap
		# 0        922924368  - A THOUSAND WORDS - ØDEGÅRDEN GJERRUD TRANSLA...        2019-06-19            True  ...    Bokmål                   None            None                         NaN
		# 1        911963582                - TTT- WINES TORE EUGEN KRISTIANSEN        2013-05-25           False  ...    Bokmål                   None            None                         NaN
		# 2        988539473                              -EBE- DATA Eyolf Berg        2005-08-20           False  ...    Bokmål       www.ebe-data.com            None                         NaN
		# 3        913460197                                          -MINUS AS        2014-04-03            True  ...    Bokmål                   None      2014-03-05                      2020.0
		# 4        922936919                 -VEIEN- MED ANITA HELLEBØ-STOREIDE        2019-06-21           False  ...    Bokmål                   None            None                         NaN
		# ...            ...                                                ...               ...             ...  ...       ...                    ...             ...                         ...
		# 1077928  998858135                                    OLAV LILLESKARE        2012-09-20            True  ...   Nynorsk                   None            None                         NaN
		# 1077929  995928825                                         POLYBOS AS        2010-10-23            True  ...    Bokmål                   None      2010-10-01                      2021.0
		# 1077930  996001997                                    PRESTEGÅRDEN AS        2010-09-30           False  ...    Bokmål  www.tuneprestegard.no      2010-09-01                      2019.0
		# 1077931  998195675  RAYMA AGENTURER, SUKKERSPINNBODEN.NO RAYMOND M...        2012-04-02           False  ...    Bokmål                   None            None                         NaN
		# 1077932  999590985                                    SAKURA SUSHI AS        2013-01-28           False  ...    Bokmål                   None      2013-01-01                      2019.0

		# [1077933 rows x 15 columns]


		# |                                  Finished in: 84.96 second(s)                           |


''' [OLD] if __name__ == '__main__': 

	file_name = getFileName()	# fetches name of current file 
	tablename = parseTablenames(file_name) # fetches the appropriate tablename for current file
	settings = parseSettings(file_name)	# fetches the appropriate settings for current file

	total_elements = gettotalElements()
	
	json_file_name = 'enheter_alle.json.gz' #FIXME --> TEMP while testing
	print("downloading file..")
	# downloadJSON(json_file_name)	# DISABLED
	print("    downloading complete")
	print("reading dataset..")
	data = readDataset(json_file = json_file_name)
	print("    reading complete")
	print("making dataframe..")
	# tqdm.pandas(desc = 'making dataframe:') 
	data = json_file_name #FIXME --> TEMP while testing
	df = jsonDataframe(data)
	print(df)
	# df.progress_apply(lambda x: x**2)
	print("    dataframe complete")
	print("uploading to database..")
	databaseManager(df, tablename)
	print("    upload complete")
	print("cleaning table..")
	# cleanUp(tablename)
	print("    cleaning complete")
	print(df) #FIXME --> TEMP while testing
	print(f"|				   Finished in< {round(time.perf_counter() - start, 2)} second(s)				  |")


	df = fetchData(tablename)
	print(df)
'''




