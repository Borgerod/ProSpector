# import time; start = time.perf_counter() #Since it also takes time to Import libs, I allways start the timer asap. 
# import os
# import re
# import string
# import pandas as pd
# import numpy as np
# from os import path
# from tqdm import tqdm
# import concurrent.futures
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from inspect import currentframe, getframeinfo
# import json
# import psycopg2
# from psycopg2.extras import Json
# from sqlalchemy import create_engine
# from tqdm import tqdm
# import pandas as pd 
# import requests 
# from bs4 import BeautifulSoup
# import numpy as np
# import pandas as pd 
# import json
# import psycopg2
# from psycopg2.extras import Json
# from sqlalchemy import create_engine
# import concurrent.futures
# from tqdm import tqdm


# def getRequest(url='https://data.brreg.no/enhetsregisteret/api/enheter/929616359'):
# 	''' simple get request based on next_page -> json_dict '''
# 	# url = f'https://data.brreg.no/enhetsregisteret/api/enheter/?page=0&size=20'
# 	return (requests.get(url, timeout = 10)).json()


# def datasetEditor(df):
# 	'''
# 		drops columns not in keep_list, then renames columns from BRREG dataset  
# 	'''
# 	keep_list = np.array([	'organisasjonsnummer', 'navn', 'registreringsdatoEnhetsregisteret',
# 							'registrertIMvaregisteret', 'antallAnsatte', 'stiftelsesdato',
# 							'registrertIForetaksregisteret', 'registrertIStiftelsesregisteret',
# 							'registrertIFrivillighetsregisteret', 'sisteInnsendteAarsregnskap',
# 							'konkurs', 'underAvvikling',
# 							'underTvangsavviklingEllerTvangsopplosning', 'maalform',
# 							'organisasjonsform.kode', 'organisasjonsform.beskrivelse',
# 							'organisasjonsform._links.self.href', 'naeringskode1.beskrivelse',
# 							'naeringskode1.kode', 'forretningsadresse.land',
# 							'forretningsadresse.landkode', 'forretningsadresse.postnummer',
# 							'forretningsadresse.poststed', 'forretningsadresse.adresse',
# 							'forretningsadresse.kommune', 'forretningsadresse.kommunenummer',
# 							'institusjonellSektorkode.kode', 'institusjonellSektorkode.beskrivelse',
# 							'_links.self.href', 'postadresse.land', 'postadresse.landkode',
# 							'postadresse.postnummer', 'postadresse.poststed', 'postadresse.adresse',
# 							'postadresse.kommune', 'postadresse.kommunenummer', 'hjemmeside',])
# 	df = df[df.columns.intersection(keep_list)]
# 	return df.rename(columns = {	'organisasjonsnummer':'org_num',
# 									'navn':'navn',
# 									'registreringsdatoEnhetsregisteret':'registreringsdato',
# 									'registrertIMvaregisteret':'mva_registrert',
# 									'antallAnsatte':'antall_ansatte',
# 									'registrertIForetaksregisteret':'foretaks_registeret',
# 									'registrertIStiftelsesregisteret':'stiftelses_registeret',
# 									'registrertIFrivillighetsregisteret':'frivillighets_registeret',
# 									'konkurs':'konkurs',
# 									'underAvvikling':'under_avvikling',
# 									'underTvangsavviklingEllerTvangsopplosning':'under_tvangsavvikling_eller_oppløsning',
# 									'organisasjonsform.kode':'organisasjonsform_kode',
# 									'organisasjonsform.beskrivelse':'organisasjonsform_beskrivelse',
# 									'naeringskode1.beskrivelse':'naeringskode1_beskrivelse',
# 									'naeringskode1.kode':'naeringskode1_kode',
# 									'forretningsadresse.land':'land',
# 									'forretningsadresse.landkode':'landkode',
# 									'forretningsadresse.postnummer':'postnummer',
# 									'forretningsadresse.poststed':'poststed',
# 									'forretningsadresse.adresse':'adresse',
# 									'forretningsadresse.kommune':'kommune',
# 									'forretningsadresse.kommunenummer':'kommunenummer',
# 									'institusjonellSektorkode.kode':'sektorkode_kode',
# 									'institusjonellSektorkode.beskrivelse':'sektorkode_beskrivelse',
# 									'hjemmeside':'hjemmeside',
# 									'stiftelsesdato':'stiftelsesdato',
# 									'sisteInnsendteAarsregnskap':'siste_innsendt_årsregnskap',})


# def makeDataframe(data):
# 	''' makes dataframe from json '''
# 	df = pd.json_normalize(data)
# 	return df

# def jsonDataframe(data):
# 	''' normalized json data and makes dataframe '''
# 	try: 
# 		return pd.read_json(data)
# 	except:									#! this might be unnessasary 
# 		return pd.json_normalize(data)		#! this might be unnessasary

# data = getRequest()
# df = datasetEditor(jsonDataframe(data))
# df = df.drop('_links.self.href', axis = 1)

dbname = 'media_vest'
host = 'localhost'
user = 'postgres'
password = 'Orikkel1991'

from sqlalchemy import delete, create_engine
import pandas as pd 
import psycopg2


def parseConfig():
	''' returns parsed payload from config file '''
	payload = { 	'dbname'   : 'media_vest',
				'host'     : 'localhost',
				'user'     : 'postgres',
				'password' : 'Orikkel1991',  }	


	dbname = payload['dbname']
	host = payload['host']
	user = payload['user']
	password = payload['password']
	return dbname, host, user, password

def getCursor(conn):
	''' returns postgres cursor '''
	return conn.cursor()

def getConnection():
	dbname, host, user, password = parseConfig()
	''' connects to database '''
	return psycopg2.connect(
		dbname = dbname, 
		host = host, 
		user = user, 
		password = password)


def deleteData(org_num, tablename):
	conn = getConnection()
	curr = getCursor(conn)
	curr.execute(f"""DELETE FROM public.{tablename} WHERE "user" = '{org_num}'""")
	# f""" DELETE {tablename}
 #                WHERE 'user' = '{org_num}'""")
	conn.commit()
	curr.close()



test_table = 'test_table'
df = pd.DataFrame([['patrick', '19'],['alex', '19']], columns = ['user', 'age'])
print(df)
engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:5432/{dbname}')
df.to_sql(f'{test_table}', engine, if_exists = 'replace', index = False)


# stmt = delete(test_table).where(test_table.c.user == 'patrick')
# print(stmt)
# d = addresses_table.delete().where(addresses_table.c.retired == 1)
# d.execute()

deleteData(org_num='patrick', tablename = 'test_table')

def fetchData(tablename):
	''' 
		desc: fetches old_df from database
		reason: needed for replaceData() & [OLD] insertData()
	'''
	dbname, host, user, password = parseConfig()
	conn = getConnection()
	curr = getCursor(conn)  
	curr.execute(f"SELECT * FROM {tablename};") 
	old_data = curr.fetchall()
	column_names  = [desc[0] for desc in curr.description]
	old_df = pd.DataFrame(old_data, columns = column_names)
	curr.close()
	conn.close()
	return old_df
print(fetchData(tablename='test_table'))