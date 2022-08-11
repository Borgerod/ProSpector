'''* TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP 
-							
-							_____ WHERE I LEFT OF _____
-						[10.08.22]
-						About to make an Update function 
-						ATM it seems like i need two seperate functions for "download whole dataset" and "update dataset"
-
- TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP '''

import time; start = time.perf_counter() #Since it also takes time to Import libs, I allways start the timer asap. 
import pandas as pd 
import requests 
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd 
import json
import psycopg2
from psycopg2.extras import Json
from sqlalchemy import create_engine
import concurrent.futures
from tqdm import tqdm

# ___ local imports __________
from config import payload, tablenames, settings
from postgres import databaseManager, cleanUp, fetchData
from file_manager import *

import json
import gzip
import pandas as pd 
import pprint
import ast


'''
TODO LIST:
	- [X] create downloader function 
	- [X] implement postgres code 
	- [ ] check if current version works 
	- [ ] Make Update function 
	- [ ] make documentation on "RUNDOWN OF THE PROGRAM", including what postgres.py does
	- [ ] make documentation on "NOTABLE FLAWS"
'''


''' * ____ API REQUEST ___________________________
'''

def getRequest():
	''' simple get request based on next_page -> json_dict '''
	url = f'https://data.brreg.no/enhetsregisteret/api/enheter/?page=0&size=20'
	return (requests.get(url, timeout = 10)).json()

def gettotalElements():
	''' 
		Not used in code.
		gets the total number of elements (Companies) from JSON, 
		used for supervising & calculations
	'''
	json_str = getRequest()
	return json_str['page']['totalElements']


''' * ____ DOWNLOAD JSONFILE _____________________
'''
def downloadJSON(json_file_name):
	with open('enheter_alle.json.gz', 'wb') as out_file:
		content = requests.get(url, stream=True).content
		out_file.write(content)

# FIXME : example of download with TQDM
# def download_file(url, filename):
    # """
    # Helper method handling downloading large files from `url` to `filename`. Returns a pointer to `filename`.
    # """
    # chunkSize = 1024
    # r = requests.get(url, stream=True)
    # with open(filename, 'wb') as f:
    #     pbar = tqdm( unit="B", total=int( r.headers['Content-Length'] ) )
    #     for chunk in r.iter_content(chunk_size=chunkSize): 
    #         if chunk: # filter out keep-alive new chunks
    #             pbar.update (len(chunk))
    #             f.write(chunk)
    # return filename

def readDataset(json_file):
	''' 
	imports dataset from a json.gz file (gz needs to be decoded)
	'''
	with gzip.open(json_file, 'r') as f:                        # 4. gzip --> unzips the json, removing ".gz" file from the json file  (gz = gzip)
		json_bytes = f.read()                                   # 3. bytes (i.e. UTF-8)
	json_str = json_bytes.decode('utf-8')                       # 2. dict   -> string   string (i.e. JSON)
	data = json.loads(json_str)                                 # 1. string -> json
	return data



''' * ____  MAKE DATAFRAME  _______________________
'''
def jsonDataframe(data):
	''' normalized json data and makes dataframe '''
	return pd.json_normalize(pd.read_json(data))
	## return pd.json_normalize(data)

def datasetEditor(df):
	'''
		drops columns not in keep_list, then renames columns from BRREG dataset  
	'''
	keep_list = np.array([	'organisasjonsnummer', 'navn', 'registreringsdatoEnhetsregisteret',
							'registrertIMvaregisteret', 'antallAnsatte', 'stiftelsesdato',
							'registrertIForetaksregisteret', 'registrertIStiftelsesregisteret',
							'registrertIFrivillighetsregisteret', 'sisteInnsendteAarsregnskap',
							'konkurs', 'underAvvikling',
							'underTvangsavviklingEllerTvangsopplosning', 'maalform',
							'organisasjonsform.kode', 'organisasjonsform.beskrivelse',
							'organisasjonsform._links.self.href', 'naeringskode1.beskrivelse',
							'naeringskode1.kode', 'forretningsadresse.land',
							'forretningsadresse.landkode', 'forretningsadresse.postnummer',
							'forretningsadresse.poststed', 'forretningsadresse.adresse',
							'forretningsadresse.kommune', 'forretningsadresse.kommunenummer',
							'institusjonellSektorkode.kode', 'institusjonellSektorkode.beskrivelse',
							'_links.self.href', 'postadresse.land', 'postadresse.landkode',
							'postadresse.postnummer', 'postadresse.poststed', 'postadresse.adresse',
							'postadresse.kommune', 'postadresse.kommunenummer', 'hjemmeside',])
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

