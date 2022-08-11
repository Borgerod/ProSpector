'''* TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP 
-							
-							_____ WHERE I LEFT OF _____
-						[10.08.22]
-						trying out [ALTERNATIVE] in [ MAKE DECISION a ]  
-
- TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP '''


import pandas as pd 
import numpy as np
import pandas as pd 
import json
import psycopg2
from psycopg2.extras import Json
from sqlalchemy import create_engine
import concurrent.futures

# ___ local imports ________
# from config import google_payload, brreg_payload, CHUNK_SIZE
from config import payload

'''	
	* current version of postgres.py:
		* 1. appends new table rows to old table, 
		*	 [without fetching old table and without using concat]
		* 2. runs cleanUp() which drops_duplicates, then inserts the table back

	! IMPORTANT NOTE:
		- [old] insertData() was named insertData but acted as a replaceData(), and should be named as such
		- [new] insertData() is named insertData() acts as name implies, however other files are made for old insertData, BE AWARE OF THAT while making changes

	 # TODO ____________________
	 #  - CURRENT GOAL: manage to insert/append new data to tables without using cleanUp(), pick one: 
		# - [ ] try: chaging insertData() to append rows instead of replacing table, when "updating" table with new rows.
		# - [ ] try: changing insertData() to append replace whole table, when "updating" table with new rows.

	TODO [ MAKE DECISION a ]
		- [ ] rename insertData() to appendData(), then remake insertData()
		- [ ] [MAYBE] make replaceData() & purgeData()
	  	- [ ] update extractors to call appendData() or insertData()
	  	- if [ALTERNATIVE] is used: 
	  		- [ ] include if statement in databaseManager()	

	TODO [ MAKE DECISION b ]
	  	- [X] merge fetchData and getInputTable()
	  	- [ ] update extractors using getInputData() if needed
	  	 	  UPDATE NOTE: getInputTable not referenced in postgres.py  

	TODO [ OTHER ]
	- [X] finalize databaseManager()

	TODO [ CONSIDER ]
	- [ ] replace current system for getFilename() etc, with a simple parseConfig()


	TODO [ TEST NEEDED ]
	- [ ] test if cleanUp is needed or not when running concatData() routine  
'''



''' * ___ PREP _______________________________________________ 
'''
def parseConfig():
	''' returns parsed payload from config file '''
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


''' * ___ ACTIONS _______________________________________________ 
'''

''' ? __________________________________________ [ MAKE DECISION b ] ______________________________________________
	decision desc: 
	 	fetchData() and getInputTable() as basicly the same function
	 	merge them so you only need one of them. 

	 	! IMPORTANT NOTE: make sure functions using getInputData doesnt need editing 
'''
# fixme [OLD] getInputTable()
	# def getInputTable(tablename):
		# ''' 
		# fucntion documentaion:
		# 	fetches an updated Input_List from database,
		# 	the extractors will base their searches on this list.

		# 	PS: table is returned as np.array. 
		# '''
		# dbname, host, user, password = parseConfig()
		# conn = getConnection()	
		# curr = getCursor(conn)  
		# curr.execute(f"SELECT * FROM {tablename};") 
		# input_data = curr.fetchall()
		# input_df = pd.DataFrame(input_data, columns = [desc[0] for desc in curr.description])
		# inputs = input_df.to_numpy()
		# curr.close()
		# conn.close()
		# return inputs

# * [NEW] getInputTable()
def getInputTable(tablename):
	return fetchData(tablename) # FIXME: Temporary Quick fix for [ MAKE DECISION b ] 

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
''' ? ____________________________________________________________________________________________________________
'''

'''? __________________________________________ [ MAKE DECISION a ] ________________________________________________
'''
# fixme [OLD] insertData() 
	# def insertData(df, tablename):
	# ''' 
	# 	inserts final dataframe to database, 
	# 	creates new table if table it does not exsist, else it updates
	# '''
	# conn = getConnection()
	# curr = getCursor(conn)
	# dbname, host, user, password = parseConfig()
	# engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:5432/{dbname}')	
	# df.to_sql(f'{tablename}', engine, if_exists = 'replace', index = False)
