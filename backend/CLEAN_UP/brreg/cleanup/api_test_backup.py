import pandas as pd 
import json
import psycopg2
from psycopg2.extras import Json

from sqlalchemy import create_engine


''' ___ imports for: get json from path ________ '''
import gzip
import pandas as pd 
import pprint
import requests 
from bs4 import BeautifulSoup

def getRequest():
	url = 'https://data.brreg.no/enhetsregisteret/api/enheter/?page=3&size=20' #-i -X GET
	r = requests.get(url, timeout=10)
	json = r.json()
	return json

def getpage(json):
	page =  json['page']
	return page

def getMaxpages(page):
	print(page)
	total_pages = page['totalPages']
	return total_pages

def getCurrentpage(page):
	current_page = page['number']
	return current_page

def getData(json):
	data = json['_embedded']['enheter']
	return data	

def makeDataframe(data):
	df = pd.json_normalize(data)
	return df

def datasetEditor(df):
	test = df[['organisasjonsnummer',
				'navn',
				'registreringsdatoEnhetsregisteret',
				'registrertIMvaregisteret',
				'antallAnsatte',
				'registrertIForetaksregisteret',
				'registrertIStiftelsesregisteret',
				'registrertIFrivillighetsregisteret',
				'konkurs',
				'underAvvikling',
				'underTvangsavviklingEllerTvangsopplosning',
				'organisasjonsform.kode',
				'organisasjonsform.beskrivelse',
				'naeringskode1.beskrivelse',
				'naeringskode1.kode',
				'forretningsadresse.land',
				'forretningsadresse.landkode',
				'forretningsadresse.postnummer',
				'forretningsadresse.poststed',
				'forretningsadresse.adresse',
				'forretningsadresse.kommune',
				'forretningsadresse.kommunenummer',
				'institusjonellSektorkode.kode',
				'institusjonellSektorkode.beskrivelse',
				'hjemmeside',
				'stiftelsesdato',
				'sisteInnsendteAarsregnskap']]
	# df.drop([	'maalform',
	# 			'organisasjonsform._links.self.href',
	# 			'_links.self.href',
	# 			'postadresse.land',
	# 			'postadresse.landkode',
	# 			'postadresse.postnummer',
	# 			'postadresse.poststed',
	# 			'postadresse.adresse',
	# 			'postadresse.kommune',
	# 			'postadresse.kommunenummer',
	# 			'naeringskode2.beskrivelse',
	# 			'naeringskode2.kode',
	# 			'naeringskode2.hjelpeenhetskode'    	], axis = 1, inplace = True)
	# return df 
	
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
								'sisteInnsendteAarsregnskap':'siste_innsendt_årsregnskap',})#, inplace = True })
	return df 


def apiManager():
	json = getRequest()
	
	'''pages'''
	page = getpage(json)
	toal_pages = getMaxpages(page)
	current_page = getCurrentpage(page)	

	'''data'''
	data = getData(json)
	df = makeDataframe(data)
	df = datasetEditor(df)
	return df, toal_pages, current_page










''' ___ POSTGRES BOILERPLATE ____________________________________________________ '''

# Payload:
payload = { 'dbname'   : 'media_vest',
			'host'     : 'localhost',
			'user'     : 'postgres',
			'password' : 'Orikkel1991',
			# 'tablename': 'brreg',  }
			'tablename': 'brreg_table',  }

import psycopg2
from psycopg2.extras import Json

# ___ local imports ________
# from Config import payload  #Saving for later
# print(payload)


''' ___ PREP _______________________________________________ '''
def parseConfig():
	dbname = payload['dbname']
	host = payload['host']
	user = payload['user']
	password = payload['password']
	tablename = payload['tablename']
	return dbname, host, user, password, tablename

def getCursor(conn):
	return conn.cursor() # returns cursor

def getConnection():
	return psycopg2.connect(
		dbname = dbname, 
		host = host, 
		user = user, 
		password = password)

def insertData(df):
	dbname, host, user, password, tablename = parseConfig()
	engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:5432/{dbname}')
	df.to_sql(f'{tablename}', engine, if_exists = 'replace', index = False)