# ? [TEMP CUT OUT] [might be used later]
	#* def downloadWholeDataset():
		# file_name = getFileName()	# fetches name of current file 
		# tablename = parseTablenames(file_name) # fetches the appropriate tablename for current file
		# settings = parseSettings(file_name)	# fetches the appropriate settings for current file
		# total_elements = gettotalElements()
		# url = 'https://data.brreg.no/enhetsregisteret/api/enheter/lastned' #FIXME --> TEMP while testing
		# json_file_name = 'enheter_alle.json.gz' #FIXME --> TEMP while testing

		# print("downloading file..")
		# downloadJSON(json_file_name)	# DISABLED
		# print("    downloading complete")
		# print("reading dataset..")
		# data = readDataset(json_file = json_file_name)
		# print("    reading complete")
		# print("making dataframe..")
		# data = json_file_name #FIXME --> TEMP while testing
		# df = jsonDataframe(data)
		# print("    dataframe complete")
		# print("uploading to database..")
		# databaseManager(df, tablename)
		# print("    upload complete")
		# print("cleaning table..")
		# # cleanUp(tablename)
		# print("    cleaning complete")
		# print(df) #FIXME --> TEMP while testing
		# print(f"|				   Finished in< {round(time.perf_counter() - start, 2)} second(s)				  |")
	
	#* def UpdateDataBase():
		# file_name = getFileName()	# fetches name of current file 
		# tablename = parseTablenames(file_name) # fetches the appropriate tablename for current file
		# settings = parseSettings(file_name)	# fetches the appropriate settings for current file

		# total_elements = gettotalElements()
		
		# json_file_name = 'enheter_alle.json.gz' #FIXME --> TEMP while testing
		# print("downloading file..")
		# downloadJSON(json_file_name)
		# print("    downloading complete")
		
		# print("reading dataset..")
		# data = readDataset(json_file = json_file_name)
		# print("    reading complete")
		
		# print("making dataframe..")
		# # tqdm.pandas(desc = 'making dataframe:') 
		#  #FIXME --> TEMP while testing
		# df = jsonDataframe(data = json_file_name)
		# # df.progress_apply(lambda x: x**2)
		# print("    dataframe complete")
		
		# print("uploading to database..")
		# databaseManager(df, tablename)
		# print("    upload complete")
		# print("cleaning table..")
		# # cleanUp(tablename)
		# print("    cleaning complete")
		# print(df) #FIXME --> TEMP while testing
		# print(f"|				   Finished in< {round(time.perf_counter() - start, 2)} second(s)				  |")