# [OLD NEW] replaceData() --> REPLACE
	# def replaceData(df, tablename): 
		''' 
			inserts final dataframe to database, 
			! REPLACES old table, with new table.
			if tablename does not exsist in db, it creates new table. 
		'''
		conn = getConnection()
		curr = getCursor(conn)
		dbname, host, user, password = parseConfig()
		engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:5432/{dbname}')
		df.to_sql(f'{tablename}', engine, if_exists = 'replace', index = False)
# [OLD NEW] insertData()	--> APPEND
	# def insertData(df, tablename): 
		''' 
			inserts final dataframe to database, 
			! APPENDS new table to old table.
			if tablename does not exsist in db, it creates new table. 
		'''
	conn = getConnection()
	curr = getCursor(conn)
	dbname, host, user, password = parseConfig()
	engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:5432/{dbname}')
	df.to_sql(f'{tablename}', engine, if_exists = 'append', index = False)

# * [ALTERNATIVE] insertData() ---> [ TWO-IN-ONE ]
def insertData(df, tablename): 
	''' 
		desc: inserts final dataframe to database,
		does: checks if tablename == 'brreg_table'
			 ! then either "APPENDS" or "REPLACES" the table
			  creates new table if table it does not exsist, else it updates
	'''
	conn = getConnection()
	curr = getCursor(conn)
	dbname, host, user, password = parseConfig()
	engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:5432/{dbname}')
	if tablename == 'brreg_table':
		df.to_sql(f'{tablename}', engine, if_exists = 'append', index = False)
	else:
		df.to_sql(f'{tablename}', engine, if_exists = 'replace', index = False)
'''? _______________________________________________________________________________________________________________
'''

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

def cleanUp(tablename):
	'''	
		desc: this function performs a cleanup routine which is runned after every extraction run.
		does: fetches table from database, drops duplicates (pandas), then replaces old table. 
		reason: needed for appendData() 
				brreg.py will extract all the data (or up to the specified limit) 
				from brønnøysund register, which is appended to brreg_table and 
				if the table is not empty it will create duplicates. this function performs a 
	'''
	df = fetchData(tablename)
	df = df.drop_duplicates(subset = 'org_num')
	conn = getConnection()
	curr = getCursor(conn)
	dbname, host, user, password = parseConfig()
	engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:5432/{dbname}')
	df.to_sql(f'{tablename}', engine, if_exists = 'append', index = False)
	print(df)
	curr.close()
	conn.close()


'''* ___ MANAGER _______________________________________________ 
'''
# fixme [OLD] databaseManager()
# def databaseManager(df, tablename):
	# dbname, host, user, password = parseConfig()
	# conn = getConnection()

	# # OLD concat call  [might be needed for [OLD]inserData() / [NEW]replaceData()]
	# 	''' manage database '''
	# 	# old_df = pd.DataFrame()
	# 	# try:
	# 	# 	conn = getConnection()
	# 	# 	old_df = getInputTable(tablename)
	# 	# 	# old_df = fetchData(tablename)
	# 	# except:
	# 	# 	pass
	# 	# 	# print("table does not exsist")		
	# 	# try: 
	# 	# 	df = concatData(df, old_df)
	# 	# 	# print(df)
	# 	# except:
	# 	# 	pass
	# 	# 	print("unable to concat")

	# insertData(df, tablename)	

# [OLD NEW] databaseManager()	
# # def databaseManager(df, tablename):
	# # ''' 
	# # 	desc: the file's main function 
	# # 	does: gets connection, runs if statement, then sends table straight to insertData()
	# # 		  if tablename is NOT 'brreg_table': runs the "concat(old_df, new_df)" routine.
	# # 		  if tablename is 'brreg_table': does nothing.
	# # '''
	# # print('\n fetching data\n passing to databaseManager() \n check if tablename == "brreg_table":') #FIXME --> TEMP while testing
	# # #FIXME --> TEMP while testing
	# # # dbname, host, user, password = parseConfig() 
	# # # conn = getConnection()
	# # if 'brreg_table' not in tablename:
	# # 	print(f'	FALSE --> tablename is NOT named "brreg_table"\n	 	tablename: {tablename}\n	 	type: {type(tablename)}\n') #FIXME --> TEMP while testing

	# # 	old_df = pd.DataFrame()
	# # 	try:
	# # 		# conn = getConnection()
	# # 		old_df = getInputTable(tablename)
	# # 		# old_df = fetchData(tablename)
	# # 	except:
	# # 		# pass
	# # 		print(f'	Error: did NOT find old_table --> old_df = empty') #FIXME --> TEMP while testing
	# # 		# print("table does not exsist")		
	# # 	try: 
	# # 		df = concatData(df, old_df)
	# # 	except:
	# # 		# pass
	# # 		print(f'	Error: UNABLE to concat --> final_df = new_table') #FIXME --> TEMP while testing
	# # 		# print("unable to concat")
	# # 	insertData(df, tablename)
	# # else: 
	# # 	print(f'	TRUE --> tablename IS named "brreg_table"\n	 	tablename: {tablename}\n	 	type: {type(tablename)}\n') #FIXME --> TEMP while testing
	# # 	insertData(df, tablename)
	# # 	cleanUp(tablename) #FIXME --> TEMP while testing
	# # print(f"|				   Finished 				|")

