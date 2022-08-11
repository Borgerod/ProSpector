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
from postgres import databaseManager, getInputTable
from config import payload, tablenames
from file_manager import *




'''
PURPOSE: 
	make sures to update input_table
	
	...


'''

def inputTableManager():

	# FOR TESTING
	df = pd.DataFrame(columns = ['org_num', 'navn'])

	'''__commands__''' 
	input_data = getInputTable(tablenames['input_table'])	# gets current input table 
	# insertData(df, tablename)	# Either makes or for updates input table 

def inputTable():
	tablename = parseTablenames(getFileName())
	input_data = getInputTable(tablename)
	



if __name__ == '__main__':
	inputTableManager()

