''' TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP  TEMP TEMP TEMP TEMP TEMP TEMP TEMP  TEMP TEMP TEMP TEMP TEMP TEMP TEMP  TEMP TEMP TEMP TEMP TEMP TEMP TEMP '''
'''	

#> NEW GOOGLE.PY AFTER NOTES FROM MEETING WITH DANIEL KARLSEN
	- [ ] add address and postnumber and place insted of "maps" in search term 
	- [ ] get address from brreg.py


'''
''' TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP  TEMP TEMP TEMP TEMP TEMP TEMP TEMP  TEMP TEMP TEMP TEMP TEMP TEMP TEMP  TEMP TEMP TEMP TEMP TEMP TEMP TEMP '''

import json
import time

from sqlalchemy import create_engine
# from actions.db_query import Table

# from SQL.core.session import get_db, getSession; start = time.perf_counter() #Since it also takes time to Import libs, I allways start the timer asap. 
import requests 
import numpy as np
import pandas as pd 
import datetime as dt
from tqdm import tqdm

# ___ local imports __________
from SQL.postgres import cleanUp, fetchData, postLastUpdate, replacetData, insertData
# from add_row import getSession #! SOON TO BE REPLACED 
from utilities.file_manager import *

# > import test (on behalf of file_manager) 
from SQL.core.__config import tablenames, settings


##! old (DISABLED)
# def getTableName() -> str:
# 	return parseTablenames(getFileName())



def getCurrentData() -> dt.datetime:
	return dt.datetime.now().date()

def getDateDiff() -> None:
	return getCurrentData() - dt.datetime.strptime(getLastUpdate(col_name='brreg_table'), '%Y-%m-%d').date()

def downloadJSON(json_file_name:str, url:str) -> None:
	"""
		Helper method handling downloading large files from `url` to `filename`. Returns a pointer to `filename`.
	"""
	chunk_size = 1024
	r = requests.get(url, stream=True)
	with open(f'{json_file_name}', 'wb') as f:
		pbar = tqdm( unit="B", total=int( r.headers['Content-Length'] ) )
		for chunk in r.iter_content(chunk_size = chunk_size): 
			if chunk: # filter out keep-alive new chunks
				pbar.update (len(chunk))
				f.write(chunk)

def jsonDataframe(data: json) -> pd.DataFrame:
	return pd.read_json(data)

def datasetEditor(brreg_table) -> pd.DataFrame:
	'''
		Makes Dataframe from brreg Json file, picks out desiered columns, returns "dirty" df 
		drops columns not in keep_list, then renames columns from BRREG dataset  
			
			will return ==> brreg_table, input_table 

	'''
	# brreg_table = brreg_table[[		
	# 	'organisasjonsnummer', 
	# 	'navn',
	# 	'konkurs', 
	# 	'underAvvikling',
	# 	'underTvangsavviklingEllerTvangsopplosning',
	# 	'postadresse',
	# 	'forretningsadresse',
	# 	]]
	brreg_table = brreg_table[[
		'organisasjonsnummer', 
		'navn', 
		'postadresse',
		'forretningsadresse',
		'registreringsdatoEnhetsregisteret', 
		'mva_registrert',
		'antallAnsatte', 
		'registrertIForetaksregisteret', 
		'registrertIStiftelsesregisteret',
		'registrertIFrivillighetsregisteret', 
		'konkurs',
		'underAvvikling',
		'underTvangsavviklingEllerTvangsopplosning', 
		'hjemmeside',
		'stiftelsesdato', 
		'sisteInnsendteAarsregnskap'
		]]
	brreg_table.rename(columns = {	'organisasjonsnummer':'org_num',
									'navn':'navn',
									'postadresse':'postadresse',
									'forretningsadresse':'forretningsadresse',
									'registreringsdatoEnhetsregisteret':'registreringsdato',
									'registrertIMvaregisteret':'mva_registrert',
									'antallAnsatte':'antall_ansatte',
									'registrertIForetaksregisteret':'foretaks_registeret',
									'registrertIStiftelsesregisteret':'stiftelses_registeret',
									'registrertIFrivillighetsregisteret':'frivillighets_registeret',
									'konkurs':'konkurs',
									'underAvvikling':'under_avvikling',
									'underTvangsavviklingEllerTvangsopplosning':'under_tvangsavvikling_eller_oppløsning',
									'hjemmeside':'hjemmeside',
									'stiftelsesdato':'stiftelsesdato',
									'sisteInnsendteAarsregnskap':'siste_innsendt_årsregnskap',
									})

	# dumping dictionaries to df 
	brreg_table['postadresse'] = brreg_table['postadresse'].apply(json.dumps)
	brreg_table['forretningsadresse'] = brreg_table['forretningsadresse'].apply(json.dumps)
	brreg_table = brregCleanUp(brreg_table) # Removes all rows which is bankrupt etc.

	# making input_table (input_table is a simplified version of brreg_table)
	input_table = brreg_table[['org_num', 'navn', 'postadresse', 'forretningsadresse',]]
	return brreg_table, input_table