''' * ____  MAIN  ________________________________
'''
def brregExtractor(url):
	file_name = getFileName()	# fetches name of current file 
	tablename = parseTablenames(file_name) # fetches the appropriate tablename for current file
	settings = parseSettings(file_name)	# fetches the appropriate settings for current file
	total_elements = gettotalElements() # gets total elements of dataset from api 
	json_file_name = 'enheter_alle.json.gz' #FIXME --> TEMP while testing
	# FIXME [DISABLED while testing] downloadJSON()
		# print("downloading file..")
		# downloadJSON(json_file_name)	# DISABLED
		# print("    downloading complete")
	# ?  [TEMP CUT OUT] readDataset() [might not be needed]
		# print("reading dataset..")
		# data = readDataset(json_file = json_file_name)
		# print("    reading complete")
	

	print("making dataframe..")
	data = json_file_name #FIXME --> TEMP while testing
	df = jsonDataframe(data)
	print(df)
	print("    dataframe complete")
	

	print("uploading to database..")
	databaseManager(df, tablename)
	print('    upload complete')


	# ?  [TEMP CUT OUT] cleanUp() [might not be needed]
		# print("cleaning table..")
		# cleanUp(tablename)
		# print("    cleaning complete")
	

	print(f'Display results:\n\n{df}\n\n')
	db_table = fetchData(tablename)
	print(db_table)	
	print(f'|				   Finished in: {round(time.perf_counter() - start, 2)} second(s)				  |')
	

	''' ! OUTPUT FROM CURRENT RUN [11.08.2022]:
		
		downloading file..
		    downloading complete
		
		making dataframe..
		Empty DataFrame
		Columns: []
		Index: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
		? NOTE --> [SHOWING: print(df), line: 238]
		    dataframe complete
		
		uploading to database..
		    upload complete
		
		Display results: 
		Empty DataFrame
		Columns: []
		Index: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
		? NOTE --> [SHOWING: print(df), line: ??? -> might be "print(df)" from cleanUp (postgres.py)]

		Empty DataFrame
		Columns: []
		Index: [0, 1]
		? NOTE --> [SHOWING: print(db_table), line: 255]

		Finished in: {round(time.perf_counter() - start, 2)} second(s)
	'''


if __name__ == '__main__': 

	update_url = 'https://data.brreg.no/enhetsregisteret/api/oppdateringer/enheter'
	downlaod_url = 'https://data.brreg.no/enhetsregisteret/api/enheter/lastned'
	brregExtractor(url = downlaod_url)

	''' * ANNBEFALING FRA BRREG IHT OPPDATERING
		Vi anbefaler følgende bruk: Filtrer på dato for første gangs uthenting, slik at man unngår enheter tidligere enn eventuell siste kopi. 
		Filtrer så på updateid for å hente neste sett av resultater. (Her kan man trygt bruke updateid+1). 
		Page+size kan benyttes for mer presis navigering i en updateid- eller dato-spørring.
	'''






	''' * PAGINERING
		Det er mulig å filtrere og bla gjennom resultatsettet via page+size, dato og/eller updateid, men med visse begrensninger. 
		(Page+1)*size kan ikke overskride 10 000 og det kan finnes flere elementer med samme dato. Updateid kan bare forekomme en gang, 
		men disse er gjenbrukt på tvers av underenheter og enheter og kan ha gap på flere tusen id’er.
	'''

	''' [OLD] if __name__ == '__main__': 

		file_name = getFileName()	# fetches name of current file 
		tablename = parseTablenames(file_name) # fetches the appropriate tablename for current file
		settings = parseSettings(file_name)	# fetches the appropriate settings for current file

		total_elements = gettotalElements()
		
		json_file_name = 'enheter_alle.json.gz' #FIXME --> TEMP while testing
		print("downloading file..")
		# downloadJSON(json_file_name)	# DISABLED
		print("    downloading complete")
		print("reading dataset..")
		data = readDataset(json_file = json_file_name)
		print("    reading complete")
		print("making dataframe..")
		# tqdm.pandas(desc = 'making dataframe:') 
		data = json_file_name #FIXME --> TEMP while testing
		df = jsonDataframe(data)
		print(df)
		# df.progress_apply(lambda x: x**2)
		print("    dataframe complete")
		print("uploading to database..")
		databaseManager(df, tablename)
		print("    upload complete")
		print("cleaning table..")
		# cleanUp(tablename)
		print("    cleaning complete")
		print(df) #FIXME --> TEMP while testing
		print(f"|				   Finished in< {round(time.perf_counter() - start, 2)} second(s)				  |")


		df = fetchData(tablename)
		print(df)
	'''