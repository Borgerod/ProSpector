# import pandas as pd 
# import numpy as np
# import pandas as pd 
# import json
# import psycopg2
# from psycopg2.extras import Json
# from sqlalchemy import create_engine
# import concurrent.futures

# # ___ local imports ________
# # from config import google_payload, brreg_payload, CHUNK_SIZE
# from config import payload

# ''' ___ PREP _______________________________________________ '''
# def parseConfig():
# 	''' returns parsed payload from config file '''
# 	dbname = payload['dbname']
# 	host = payload['host']
# 	user = payload['user']
# 	password = payload['password']
# 	return dbname, host, user, password

# def getCursor(conn):
# 	''' returns postgres cursor '''
# 	return conn.cursor()

# def getConnection():
# 	dbname, host, user, password = parseConfig()
# 	''' connects to database '''
# 	return psycopg2.connect(
# 		dbname = dbname, 
# 		host = host, 
# 		user = user, 
# 		password = password)

# ''' ___ ACTIONS _______________________________________________ '''
# # def getInputTable(tablename):
# 	# ''' 
# 	# fucntion documentaion:
# 	# 	fetches an updated Input_List from database,
# 	# 	the extractors will base their searches on this list.

# 	# 	PS: table is returned as np.array. 
# 	# '''
# 	# dbname, host, user, password = parseConfig()
# 	# conn = getConnection()	
# 	# curr = getCursor(conn)  
# 	# curr.execute(f"SELECT * FROM {tablename};") 
# 	# input_data = curr.fetchall()
# 	# input_df = pd.DataFrame(input_data, columns = [desc[0] for desc in curr.description])
# 	# inputs = input_df.to_numpy()
# 	# curr.close()
# 	# conn.close()
# 	# return inputs

# def getInputTable(tablename):
# 	''' 
# 	fucntion documentaion:
# 		fetches an updated Input_List from database,
# 		the extractors will base their searches on this list.

# 		PS: table is returned as np.array. 
# 	'''
# 	dbname, host, user, password = parseConfig()
# 	conn = getConnection()	
# 	curr = getCursor(conn)  
# 	curr.execute(f"SELECT * FROM {tablename};") 
# 	input_data = curr.fetchall()
# 	input_df = pd.DataFrame(input_data, columns = [desc[0] for desc in curr.description])
# 	# inputs = input_df.to_numpy()
# 	curr.close()
# 	conn.close()
# 	return input_df


# def insertData(df, tablename):
# 	''' 
# 		inserts final dataframe to database, 
# 		creates new table if table it does not exsist, else it updates
# 	'''
# 	conn = getConnection()
# 	curr = getCursor(conn)
# 	dbname, host, user, password = parseConfig()
# 	engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:5432/{dbname}')
# 	df.to_sql(f'{tablename}', engine, if_exists = 'append', index = False)
	
# 	# df.to_sql(f'{tablename}', engine, if_exists = 'replace', index = False)
	
# 	# if tablename == 'brreg_table':
# 	# 	df.to_sql(f'{tablename}', engine, if_exists = 'append', index = False)
# 	# else:
# 	# 	df.to_sql(f'{tablename}', engine, if_exists = 'replace', index = False)



# def fetchData(tablename):
# 	''' fetches old_df from database '''
# 	conn = getConnection()
# 	dbname, host, user, password = parseConfig()
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
# 	try:
# 		old_df.set_index(old_df['org_num'].squeeze(), inplace = True)
# 	except KeyError:
# 		old_df.set_index(old_df['org_num'], inplace = True)
# 	try: 
# 		old_df.drop('org_num', axis = 1, inplace=True)
# 	except KeyError:
# 		pass
# 	try:
# 		df.set_index(['org_num'],  inplace = True)
# 	except:
# 		pass
# 	try: 
# 		df.drop('org_num', axis = 1, inplace=True)
# 	except KeyError:
# 		pass
# 	df = pd.concat((df, old_df), axis = 0)
# 	df = df.groupby(df.index).last().reset_index()
	
# 	return df

# def cleanUp(tablename):
# 	'''
# 		fetches table from database, drops duplicates (pandas), then replaces old table. 
# 		reason:
# 			the code works by; fetching old table, concat old table with new table, 
# 			finally insert concated table to db. current version of code does not properly 
# 			delete old table or drop duplicates when inserting the concated table. 
# 			This function makes sure that it happens. 	
# 	'''
# 	df = fetchData(tablename)
# 	df = df.drop_duplicates(subset = 'org_num')
# 	conn = getConnection()
# 	curr = getCursor(conn)
# 	dbname, host, user, password = parseConfig()
# 	engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:5432/{dbname}')
# 	df.to_sql(f'{tablename}', engine, if_exists = 'append', index = False)
# 	print(df)
# 	curr.close()
# 	conn.close()


# ''' ___ MANAGER _______________________________________________ '''
# def databaseManager(df, tablename):
# 	dbname, host, user, password = parseConfig()
# 	conn = getConnection()

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
# 	insertData(df, tablename)	
	


