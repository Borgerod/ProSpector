import time
import pandas as pd 
import psycopg2
from sqlalchemy import create_engine
from datetime import datetime as dt 
# ___ local imports ________
from config import payload


def parseConfig_to_User_API():
	dbname = payload['dbname2']
	host = payload['host']
	user = payload['user']
	password = payload['password']
	return dbname, host, user, password

def parseConfig():
	dbname = payload['dbname']
	host = payload['host']
	user = payload['user']
	password = payload['password']
	return dbname, host, user, password

def getCursor(conn):
	return conn.cursor()

def getConnection(**kwargs):
	if kwargs.get('to_user_api', None):
		dbname, host, user, password = parseConfig_to_User_API()
	else:
		dbname, host, user, password = parseConfig()
	return psycopg2.connect(
		dbname = dbname, 
		host = host, 
		user = user, 
		password = password)


def getInputTable(tablename):
	return fetchData(tablename) # TODO: function is deprecated, should be deleted (some files might still use this)

def fetchData(tablename, **kwargs):
	''' 
		desc: fetches old_df from database
		reason: needed for replaceData() & [OLD] insertData()
	'''
	if kwargs.get('to_user_api', None):
		dbname, host, user, password = parseConfig_to_User_API()
		conn = getConnection(to_user_api=True)
	else:
		dbname, host, user, password = parseConfig()
		conn = getConnection()
	curr = getCursor(conn)  
	curr.execute(f'SELECT * FROM "{tablename}";') 
	old_data = curr.fetchall()
	column_names  = [desc[0] for desc in curr.description]
	old_df = pd.DataFrame(old_data, columns = column_names)
	curr.close()
	conn.close()
	return old_df


def insertData(df, tablename, **kwargs): 
	''' 
		desc: inserts final dataframe to database,
		does: checks if tablename == 'brreg_table'
			 ! then either "APPENDS" or "REPLACES" the table
			  creates new table if table it does not exsist, else it updates
	'''

	if kwargs.get('to_user_api', None):
		conn = getConnection(to_user_api=True)
		dbname, host, user, password = parseConfig_to_User_API()
	else:
		conn = getConnection()
		dbname, host, user, password = parseConfig()
	curr = getCursor(conn)
	engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:5432/{dbname}')	
	if tablename == 'brreg_table':
		df.to_sql(f"{tablename}", engine, if_exists = 'append', index = False)
	else:
		try:
			df.to_sql(f"{tablename}", engine, if_exists = 'replace', index = False)
		except psycopg2.ProgrammingError:
			time.sleep(0.2)
			df.to_sql(f"{tablename}", engine, if_exists = 'replace', index = False)
	curr.close()
	conn.close()

def replacetData(df, tablename, **kwargs):  # ! MIGHT NOT ME NESSASARY, cleanUp() should have solved this issue
	''' 
		Special case for brreg.py where downloading whole dataset 
		appended instead of replacing, this was the seasiest solution. 
	'''
	if kwargs.get('to_user_api', None):
		conn = getConnection(to_user_api=True)
		dbname, host, user, password = parseConfig_to_User_API()
	else:
		conn = getConnection()
		dbname, host, user, password = parseConfig()
	curr = getCursor(conn)
	
	engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:5432/{dbname}')	
	df.to_sql(f'{tablename}', engine, if_exists = 'replace', index = False)
	curr.close()
	conn.close()

def concatData(df, old_df):
	''' 
		desc: Concat old_df from database with new df from api request.
		reason: needed for replaceData() & [OLD] insertData()
	'''
	try:
		old_df.set_index(old_df['org_num'].squeeze(), inplace = True)
	except KeyError:
		old_df.set_index(old_df['org_num'], inplace = True)
	
	try: 
		old_df.drop('org_num', axis = 1, inplace=True)
	except KeyError:
		pass
	
	try:
		df.set_index(['org_num'],  inplace = True)
	except:
		pass
	
	try: 
		df.drop('org_num', axis = 1, inplace=True)
	except KeyError:
		pass
	
	df = pd.concat((df, old_df), axis = 0)
	return df.groupby(df.index).last().reset_index()

def cleanUp(tablename, **kwargs):
	'''	
		desc: this function performs a cleanup routine which is runned after every extraction run.
		does: fetches table from database, drops duplicates (pandas), then replaces old table. 
		reason: needed for appendData() 
				brreg.py will extract all the data (or up to the specified limit) 
				from brønnøysund register, which is appended to brreg_table and 
				if the table is not empty it will create duplicates. this function performs a 
	'''
	if kwargs.get('to_user_api', None):
		df = fetchData(tablename, to_user_api=True)
	else:
		df = fetchData(tablename)
	df = df.drop_duplicates(subset = 'org_num')
	df = df.reset_index()
	if kwargs.get('to_user_api', None):
		conn = getConnection(to_user_api=True)
		dbname, host, user, password = parseConfig_to_User_API()
	else:
		conn = getConnection()
		dbname, host, user, password = parseConfig()
	curr = getCursor(conn)
	engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:5432/{dbname}')
	df.to_sql(f'{tablename}', engine, if_exists = 'replace', index = False)
	curr.close()
	conn.close()