def brregCleanUp(brreg_table):
	'''
		a clean up routine specifically made for "brreg_table", before it is uploaded to "input_table".
		function is called by: resetInputTable()
		the routine:
			removes companies that is tagged; bankrupt, disolved, liquidated, (might include "last annual report == None")
	'''
	return brreg_table.loc[(brreg_table['under_avvikling'] == False) & (brreg_table['under_tvangsavvikling_eller_oppløsning'] == False) & (brreg_table['konkurs'] == False)]


#* __________ CURRENT WORKSPACE ______________________________________________________________________________________________________

import ast
def makeInputTableFromBrregTable():
	'''
	fetches "dirty" brreg_table from postgres
	trims the table, usign only the nessasary columns for faster query
	finally makes input_table 
	'''
	brreg_table = fetchData(tablename = 'brreg_table')
	# print(brreg_table)
	
	# brreg_table = brreg_table.iloc[:5]
	forretningsadresse_ = brreg_table['forretningsadresse']
	adresse_short = []

	for forretningsadresse in forretningsadresse_:
		forretningsadresse = ast.literal_eval(forretningsadresse)
		adresse_short_ = forretningsadresse['adresse']
		print(adresse_short_)
		adresse_short.append([adresse_short_])
	# adresse_df = pd.DataFrame(adresse_short)	
	adresse_df = pd.DataFrame(adresse_short, columns=['adresse_short'])	
	# print(adresse_df)
	#TEMP while testing 
	input_table = brreg_table[[
		'organisasjonsnummer', 
		'navn', 
		# 'postadresse',
		'forretningsadresse',
		]]
	input_table = pd.concat([input_table, adresse_df], axis=1)
	# print(input_table)
	
	
	# input_table.rename(columns = { 
	# 	'organisasjonsnummer':'org_num', 
	# 	'navn':'navn', 
	# 	# 'postadresse':'postadresse',
	# 	'forretningsadresse':'forretningsadresse',
	# })
	#* THIS WILL REPLACE TEMP AFTER CHANGES
	# input_table = brreg_table[['org_num', 'navn', 'postadresse', 'forretningsadresse',]]
	
	# print(input_table)

	# INSERTING input_table TO POSTGRES using insertData()
	# cleanUp, postLastUpdate, replacetData, 

	# insertData(df=input_table, tablename='input_table')


	# insertData(df=input_table, tablename='input_table_test')
	replacetData(df=input_table, tablename='input_table')
	



#TEMP cutout from postgres
# session = getSession()
# engine = create_engine(settings.DATABASE_URL)
# def getBrregTable() -> pd.DataFrame:
# 	''' simple get function for call_list
# 	'''
# 	return pd.read_sql_table(
# 		'brreg_table',
# 		con = engine
# 		)

# def makeInputTableFromBrregTable():
# 	brreg = getBrregTable()
# 	input_table = brreg[['org_num', 'navn', 'postadresse', 'forretningsadresse',]]
# 	print(input_table)


