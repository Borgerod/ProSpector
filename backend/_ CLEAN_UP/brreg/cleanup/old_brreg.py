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

# ___ local imports ________
# from Config import payload  #Saving for later
# print(payload)

# Payload:
''' NB:  TEMPORARY CONFIG '''
payload = { 'dbname'   : 'media_vest',
			'host'     : 'localhost',
			'user'     : 'postgres',
			'password' : 'Orikkel1991',
			'tablename': 'brreg_table',  }


'''
	TODO:
	- [X] implement loop for getRequests()
	- [X] create multithreaded loop
	- [ ] finish Config
	- [ ] implement progressbar

'''

 


''' ___ PART 1, BBREG API  ____________________________________________________ '''

## OLD GETREQUEST()
# def getRequest():
# 	url = 'https://data.brreg.no/enhetsregisteret/api/enheter/?page=3&size=20' #-i -X GET
# 	r = requests.get(url, timeout=10)
# 	json = r.json()
# 	return json

# NEW GETREQUEST()
def getRequest(next_page):
	url = f'https://data.brreg.no/enhetsregisteret/api/enheter/?page={next_page}&size=20' #-i -X GET
	r = requests.get(url, timeout = 10)
	json = r.json()
	return json


def getpage(json):
	page =  json['page']
	return page

def getMaxpages(page):
	''' 
		gets the total number of pages from JSON, 
		used for breaking the loop 
	'''
	total_pages = page['totalPages']
	return total_pages

def gettotalElements(page):
	''' 
		Not used in code.
		gets the total number of elements (Companies) from JSON, 
		used for supervising & calculations
	'''
	total_elements = page['totalElements']
	return total_elements

def getCurrentpage(page):
	''' gets the current page from JSON '''
	current_page = page['number']
	return current_page

def getnext_page(current_page):
	next_page = current_page + 1
	return next_page

def getData(json):
	''' gets data from JSON '''
	data = json['_embedded']['enheter']
	return data	

def makeDataframe(data):
	''' makes dataframe from json '''
	df = pd.json_normalize(data)
	return df

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
	df = df.rename(columns = {	'organisasjonsnummer':'org_num',
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
	return df 

def apiManager(current_page):
	'''
		Manages the api from "Brønnøysynd registeret"
	'''
	json = getRequest(current_page)
	'''pages'''
	page = getpage(json)
	toal_pages = getMaxpages(page)
	current_page = getCurrentpage(page)	
	next_page = getnext_page(current_page)

	'''data'''
	data = getData(json)
	
	df = makeDataframe(data)
	df = datasetEditor(df)
	return df, toal_pages, current_page, next_page




# ''' ___ PART 2; POSTGRES  ____________________________________________________ 
# '''

# ''' ___ PREP _______________________________________________ '''
# def parseConfig():
# 	''' returns parsed payload from config file '''
# 	dbname = payload['dbname']
# 	host = payload['host']
# 	user = payload['user']
# 	password = payload['password']
# 	tablename = payload['tablename']
# 	return dbname, host, user, password, tablename

# def getCursor(conn):
# 	''' returns postgres cursor '''
# 	return conn.cursor()

# def getConnection():
# 	''' connects to database '''
# 	return psycopg2.connect(
# 		dbname = dbname, 
# 		host = host, 
# 		user = user, 
# 		password = password)

# ''' ___ ACTIONS _______________________________________________ '''
# def insertData(df):
# 	''' 
# 		inserts final dataframe to database, 
# 		creates new table if table it does not exsist, else it updates
# 	'''
# 	conn = getConnection()
# 	curr = getCursor(conn)
# 	dbname, host, user, password, tablename = parseConfig()
# 	engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:5432/{dbname}')
# 	df.to_sql(f'{tablename}', engine, if_exists = 'replace', index = False)

# def fetchData(conn, tablename):
# 	''' fetches old_df from database '''
# 	dbname, host, user, password, tablename = parseConfig()
# 	curr = getCursor(conn)  
# 	curr.execute(f"SELECT * FROM {tablename};") 
# 	old_data = curr.fetchall()
# 	column_names  = [desc[0] for desc in curr.description]
# 	old_df = pd.DataFrame(old_data, columns = column_names)
# 	curr.close()
# 	conn.close()
# 	return old_df
  
# def concatData(df, old_df):
# 	''' Concat old_df from database with new df from api request '''
# 	df.set_index(['org_num'],  inplace = True)
# 	try: 
# 		df.drop('org_num', axis = 1, inplace=True)
# 	except KeyError:
# 		pass
# 	old_df.set_index(old_df['org_num'].squeeze(), inplace = True)
# 	try: 
# 		old_df.drop('org_num', axis = 1, inplace=True)
# 	except KeyError:
# 		print("KeyError: old_df['org_num']")
# 	df = pd.concat((df, old_df), axis = 0)
# 	df = df.groupby(df.index).last().reset_index()
# 	return df

# ''' ___ MANAGER _______________________________________________ '''
# def databaseManager(df):
# 	''' manage database '''
# 	old_df = pd.DataFrame()
# 	try:
# 		conn = getConnection()
# 		old_df = fetchData(conn, tablename)
# 	except:
# 		print("table does not exsist")
# 	# try: 
# 	# 	df = concatData(df, old_df)
# 	# except:
# 	# 	print("unable to concat") 
# 	df = concatData(df, old_df)
# 	insertData(df)	


if __name__ == '__main__':
	print("_"*91)
	print("|											  |")
	print("|			Starting: Brønnøysund Register Extractor 			  |")
	print("|											  |")
	print("_"*91)
	print()

	''' preperations: parse config, connect to database and connect to api manager '''
	dbname, host, user, password, tablename = parseConfig()
	conn = getConnection()
	
	''' first run '''
	first_page = 0 
	df, toal_pages, current_page, next_page = apiManager(first_page)
	databaseManager(df)

	''' makes list of all page numbers '''
	# toal_pages = 30 #for testing
	all_pages = np.arange(next_page-1, toal_pages)

	''' Loop, rest of the pages '''
	with tqdm(total = toal_pages) as pbar:
		with concurrent.futures.ThreadPoolExecutor() as executor:
			results = executor.map(apiManager, all_pages)
			for result in results:
				databaseManager(result[0])
				pbar.update(1)	
	print("																		"+"_"*91)
	print("																		|											  |")
	print("																		|				   Data Extraction Complete. 				  |")
	print("																		|											  |")
	print("																		"+"_"*91)
	print()			