def checkForTable(tablename):
	print(f"checking if {tablename} exists.. ")
	conn = getConnection()
	try:
		curr = conn.cursor()
		curr.execute(f"SELECT * FROM {tablename};")
		_ = curr.fetchone()[0]
		table_exists = True
		print(f"    table; {tablename} exist")
		curr.close()
	except psycopg2.errors.UndefinedTable:
		table_exists = False
		print(f"    Error: table {tablename} does not exist")
	conn.close()
	return table_exists

def checkForElement(org_num, tablename):
	conn = getConnection()
	try:
		curr = conn.cursor()
		curr.execute(f"""SELECT FROM public."{tablename}" WHERE "org_num" = '{org_num}'""")
		_ = curr.fetchone()
		conn.close()
		return True
	except TypeError:
		conn.close()
		return False

def checkIfMissing(org_num):
	'''
		checks if company is missing from input_table, 
		if so, then it is already confirmed and 
		the extractor should move on to the next company. 
	'''
	if checkForElement(org_num, tablename='input_table'):
		return False
	else:
		return True

def postLastUpdate(tablename):
	conn = getConnection()
	curr = getCursor(conn)
	curr.execute(
	f""" UPDATE update_tracker
				SET {tablename} = '{dt.now().strftime('%Y-%m-%d')}'
				WHERE index = 'date'""")
	conn.commit()
	curr.close()
	conn.close()

def deleteData(org_num, tablename):
	conn = getConnection()
	curr = getCursor(conn)
	curr.execute(f"""DELETE FROM public."{tablename}" WHERE "org_num" = '{org_num}'""")
	conn.commit()
	curr.close()
	conn.close()

def purgeTable(tablename, **kwargs):
	''' 
		Purges the data for the given table, with a warning, unless an override is stated.
		How to call function:
			purgeTable(tablename = 'gulesider_test_table', override = True)
	'''

	if kwargs.get('override', None):
		purge()
	else:
		print(f'''	________ !!! WARNING !!! ________\n 	you are about to delete ALL the of the data stored in {tablename}, \n 	please make sure to make a backup before proceeding.\n''')
		repeat = True
		while repeat:
			input_ = input(f"	are you sure you want to purge {tablename}? (y/n)")
			if input_ == ("y" or "Y" or "yes" or "Yes"):
				print("\n		purging table..")
				purge()
				print(f"		purge complete.")
				repeat = False
				break
			elif input_ == ("n" or "N" or "no" or "No"):
				print(f"\n	aborting purge of {tablename}.")
				repeat = False
				break
			else:
				print('''\n	Error: invalied input, please type "y" for yes, or "n" for no, \n 	or press "ctrl+c" to close the program.\n\n''')

def purge():
	'''
		purge command used by purgeTable()
	'''
	conn = getConnection()
	curr = getCursor(conn)
	curr.execute(f"truncate daily_monitor;")
	conn.commit()
	curr.close()
	conn.close()


'''* ___ MANAGER _______________________________________________ 
'''

def databaseManager(df, tablename, **kwargs):
	''' 
		desc: the file's main function 
		does: gets connection, runs if statement, then sends table straight to insertData()
			  if tablename is NOT 'brreg_table': runs the "concat(old_df, new_df)" routine.
			  if tablename is 'brreg_table': does nothing.
	'''
	if kwargs.get('to_user_api', None):		
		old_df = pd.DataFrame()
		try:
			old_df = fetchData(tablename, to_user_api=True)
		except:
			pass
		try: 
			df = concatData(df, old_df)
		except:
			pass
		try:
			insertData(df, tablename, to_user_api=True)	
			print(f"Succeeded to insert data in {tablename}")
		except: 
			print(f"Faled to insert data in {tablename}")
	else:	
		if 'brreg_table' not in tablename:
			old_df = pd.DataFrame()
			try:
				old_df = fetchData(tablename)
			except:
				pass
			try: 
				df = concatData(df, old_df)
			except:
				pass
		try:	
			insertData(df, tablename)
			
			print("Succeeded to insert data")
		except: 
			print("Faled to insert data")


def googleDatabaseManager(df, tablename, **kwargs):
	''' 
		desc: the file's main function 
		does: gets connection, runs if statement, then sends table straight to insertData()
			  if tablename is NOT 'brreg_table': runs the "concat(old_df, new_df)" routine.
			  if tablename is 'brreg_table': does nothing.
	'''
	if kwargs.get('to_user_api', None):		
		old_df = pd.DataFrame()
		try:
			old_df = fetchData(tablename, to_user_api=True)
		except:
			pass
		df = concatData(df, old_df)
		try:
			insertData(df, tablename, to_user_api=True)	
			print(f"Succeeded to insert data in {tablename}")
		except: 
			time.sleep(0.2)
			insertData(df, tablename, to_user_api=True)