def makeBrregTableFromJson():
	brreg_table = jsonDataframe(data = r'utilities/enheter_alle.json.gz')
	print(brreg_table.iloc[0])
	
	# #TEMP while testing 
	# input_table = brreg_table[[
	# 	'organisasjonsnummer', 
	# 	'navn', 
	# 	'postadresse',
	# 	'forretningsadresse',
	# 	]]
	# input_table.rename(columns = { 
	# 	'organisasjonsnummer':'org_num', 
	# 	'navn':'navn', 
	# 	'postadresse':'postadresse',
	# 	'forretningsadresse':'forretningsadresse',
	# })
	# #* THIS WILL REPLACE TEMP AFTER CHANGES
	# # input_table = brreg_table[['org_num', 'navn', 'postadresse', 'forretningsadresse',]]
	
	# print(input_table)

	# # INSERTING input_table TO POSTGRES using insertData()
	# # cleanUp, postLastUpdate, replacetData, 

	# # insertData(df=input_table, tablename='input_table')


	# # insertData(df=input_table, tablename='input_table_test')
	# # replacetData(df=input_table, tablename='input_table')
	






#* _____________________________________________________________________________________________________________________________________


''' 
	* ____  MAIN  ________________________________
'''
def brregExtractor():

	''' 
		Decide wether to download or not
		Checks if table exsist, then checks if its tiem for an update. 
	'''
	# tablename = getTableName()
	json_file_name = 'enheter_alle.json.gz'
	
	''' #> temporatry disabled
		downloadWholeDataset(tablename, json_file_name, action = 'enheter/lastned')
		postLastUpdate(tablename)
		if not checkForTable(tablename):
			print(f" 	downloading please wait..")
			downloadWholeDataset(tablename, json_file_name, action = 'enheter/lastned')
			postLastUpdate(tablename)
		print("checking latest update..")
		if getDateDiff() >= dt.timedelta(days=7):
			print("	update needed\n 		updating please wait..")
			downloadWholeDataset(tablename, json_file_name, action = 'enheter/lastned')
			postLastUpdate(tablename)
		else:
			print("	no update needed")
		print("continuing to data extraction.")
		print("\n\n")
	'''
		
	makeInputTableFromBrregTable()

	

if __name__ == '__main__':	
	# makeBrregTableFromJson()	
	brregExtractor()

	# TEMP while testing 
	# checking if input_table exist:
	# input_table = fetchData(tablename = 'input_table')
	# print(input_table)







""" #! Old stuff (unsorted)
	# from models.brreg_table import BrregTable

	# class Brreg:
	# 	def __init__(self) -> None:
	# 		self.organisasjonsnummer = None
	# 		self.navn = None
	# 		self.konkurs = None
	# 		self.underAvvikling = None
	# 		self.underTvangsavviklingEllerTvangsopplosning = None
	# 		self.postadresse = None
	# 		self.forretningsadresse = None

	# 	def insertRowToBrreg(self,):
	# 		db  = get_db()
	# 		row = db.BrregTable(
	# 			self.organisasjonsnummer,
	# 			self.navn,
	# 			self.konkurs,
	# 			self.underAvvikling,
	# 			self.underTvangsavviklingEllerTvangsopplosning,
	# 			self.postadresse,
	# 			self.forretningsadresse,
	# 			)
	# 		self.addRowToDb(row, session = db)
		
	# 	def addRowToDb(self, row, session) -> str:
	# 		'''
	# 			will [a] try to add row to db, 
	# 			  or [b] replace row if "a" was unsuccsessfull.
	# 		'''
	# 		try:
	# 			session.add(row)
	# 			session.commit()
	# 		except:
	# 			session.rollback()
	# 			session.query(db.CallListTest).filter_by(org_num = self.org_num).delete()

"""


