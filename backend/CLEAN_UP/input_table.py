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
	try:
		input_table = fetchData(tablename = 'input_table')
	except:
		input_table=[]
	print(f'current length of input_table: {len(input_table)}')
	# time.sleep(0.5)
	if input("are you sure you want to reset input_table? (y/n)") == "y" or "Y" or "yes" or "Yes":
		print("	resetting input_table..")
		brreg = fetchData(tablename = "brreg_table")
		input_table = brreg[['org_num', 'navn']]
		replacetData(input_table, tablename = "input_table")
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
	# cleanUp(tablename = "input_table")
	input_table = fetchData(tablename = "input_table")
	try:
		output_table = fetchData(tablename = "output_table")
		output_table = output_table[['org_num', 'navn']]
	except:
		output_table = pd.DataFrame()
	print(f'current length of output_table: {len(output_table)}')
	print(f'current length of input_table: {len(input_table)}')

	
	df = pd.concat([output_table, input_table], axis=0)
	df = df.drop_duplicates(subset = 'org_num', keep=False)
	df = df.reset_index(drop=True)
	replacetData(df, tablename = "input_table")
	print(f'current length of output_table: {len(output_table)}')
	print(f'current length of input_table: {len(df)}')