# def insertData(conn, dict_obj, tablename):
	# print()
	# print("_"*50)
	# print(f'inserting data_json to {tablename}:')
	# print('data inserted:')
	# pprint.pprint(dict_obj)
	# print("_"*50)
	# print()
	# print(" NOT FINISHED ")
	# curr = conn.cursor()
	# # PS NEEDS TO BE CHANGED!!! using a different datastructure from boilerplate
	# curr.execute(f'''
	# 	INSERT INTO
	# 		{tablename}(org_num,
	# 					navn,
	# 					registreringsdato,
	# 					mva_registrert,
	# 					antall_ansatte,
	# 					foretaks_registeret,
	# 					stiftelses_registeret,
	# 					frivillighets_registeret,
	# 					konkurs,
	# 					under_avvikling,
	# 					under_tvangsavvikling_eller_oppløsning,
	# 					organisasjonsform_kode,
	# 					organisasjonsform_beskrivelse,
	# 					naeringskode1_beskrivelse,
	# 					naeringskode1_kode,
	# 					land,
	# 					landkode,
	# 					postnummer,
	# 					poststed,
	# 					adresse,
	# 					kommune,
	# 					kommunenummer,
	# 					sektorkode_kode,
	# 					sektorkode_beskrivelse,
	# 					hjemmeside,
	# 					stiftelsesdato,
	# 					siste_innsendt_årsregnskap) 	
	# 	VALUES(	%(org_num)s, 
	# 			%(navn)s, 
	# 			%(registreringsdato)s, 
	# 			%(mva_registrert)s, 
	# 			%(antall_ansatte)s, 
	# 			%(foretaks_registeret)s, 
	# 			%(stiftelses_registeret)s, 
	# 			%(frivillighets_registeret)s, 
	# 			%(konkurs)s, 
	# 			%(under_avvikling)s, 
	# 			%(under_tvangsavvikling_eller_oppløsning)s, 
	# 			%(organisasjonsform_kode)s, 
	# 			%(organisasjonsform_beskrivelse)s, 
	# 			%(naeringskode1_beskrivelse)s, 
	# 			%(naeringskode1_kode)s, 
	# 			%(land)s, 
	# 			%(landkode)s, 
	# 			%(postnummer)s, 
	# 			%(poststed)s, 
	# 			%(adresse)s, 
	# 			%(kommune)s, 
	# 			%(kommunenummer)s, 
	# 			%(sektorkode_kode)s, 
	# 			%(sektorkode_beskrivelse)s, 
	# 			%(hjemmeside)s, 
	# 			%(stiftelsesdato)s, 
	# 			%(siste_innsendt_årsregnskap)s)''', [json.dumps(dict_obj)])

# def createNewTable(conn, df, tablename):
	# curr = conn.cursor()
	# create_table = """CREATE TABLE {} (	org_num VARCHAR PRIMARY KEY,
	# 									navn VARCHAR,
	# 									registreringsdato VARCHAR,
	# 									mva_registrert VARCHAR,
	# 									antall_ansatte VARCHAR,
	# 									foretaks_registeret VARCHAR,
	# 									stiftelses_registeret VARCHAR,
	# 									frivillighets_registeret VARCHAR,
	# 									konkurs VARCHAR,
	# 									under_avvikling VARCHAR,
	# 									under_tvangsavvikling_eller_oppløsning VARCHAR,
	# 									organisasjonsform_kode VARCHAR,
	# 									organisasjonsform_beskrivelse VARCHAR,
	# 									naeringskode1_beskrivelse VARCHAR,
	# 									naeringskode1_kode VARCHAR,
	# 									land VARCHAR,
	# 									landkode VARCHAR,
	# 									postnummer VARCHAR,
	# 									poststed VARCHAR,
	# 									adresse VARCHAR,
	# 									kommune VARCHAR,
	# 									kommunenummer VARCHAR,
	# 									sektorkode_kode VARCHAR,
	# 									sektorkode_beskrivelse VARCHAR,
	# 									hjemmeside VARCHAR,
	# 									stiftelsesdato VARCHAR,
	# 									siste_innsendt_årsregnskap VARCHAR)
	# 								   ;""".format(tablename)
	# curr.execute(create_table)
	# conn.commit()
	# curr.close()
	# insertData(df)

# def tryCreateTable(conn):
	# try:
	# 	createTable(conn)
	# except (Exception, psycopg2.DataError) as error:
	# 	print(error)
	# 	conn = getConnection()

# def tableManager(conn, table_exists, tablename, dict_obj):
	# ''' IF statement - makes decition based on table_exists from checkForTable():
	# 		a. runs addToDatabase(), if table_exists == True
	# 		b. runs createNewTable(), if table_exists == False
	# '''
	# if table_exists == True:
	# 	insertData(df)
	# 	# insertData(conn, dict_obj, tablename)
	# elif table_exists == False:
	# 	createNewTable(conn, df, tablename)
	# else:
	# 	print(f'    Unknown Error in tableManager(): table_exists was neither True or False, or data_json might be corrupt.')
	# 	print(f'    				Check for errors in "checkForTable()".')

