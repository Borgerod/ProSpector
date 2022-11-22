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
# def insertData(df, tablename):
# 	''' 
# 		inserts final dataframe to database, 
# 		creates new table if table it does not exsist, else it updates
# 	'''
# 	conn = getConnection()
# 	curr = getCursor(conn)
# 	dbname, host, user, password = parseConfig()
# 	engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:5432/{dbname}')
# 	df.to_sql(f'{tablename}', engine, if_exists = 'replace', index = False)

# def fetchData(conn, tablename):
# 	''' fetches old_df from database '''
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

# 	df.set_index(['org_num'],  inplace = True)
# 	try: 
# 		df.drop('org_num', axis = 1, inplace=True)
# 	except KeyError:
# 		pass

# 	# print(old_df)
# 	# if old_df is np.ndarray:
# 	# 	old_df =S pd.DataFrame(my_array, columns = ['org_num', 'navn'])

# 	try:
# 		old_df.set_index(old_df['org_num'].squeeze(), inplace = True)
# 	except KeyError:
# 		old_df.set_index(old_df['org_num'], inplace = True)
# 	try: 
# 		old_df.drop('org_num', axis = 1, inplace=True)
# 	except KeyError:
# 		print("KeyError: old_df['org_num']")
# 	df = pd.concat((df, old_df), axis = 0)
# 	df = df.groupby(df.index).last().reset_index()
# 	return df

# ''' ___ MANAGER _______________________________________________ '''
# def databaseManager(df, tablename):
# 	dbname, host, user, password = parseConfig()
# 	conn = getConnection()
# 	''' manage database '''
# 	old_df = pd.DataFrame()
# 	try:
# 		conn = getConnection()
# 		old_df = fetchData(conn, tablename)
# 	except:
# 		print("table does not exsist")
# 	try: 
# 		df = concatData(df, old_df)
# 	except:
# 		print("unable to concat") 

# 	# df = concatData(df, old_df)

# 	insertData(df, tablename)	


# '''OLD getInputChunks() BEFORE CHANGED TO getInputTable()'''
# # def getInputChunks(tablename):
# 	# dbname, host, user, password = parseConfig()
# 	# conn = getConnection()

# 	# ''' fetches old_df from database '''
# 	# tablename = 'brreg_table'
# 	# # tablename = 'search_list'
# 	# curr = getCursor(conn)  
# 	# curr.execute(f"SELECT * FROM {tablename};") 
# 	# input_data = curr.fetchall()
# 	# column_names  = [desc[0] for desc in curr.description]
# 	# input_df = pd.DataFrame(input_data, columns = column_names)
# 	# input_df = input_df[['org_num', 'navn']] #for testing
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
# 	inputs = input_df.to_numpy()
# 	curr.close()
# 	conn.close()
# 	return inputs

# # if __name__ == '__main__':
