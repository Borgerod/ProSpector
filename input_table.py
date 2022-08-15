import pandas as pd 
import numpy as np
import pandas as pd 
import json
import psycopg2
from psycopg2.extras import Json
from sqlalchemy import create_engine
import concurrent.futures
from inspect import currentframe, getframeinfo


# ___ local imports ________
from config import payload, tablenames, settings
from postgres import databaseManager, cleanUp, fetchData, checkForTable, postLastUpdate, deleteData ,insertData, replacetData
from file_manager import *




'''
PURPOSE: 
	make sures to update input_table
	
	...

'''

def resetInputTable():
	'''
		used mainly for testing, 
		it disregards the changes that 'removeExtracted()' has done, 
		and renews input_table from brreg_table
	'''
	input_table = fetchData(tablename = 'input_table')
	print(f'current length of input_table: {len(input_table)}')
	if input("are you sure you want to reset input_table? (y/n)") == "y" or "Y" or "yes" or "Yes":
		print("	resetting input_table..")
		brreg = fetchData(tablename = 'brreg_table')
		input_table = brreg[['org_num', 'navn']]
		replacetData(input_table, tablename = 'input_table')
		print("	reset complete.")
		print(f'new length of input_table: {len(input_table)}')

def inputTableManager(): #? Don't think this is in use

	# FOR TESTING
	df = pd.DataFrame(columns = ['org_num', 'navn'])

	'''__commands__''' 
	input_data = getInputTable(tablenames['input_table'])	# gets current input table 
	# insertData(df, tablename)	# Either makes or for updates input table 

def inputTable(): #? Don't think this is in use
	tablename = parseTablenames(getFileName())
	input_data = getInputTable(tablename)
	
def removeExtracted():
	'''
		removed companies from input_table that has been extracted by google and gulesider
	'''
	input_table = fetchData(tablename = 'input_table')
	gulesider =  fetchData(tablename = 'gulesider_table')
	google = fetchData(tablename = 'google_table')
	gulesider.org_num = gulesider.org_num.astype(int).astype(str)

	common1 = input_table.merge(google, on = ['org_num'])
	common2 = input_table.merge(gulesider, on = ['org_num'])
	to_be_removed = common1.merge(common2, on = ['org_num'])

	new_input_table = input_table[(~input_table.org_num.isin(to_be_removed.org_num))]
	new_input_table = new_input_table.reset_index(drop = True)
	print(new_input_table)
	insertData(new_input_table, tablename = 'input_table')

if __name__ == '__main__':
	resetInputTable()
	input_table = fetchData(tablename = 'input_table')
	print(f'current length of input_table: {len(input_table)}')











# def getLastUpdate(col_name):
# 	'''
# 		gets the date for when a table was last modified from update_tracker
# 		- "update_tracker" is a seperate small table that is updated after each sucsessfull run
		
# 		Note:  to avoid confusion, the variable "tablename" passed when calling getLastUpdate(tablename) is renamed to col_name, 
# 			   since fetchData() also uses "tablename"		
# 	'''
# 	df = fetchData(tablename = parseTablenames('update_tracker')) # fetches tablename for "update_tracker" from config, then fetchess df for database
# 	return df.iloc[0][col_name] # fetches date-cell for "col_name" returns -> str 

# status = getLastUpdate(col_name = ["google_table", "brreg_table", "gulesider_table",])

# from itertools import groupby

# def all_equal(iterable):
#     g = groupby(iterable)
#     return next(g, True) and not next(g, False)

# def uqualUpdateChecker():
# 	if not all_equal(status):
# 		''' RUN google.py & gulesider.py'''

# # def removeFromInput_table(org_num):
	


# def checkgoogleTable(org_num):
# 	if org_num in fetchData(tablename = 'google_table'):
# 		return 1
# 	else: 
# 		return 0

# def checkgulesiderTable(org_num):
# 	if org_num in fetchData(tablename = 'gulesider_table'):
# 		return 1
# 	else: 
# 		return 0

# def deleteFromInputTableChecker(org_num):
# 	google_status = checkgoogleTable(org_num)
# 	gulesider_status = checkgulesiderTable(org_num)
# 	if (google_status, gulesider_status) == 1:

# 		print(f'{org_num} has been scraped, deleting from iput_table')
# 		print(google_status, gulesider_status)
# 	else:
# 		print(f'{org_num} has NOT been scraped')
# 		print(google_status, gulesider_status)
# 		# pass

# def inputTableController():
# 	org_num = fetchData(tablename = 'input_table')['org_num']
# 	with concurrent.futures.ThreadPoolExecutor() as executor:
# 		list(executor.map(deleteFromInputTableChecker, org_num))

# inputTableController()





# # for i in input_snippet:
# 	# print(i)
# if input_snippet.isin(google.org_num):
# # if i isin google['org_num']:
# 	print(1)


# print()
# print()