# def checkForTable(conn, tablename):
	# table_exists = False
	# print(f"checking if {tablename} exists: ")
	# try:
	# 	curr = conn.cursor()
	# 	curr.execute("select * from information_schema.tables where table_name=%s", (tablename,))				 	# check table
	# 	# curr.execute("select exists(select * from information_schema.tables where table_name=%s)", (tablename,))	# check table alt
	# 	# curr.execute("select exists(select relname from pg_class where relname='" + table_str + "')")			 	# check table alt
	# 	exists = curr.fetchone()[0]
	# 	table_exists = True
	# 	print(f"    table; {tablename} was found, proceeding to concatenate new data..")
	# 	print(f"    please wait..")
	# 	curr.close()
	# # except psycopg2.Error as e:
	# except TypeError as e:
	# 	print(f"    Error: table {tablename} does not exsist, proceeding to create a new table..")
	# 	print(f"    please wait..")
	# print(f"table_exists = {table_exists}")
	# return table_exists

def fetchData(conn, tablename):
	dbname, host, user, password, tablename = parseConfig()
	curr = getCursor(conn)  
	curr.execute(f"SELECT * FROM {tablename};") 
	old_data = curr.fetchall()
	# curr.execute(f"Select * FROM {tablename} LIMIT 0")
	
	column_names  = [desc[0] for desc in curr.description]
	print(type(column_names))

	# column_names = old_df['org_num'].squeeze().tolist()
	# print(type(column_names))

	old_df = pd.DataFrame(old_data, columns = column_names)
	# print(type(old_data))
	# old_df = pd.json_normalize(old_data)
	# print(old_df['org_num'])

	# col_one_list = old_df['org_num'].squeeze().tolist()
	# # print(col_one_list)
	# df=old_df.set_index([col_one_list])
	# print(df)



	# print(type(old_data))
	# print(old_df)
	# new_index = old_df['org_num'].values.tolist()
	# new_index =[i.value for i in old_df['org_num']]
	# print(new_index)
	# test = old_df.set_index(['org_num'],  inplace = True)
	# old_df.set_index(old_df['org_num'].squeeze(), inplace = True)
	# print(old_df)
	# print((old_df.columns))
	# print(type(old_df.columns))

	curr.close()
	conn.close()
	return old_df

# # TEMPORARY
# def alterTable(conn):
# 	curr = getCursor(conn)
# 	for newname in column_names:
# 		curr.execute("ALTER TABLE <tablename> RENAME <oldcolumn> TO <newcolumn>;")

def concatData(df, old_df):
	# print(df.iloc[0])
	# print(len(df.iloc[0]))
	# print()
	# print(old_df.iloc[0])
	# print(len(old_df.iloc[0]))
	# print()
	# print()
	df.set_index(['org_num'],  inplace = True)
	try: 
		df.drop('org_num', axis=1, inplace=True)
	except KeyError:
		print("KeyError: df['org_num']")
	# old_df.set_index([['org_num']],  inplace = True)
	# col_one_list = old_df['org_num'].squeeze().tolist()
	# old_df.set_index(col_one_list, inplace = True)
	
	old_df.set_index(old_df['org_num'].squeeze(), inplace = True)
	try: 
		old_df.drop('org_num', axis=1, inplace=True)
	except KeyError:
		print("KeyError: old_df['org_num']")
	


	# print((old_df.columns))
	# print(type(old_df.columns))


	print("NEW DF:")
	print(df)
	# print(f"column types:\n{df.dtypes}")
	print()
	print("OLD DF:")
	print(old_df)
	# print(f"column types:\n{old_df.dtypes}")
	print()
	df = pd.concat((df, old_df), axis = 0)
	df = df.groupby(df.index).last().reset_index()
	# print(f"column types:\n{df.dtypes}")
	return df

if __name__ == '__main__':
	dbname, host, user, password, tablename = parseConfig()
	conn = getConnection()
	# curr = getCursor(conn)
	df, toal_pages, current_page = apiManager()


	''' manage database '''
	# table_exists = checkForTable(conn, tablename)
	# dict_obj = df.to_dict()
	# print(df)
	# print()
	# print("#"*100)

	# old_df = fetchData(conn, tablename)
	# df = concatData(df, old_df)
	try:
		old_df = fetchData(conn, tablename)
	except:
		print("table does not exsist")
	try: 
		df = concatData(df, old_df)
	except:
		print("unable to concat") 
	

	insertData(df)
	
	print()
	print()
	print("#"*100)
	print('FINAL')
	print(df)


	# tableManager(conn, table_exists, tablename, df)

	# page = json['page']
	# current_page = page['number']
	# total_pages = page['totalpages']
	
	# print(current_page)
	# print(total_pages)
	# print(len(data))
	# pprint.pprint(data)