""" #! Old stuff 
	# class InputTable:

	# 	def makeInputTable(self):
	# 		db  = get_db()
	# 		row = db.BrregTable(   
	# 			self.org_num,
	# 			self.navn,
	# 			self.postadresse,
	# 			self.forretningsadresse,
	# 		)
	# 		Table('input_table').addRowToTable(row, session = db)

	# def resetInputTable():
	# 	# TODO NEEDS WORK 
	# 	'''
	# 		used mainly for testing, 
	# 		it disregards the changes that 'removeExtracted()' has done, 
	# 		and renews input_table from brreg_table
	# 	'''
	# 	print("	resetting input_table..")
	# 	brreg = fetchData(tablename = "brreg_table")
	# 	brreg = brregCleanUp(brreg)
	# 	input_table = brreg[['org_num', 'navn', 'postadresse', 'forretningsadresse',]]
	# 	print("skipping action: 'removing output_table data from input_table'")
	# 	# print(f" removing output_table data from input_table")
	# 	# output_table = fetchData(tablename = "google_input_table")
	# 	# output_table = output_table[['org_num', 'navn']]
	# 	# df = pd.concat([output_table, input_table], axis=0)
	# 	# df = df.drop_duplicates(subset = 'org_num', keep=False)
	# 	# df = df.reset_index(drop=True)
	# 	# replacetData(df, tablename = "input_table")
	# 	df = input_table
	# 	replacetData(df, tablename = "input_table")
	# 	print("	reset complete.")
	# 	print(f'new length of input_table: {len(df)}')
	# 	print(f'Display results:\n\n{df}\n\n')



	# def downloadWholeDataset(tablename, json_file_name, action):
		# print("_"*91)
		# print("|			Starting: Brønnøysund Register Extractor 			  |")
		# print("_"*91)
		# print()	

		# url = f'https://data.brreg.no/enhetsregisteret/api/{action}'
		
		# # print("downloading file..")
		# # downloadJSON(json_file_name, url)
		# # print("    downloading complete") 
		# # pd.options.display.max_rows = 10				# Rows 	   (length)
		# # pd.options.display.max_columns = None				# Columns  (width)
		# # pd.options.display.max_colwidth = None			# Columns  (column display border)
		# # pd.options.display.width = 2000		

		# print("making dataframe..")
		# df = jsonDataframe(data = json_file_name)
		
		# # print(f'{df}\n')	
		# # print("    dataframe complete \n\n")
		# # df = df.iloc[0]
		# # post = df.loc['postadresse']
		# # bedrift = df.loc['forretningsadresse']
		# # print()
		# # print(df)
		# # print("\n\n")
		# # print(post)
		# # print("\n\n")
		# # print(bedrift)
		# # print("\n\n")

		# print("editing dataframe..")
		# df = datasetEditor(df)
		# df = df.loc['organisasjonsnummer', 
		# 			'navn',
		# 			'postadresse',
		# 			'forretningsadresse',]
		# print(f'{df}\n')	
		# print("    editing complete \n")


		# try: 
		# print("    inserting df to db \n")
		# insertData(df, tablename='')
		# engine = create_engine(f'postgresql+psycopg2://postgres:Orikkel1991@local:5432/ProSpector_Dev')
		# df.to_sql('input_table', con=engine)


		# # replacetData(df, tablename='input_table')
		# # except:
		# 	# insertData(df, tablename='input_table')




		# # print("uploading to database..")
		# replacetData(df, tablename)
		# print('    upload complete')
		# print()

		# df print()
		# resetInputTable()
		# print()

		# # '''	! Optional 
		# # 	fetches and displays results 
		# # '''
		# db_table = fetchData(tablename)
		# print(f'Display results:\n\n{db_table}\n\n')
		# print()

		# print("cleaning database..")
		# # cleanUp(tablename)
		# print("    cleaning complete")
		

		# print("_"*62)
		# print(f"		    Update Complete. 			  ")
		# print(f"		Finished in {round(time.perf_counter() - start, 2)} second(s)				  ")
		# print("_"*62)
		# print()



"""

