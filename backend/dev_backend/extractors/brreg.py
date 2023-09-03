''' TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP  TEMP TEMP TEMP TEMP TEMP TEMP TEMP  TEMP TEMP TEMP TEMP TEMP TEMP TEMP  TEMP TEMP TEMP TEMP TEMP TEMP TEMP '''
'''	
This is used to make input_table
NOTE: This code is for the most part not in use except for fetching location info. 
Designed to be used once per quarter, year, oslt.


#> UNDER CONSTRUCTION


'''
''' TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP  TEMP TEMP TEMP TEMP TEMP TEMP TEMP  TEMP TEMP TEMP TEMP TEMP TEMP TEMP  TEMP TEMP TEMP TEMP TEMP TEMP TEMP '''



import json
import requests 
import numpy as np
import pandas as pd 
#> test 
from tqdm import tqdm
from multiprocessing import Pool 

''' ___ local imports ___'''
from SQL.insert import Insert
from SQL.reset import Reset



''' 
____ Track_record ____
	tot. time:  294.28s  (141.04s if .to_sql() is used) 	  
'''



class BrregExtractor:
	def __init__(self) -> None:
		self.url = f'https://data.brreg.no/enhetsregisteret/api/enheter/lastned'
		self.json_file_name = 'enheter_alle.json.gz'
		self.json_file_path = r'utilities/enheter_alle.json.gz'
		
	def downloadJSON(self) -> None:
		"""
			Helper method handling downloading large files from `url` to `filename`. Returns a pointer to `filename`.
		"""
		chunk_size = 1024
		r = requests.get(self.url, stream=True)
		# with open(f'{self.json_file_name}', 'wb') as f:
		with open(f'{self.json_file_path}', 'wb') as f:
			pbar = tqdm( unit = "B", total = int( r.headers['Content-Length'] ) )
			for chunk in r.iter_content(chunk_size = chunk_size): 
				if chunk: # filter out keep-alive new chunks
					pbar.update (len(chunk))
					f.write(chunk)

	def jsonToPandas(self) -> pd.DataFrame:
		return pd.read_json(self.json_file_path)

	def editDataSet(self, brreg_table:pd.DataFrame) -> pd.DataFrame:
		'''
			Makes Dataframe from brreg Json file, picks out desiered columns, returns "dirty" df 
			drops columns not in keep_list, then renames columns from BRREG dataset  
				
				will return ==> brreg_table, input_table 
		'''
		brreg_table = brreg_table[[
			'org_num', 
			'name', 
			'postadresse',
			'loc',
			'registreringsdatoEnhetsregisteret', 
			'registrertIMvaregisteret',
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
		brreg_table = brreg_table.rename(
			columns = {	
				'org_num':'org_num',
				'name':'name',
				'postadresse':'postadresse',
				'loc':'loc',
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
				}
			)
		
		# dumping dictionaries to df 
		brreg_table['postadresse'] = brreg_table['postadresse'].apply(json.dumps)
		brreg_table['loc'] = brreg_table['loc'].apply(json.dumps)
		
		return self.removeIrrelevantCompanies(brreg_table) 

	def removeIrrelevantCompanies(self, brreg_table:pd.DataFrame) -> pd.DataFrame:
		'''
			clean up routine that removes companies which is tagged; 
				bankrupt, disolved, liquidated, (might include "last annual report == None")
			function is called by: resetInputTable()
			the routine:
		'''
		return brreg_table.loc[(brreg_table['under_avvikling'] == False) & (brreg_table['under_tvangsavvikling_eller_oppløsning'] == False) & (brreg_table['konkurs'] == False)]

	def makeTables(self) -> pd.DataFrame:
		'''
		makes two DataFrames:
			- brreg_table; Dataframe containing all the data from brreg. (Currently not in use but will keep it for future use. )
			- input_table; Shorter version of brreg_table containing only the nessasary columns. (is smaller due to faster iteration.)
		'''
		brreg_table = self.jsonToPandas()
		brreg_table = self.editDataSet(brreg_table)
		return brreg_table, brreg_table[['org_num', 'name', 'loc',]]
	
	def insertToDb(self, row):
		Insert().toInputTable(row)

	def runExtraction(self) -> None:
		'''
		runs setup, then gets array of company names, then iterates through the list via ThreadPoolExecutor: extractionManager()
		stops process if Captcha is triggered, finally sends a df of results to database.
		'''
		self.downloadJSON()
		Reset().inputTable()
		brreg_table, input_table = self.makeTables()	
		
		
		array = input_table.to_numpy()
		with Pool() as pool:
			list(tqdm(pool.imap_unordered(self.insertToDb, array), total = len(array))) #294.28s
		
		'''NOTE:
			apparently pd.to_sql() is but for now i've decided to go with the Pool solution, 
			since then eveything looks uniform, and have less variation. 

			Here is the old code if i should change my mind: 
			
			input_table.to_sql('input_table', engine, if_exists='replace',) #! 141.04s
		'''