# * [NEW] databaseManager()	
def databaseManager(df, tablename):
	''' 
		desc: the file's main function 
		does: gets connection, runs if statement, then sends table straight to insertData()
			  if tablename is NOT 'brreg_table': runs the "concat(old_df, new_df)" routine.
			  if tablename is 'brreg_table': does nothing.
	'''
	dbname, host, user, password = parseConfig() 
	## conn = getConnection()

	if 'brreg_table' not in tablename:
		old_df = pd.DataFrame()
		try:
			old_df = fetchData(tablename)
		except:
			## print("table does not exsist")
			pass
		try: 
			df = concatData(df, old_df)
		except:
			## print("unable to concat")
			pass
		insertData(df, tablename)
	else: 
		insertData(df, tablename)


'''
* [MAKE DECISION a]-TEST CONCLUTION : postgres.py works as intended 
	 FIXME brreg.py might NOT work as intended; 
		- whileloop is infinate (might be due to test settup)


	* FIRST RUN OUTPUT, (tablename: 'brreg_table'):
	 fetching data
	 passing to databaseManager()
	 check if tablename == "brreg_table":
	        TRUE --> tablename IS named "brreg_table"
	                tablename: brreg_table
	                type: <class 'str'>

	        runs insertData()
	 check if tablename == "brreg_table": (note statement looks different)
	        TRUE --> tablename IS named "brreg_table"
	                tablename: brreg_table
	                type: <class 'str'>

	        actions: APPENDS new_table to old_table
	        runs cleanUp():
	                runs fetchData() -> to get getting old_table
	                runs drop_duplicates()
	                create_engine() --> APPEND
	|                                  Finished                             |

	* SECOND RUN OUTPUT, (tablename: 'gulesider_table'):
	 fetching data
	 passing to databaseManager()
	 check if tablename == "brreg_table":
	        FALSE --> tablename is NOT named "brreg_table"
	                tablename: gulesider_table
	                type: <class 'str'>

	        runs getInputTable() -> try to get getting old_table
	        runs concatData() -> try to old_table with new_table
	        runs insertData()
	 check if tablename == "brreg_table": (note statement looks different)
	        FALSE --> tablename is NOT named "brreg_table"
	                tablename: gulesider_table
	                type: <class 'str'>

	        actions: REPLACE old_table with new_table
	|                                  Finished                             |

	TEST MATERIAL:
		def getInputTable(tablename): #FIXME --> TEMP while testing
			print(f'	runs getInputTable() -> try to get getting old_table') #FIXME --> TEMP while testing
		def concatData(df, old_df): #FIXME --> TEMP while testing
			print(f'	runs concatData() -> try to old_table with new_table') #FIXME --> TEMP while testing
		def insertData(df, tablename): #FIXME --> TEMP while testing
			print(f'	runs insertData() \n check if tablename == "brreg_table": (note statement looks different)') #FIXME --> TEMP while testing
			if tablename == 'brreg_table': #FIXME --> TEMP while testing
				print(f'	TRUE --> tablename IS named "brreg_table"\n	 	tablename: {tablename}\n	 	type: {type(tablename)}\n') #FIXME --> TEMP while testing
				print(f'	actions: APPENDS new_table to old_table') #FIXME --> TEMP while testing
			else: 
				print(f'	FALSE --> tablename is NOT named "brreg_table"\n	 	tablename: {tablename}\n	 	type: {type(tablename)}\n') #FIXME --> TEMP while testing
				print(f'	actions: REPLACE old_table with new_table') #FIXME --> TEMP while testing

		def cleanUp(tablename): #FIXME --> TEMP while testing
			print(f'	runs cleanUp():') #FIXME --> TEMP while testing
			print(f'		runs fetchData() -> to get getting old_table')
			print(f'		runs drop_duplicates()')
			print(f'		create_engine() --> APPEND')

		# * [NEW] databaseManager()	
		def databaseManager(df, tablename):
			print('\n fetching data\n passing to databaseManager() \n check if tablename == "brreg_table":') #FIXME --> TEMP while testing
			#FIXME --> TEMP while testing
			# dbname, host, user, password = parseConfig() 
			# conn = getConnection()
			if 'brreg_table' not in tablename:
				print(f'	FALSE --> tablename is NOT named "brreg_table"\n	 	tablename: {tablename}\n	 	type: {type(tablename)}\n') #FIXME --> TEMP while testing

				old_df = pd.DataFrame()
				try:
					# conn = getConnection()
					old_df = getInputTable(tablename)
					# old_df = fetchData(tablename)
				except:
					# pass
					print(f'	Error: did NOT find old_table --> old_df = empty') #FIXME --> TEMP while testing
					# print("table does not exsist")		
				try: 
					df = concatData(df, old_df)
				except:
					# pass
					print(f'	Error: UNABLE to concat --> final_df = new_table') #FIXME --> TEMP while testing
					# print("unable to concat")
				insertData(df, tablename)
			else: 
				print(f'	TRUE --> tablename IS named "brreg_table"\n	 	tablename: {tablename}\n	 	type: {type(tablename)}\n') #FIXME --> TEMP while testing
				insertData(df, tablename)
				cleanUp(tablename) #FIXME --> TEMP while testing
			print(f"|				   Finished 				|")

				
		databaseManager(df = pd.DataFrame(), tablename='gulesider_table')
'''

