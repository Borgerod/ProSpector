import time; start = time.perf_counter() #Since it also takes time to Import libs, I allways start the timer asap. 
import requests 
import numpy as np
import pandas as pd 
import datetime as dt
from tqdm import tqdm

# ___ local imports __________
from postgres import cleanUp, fetchData, checkForTable, postLastUpdate, replacetData
from file_manager import *

def getTableName():
	return parseTablenames(getFileName())

def getCurrentData():
	return dt.datetime.now().date()

def getDateDiff():
	return getCurrentData() - dt.datetime.strptime(getLastUpdate(col_name='brreg_table'), '%Y-%m-%d').date()

def downloadJSON(json_file_name, url):
    """
    	Helper method handling downloading large files from `url` to `filename`. Returns a pointer to `filename`.
    """
    chunk_size = 1024
    r = requests.get(url, stream=True)
    with open(f'{json_file_name}', 'wb') as f:
    # with open('enheter_alle.json.gz', 'wb') as f:
        pbar = tqdm( unit="B", total=int( r.headers['Content-Length'] ) )
        for chunk in r.iter_content(chunk_size = chunk_size): 
            if chunk: # filter out keep-alive new chunks
                pbar.update (len(chunk))
                f.write(chunk)

def jsonDataframe(data):
	return pd.read_json(data)

def datasetEditor(df):
	'''
		drops columns not in keep_list, then renames columns from BRREG dataset  
	'''
	keep_list = np.array([ 'organisasjonsnummer', 'navn', 'registreringsdatoEnhetsregisteret', 'mva_registrert',
					       'antallAnsatte', 'registrertIForetaksregisteret', 'registrertIStiftelsesregisteret',
					       'registrertIFrivillighetsregisteret', 'konkurs', 'underAvvikling',
					       'underTvangsavviklingEllerTvangsopplosning', 'maalform', 'hjemmeside',
					       'stiftelsesdato', 'sisteInnsendteAarsregnskap'])

	df = df[df.columns.intersection(keep_list)]
	return df.rename(columns = {	'organisasjonsnummer':'org_num',
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
									'sisteInnsendteAarsregnskap':'siste_innsendt_årsregnskap',})

def resetInputTable():
	'''
		used mainly for testing, 
		it disregards the changes that 'removeExtracted()' has done, 
		and renews input_table from brreg_table
	'''
	print("	resetting input_table..")
	brreg = fetchData(tablename = "brreg_table")
	brreg = brregCleanUp(brreg)
	input_table = brreg[['org_num', 'navn']]
	print(f" removing output_table data from input_table")
	output_table = fetchData(tablename = "google_input_table")
	output_table = output_table[['org_num', 'navn']]
	df = pd.concat([output_table, input_table], axis=0)
	df = df.drop_duplicates(subset = 'org_num', keep=False)
	df = df.reset_index(drop=True)
	replacetData(df, tablename = "input_table")
	print("	reset complete.")
	print(f'new length of input_table: {len(df)}')
	print(f'Display results:\n\n{df}\n\n')

def brregCleanUp(df):
	'''
		a clean up routine specifically made for "brreg_table", before it is uploaded to "input_table".
		function is called by: resetInputTable()
		the routine:
			removes companies that is tagged; bankrupt, disolved, liquidated, (might include "last annual report == None")
	'''
	return df.loc[(df['under_avvikling'] == False) & (df['under_tvangsavvikling_eller_oppløsning'] == False) & (df['konkurs'] == False)]

def downloadWholeDataset(tablename, json_file_name, action):
	print("_"*91)
	print("|			Starting: Brønnøysund Register Extractor 			  |")
	print("_"*91)
	print()	

	url = f'https://data.brreg.no/enhetsregisteret/api/{action}'
	
	print("downloading file..")
	downloadJSON(json_file_name, url)
	print("    downloading complete") 

	print("making dataframe..")
	df = jsonDataframe(data = json_file_name)
	print(f'{df}\n')	
	print("    dataframe complete")
	print()

	print("editing dataframe..")
	df = datasetEditor(df)
	print(f'{df}\n')	
	print("    editing complete")
	print()

	print("uploading to database..")
	replacetData(df, tablename)
	print('    upload complete')
	print()


	resetInputTable()
	print()

	'''	! Optional 
		fetches and displays results 
	'''
	db_table = fetchData(tablename)
	print(f'Display results:\n\n{db_table}\n\n')
	print()

	print("cleaning database..")
	cleanUp(tablename)
	print("    cleaning complete")
	

	print("_"*62)
	print(f"		    Update Complete. 			  ")
	print(f"		Finished in {round(time.perf_counter() - start, 2)} second(s)				  ")
	print("_"*62)
	print()

''' 
	* ____  MAIN  ________________________________
'''
def brregExtractor():

	''' 
		Decide wether to download or not
		Checks if table exsist, then checks if its tiem for an update. 
	'''
	tablename = getTableName()
	json_file_name = 'enheter_alle.json.gz'
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

if __name__ == '__main__':		
	brregExtractor()