'''
* [MAKE DECISION b]-TEST CONCLUTION: postgres.py works as intended
	* TEST OUTPUT
	tablename: "brreg_table
	______ TABLE FROM getInputTable(tablename)____________
	         org_num                                         navn  ... har_Facebook                                  facebook
	0    811879312.0                      17. Mai Nemda Kaupanger  ...        False                                      None
	1    812467182.0                                     &More AS  ...        False                                      None
	2    813646552.0                                     1 Sbx AS  ...        False                                      None
	3    813657872.0            1. Skudeneshavn Sjø Speidergruppe  ...         True  https://www.facebook.com/219276101515007
	4    814048462.0  10th Planet Jiu Jitsu Bergen - Frode Nilsen  ...        False                                      None
	..           ...                                          ...  ...          ...                                       ...
	582  999286976.0                   0-6 Vålerenggata barnehage  ...        False                                      None
	583  999292364.0                            1+1 Architects AS  ...        False                                      None
	584  999413706.0                           1-2-3 Bygg Vest AS  ...        False                                      None
	585  999515606.0                                 1001 Natt AS  ...        False                                      None
	586  999529852.0                            1-2-3 Regnskap AS  ...        False                                      None

	[587 rows x 14 columns]

	tablename: "brreg_table
	______ TABLE FROM fetchData(tablename)____________
	         org_num                                         navn  ... har_Facebook                                  facebook
	0    811879312.0                      17. Mai Nemda Kaupanger  ...        False                                      None
	1    812467182.0                                     &More AS  ...        False                                      None
	2    813646552.0                                     1 Sbx AS  ...        False                                      None
	3    813657872.0            1. Skudeneshavn Sjø Speidergruppe  ...         True  https://www.facebook.com/219276101515007
	4    814048462.0  10th Planet Jiu Jitsu Bergen - Frode Nilsen  ...        False                                      None
	..           ...                                          ...  ...          ...                                       ...
	582  999286976.0                   0-6 Vålerenggata barnehage  ...        False                                      None
	583  999292364.0                            1+1 Architects AS  ...        False                                      None
	584  999413706.0                           1-2-3 Bygg Vest AS  ...        False                                      None
	585  999515606.0                                 1001 Natt AS  ...        False                                      None
	586  999529852.0                            1-2-3 Regnskap AS  ...        False                                      None

	[587 rows x 14 columns]

	|                                  Finished                             |
'''