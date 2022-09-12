import time; start = time.perf_counter() #Since it also takes time to Import libs, I allways start the timer asap. 
import pandas as pd 
import requests 
import numpy as np
from tqdm import tqdm
import datetime as dt

# ___ local imports __________
from postgres import databaseManager, cleanUp, fetchData, checkForTable, postLastUpdate, replacetData
from file_manager import *


'''
TODO LIST:
	- [X] create downloader function 
	- [X] implement postgres code 
	- [X] check if current version works 
	- [X] Make Update function 
	- [ ] make documentation on "RUNDOWN OF THE PROGRAM", including what postgres.py does
	- [ ] make documentation on "NOTABLE FLAWS"
	- [ ] create function that drops all "unnessasary" companies

! ISSUE: 
	- [ ] something makes database double as big as it should be, fix it
'''


''' * ____ PREP ___________________________
'''
def getTableName():
	'''gets the name of the propriate table'''
	return parseTablenames(getFileName())

''' * ____ DATES ___________________________
'''
def getCurrentData():
	return dt.datetime.now().date()

def getDateDiff():
	return getCurrentData() - dt.datetime.strptime(getLastUpdate(col_name='brreg_table'), '%Y-%m-%d').date()

''' * ____ DOWNLOAD JSONFILE _____________________
'''

def downloadJSON(json_file_name, url):
    """
    	Helper method handling downloading large files from `url` to `filename`. Returns a pointer to `filename`.
    """
    chunkSize = 1024
    r = requests.get(url, stream=True)
    with open('enheter_alle.json.gz', 'wb') as f:
        pbar = tqdm( unit="B", total=int( r.headers['Content-Length'] ) )
        for chunk in r.iter_content(chunk_size = chunkSize): 
            if chunk: # filter out keep-alive new chunks
                pbar.update (len(chunk))
                f.write(chunk)

''' * ____  MAKE DATAFRAME  _______________________
'''

def jsonDataframe(data):
	''' normalized json data and makes dataframe '''
	try: 
		return pd.read_json(data)
	except:									#! this might be unnessasary 
		return pd.json_normalize(data)		#! this might be unnessasary

def datasetEditor(df):
	'''
		drops columns not in keep_list, then renames columns from BRREG dataset  
	'''
	# * [NEW] keep_list 
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

''' * ____  INPUT TABLE  _______________________
'''

def updateInput_table(tablename, df2):
	'''
		makes a new dataframe from all the differences between old brreg_table and new brreg_table, then adds them to input_table.
		ande only keeps the 'org_num' & 'navn' columns
	'''
	#! I feel like something is missing here
	#! maybe tablename should be "tablename='input_table"
	df1 = fetchData(tablename)
	new = df2[~(df1.org_num.isin(df2.org_num))&(~df1.company_name.isin(df2.company_name))]
	databaseManager(new, 'input_table') 
	# databaseManager(df, 'input_table') 

# ! ATTENTION: This is imported from input_table.py 
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
	output_table = fetchData(tablename = "output_table")
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
	'''
		Query for siste_innsendt_årsregnskap if needed:
			regnskap = df.loc[df['siste_innsendt_årsregnskap'].isnull()]
	'''
	'''
		the inverse, if ever needed:
		trash = df.loc[(df['under_avvikling'] == True) | (df['under_tvangsavvikling_eller_oppløsning'] == True) | (df['konkurs'] == True)]
	'''
	return df.loc[(df['under_avvikling'] == False) & (df['under_tvangsavvikling_eller_oppløsning'] == False) & (df['konkurs'] == False)]




''' * ____  MANAGER  ________________________________
'''
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
	

	'''
		! Having issues with this 
	'''
	# updateInput_table(tablename, df2=df)

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


''' * ____  MAIN  ________________________________
'''
def brregExtractor():

	''' 
		Decide wether to download or not
		Checks if table exsist, then checks if its tiem for an update. 
	'''
	# print("_"*91)
	# print("|			Starting: Brønnøysund Register Extractor 			  |")
	# print("_"*91)
	# print()	


	print("_"*62)
	print("|          Starting: Brønnøysund Register Extractor          |")
	print("_"*62)
	print()
	tablename = getTableName() # fetches the appropriate tablename for current file
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




''' [OLD] '''
	# total_elements = gettotalElements() # gets total elements of dataset from api 
	# json_file_name = 'enheter_alle.json.gz' #FIXME --> TEMP while testing
	# # FIXME [DISABLED while testing] downloadJSON()
	# 	# print("downloading file..")
	# 	# downloadJSON(json_file_name)	# DISABLED
	# 	# print("    downloading complete")
	# # ?  [TEMP CUT OUT] readDataset() [might not be needed]
	# 	# print("reading dataset..")
	# 	# data = readDataset(json_file = json_file_name)
	# 	# print("    reading complete")
	

	# print("making dataframe..")
	# data = json_file_name #FIXME --> TEMP while testing
	# df = jsonDataframe(data)
	# print(df)
	# print("    dataframe complete")
	

	# print("uploading to database..")
	# databaseManager(df, tablename)
	# print('    upload complete')


	# # ?  [TEMP CUT OUT] cleanUp() [might not be needed]
	# 	# print("cleaning table..")
	# 	# cleanUp(tablename)
	# 	# print("    cleaning complete")
	

	# print(f'Display results:\n\n{df}\n\n')
	# db_table = fetchData(tablename)
	# print(db_table)	
	# print(f'|				   Finished in: {round(time.perf_counter() - start, 2)} second(s)				  |')

 # OUTPUT FROM CURRENT RUN [11.08.2022]:
		# C:\Users\Big Daddy B\OneDrive\GitHub\Mediavest_Scraper_bot>python brreg.py
		# False
		# enheter_alle.json.gz
		# checking if brreg_table exists:
		#     table; brreg_table exist
		# table_exists = True
		#  STAND-IN for updateDataBase()

		# C:\Users\Big Daddy B\OneDrive\GitHub\Mediavest_Scraper_bot>python brreg.py
		# False
		# enheter_alle.json.gz
		# checking if brreg_table exists:
		#     Error: table brreg_table does not exist
		# table_exists = False
		# ___________________________________________________________________________________________
		# |                       Starting: Brønnøysund Register Extractor                          |
		# ___________________________________________________________________________________________

		# making dataframe..
		#          organisasjonsnummer                                               navn                                  organisasjonsform  ... frivilligMvaRegistrertBeskrivelser  overordnetEnhet naeringskode3
		# 0                  922924368  - A THOUSAND WORDS - ØDEGÅRDEN GJERRUD TRANSLA...  {'kode': 'ENK', 'beskrivelse': 'Enkeltpersonfo...  ...                                NaN              NaN           NaN
		# 1                  911963582                - TTT- WINES TORE EUGEN KRISTIANSEN  {'kode': 'ENK', 'beskrivelse': 'Enkeltpersonfo...  ...                                NaN              NaN           NaN
		# 2                  988539473                              -EBE- DATA Eyolf Berg  {'kode': 'ENK', 'beskrivelse': 'Enkeltpersonfo...  ...                                NaN              NaN           NaN
		# 3                  913460197                                          -MINUS AS  {'kode': 'AS', 'beskrivelse': 'Aksjeselskap', ...  ...                                NaN              NaN           NaN
		# 4                  922936919                 -VEIEN- MED ANITA HELLEBØ-STOREIDE  {'kode': 'ENK', 'beskrivelse': 'Enkeltpersonfo...  ...                                NaN              NaN           NaN
		# ...                      ...                                                ...                                                ...  ...                                ...              ...           ...
		# 1077928            998858135                                    OLAV LILLESKARE  {'kode': 'ENK', 'beskrivelse': 'Enkeltpersonfo...  ...                                NaN              NaN           NaN
		# 1077929            995928825                                         POLYBOS AS  {'kode': 'AS', 'beskrivelse': 'Aksjeselskap', ...  ...                                NaN              NaN           NaN
		# 1077930            996001997                                    PRESTEGÅRDEN AS  {'kode': 'AS', 'beskrivelse': 'Aksjeselskap', ...  ...     [Utleier av bygg eller anlegg]              NaN           NaN
		# 1077931            998195675  RAYMA AGENTURER, SUKKERSPINNBODEN.NO RAYMOND M...  {'kode': 'ENK', 'beskrivelse': 'Enkeltpersonfo...  ...                                NaN              NaN           NaN
		# 1077932            999590985                                    SAKURA SUSHI AS  {'kode': 'AS', 'beskrivelse': 'Aksjeselskap', ...  ...                                NaN              NaN           NaN

		# [1077933 rows x 25 columns]

		#     dataframe complete

		# editing dataframe..
		#            org_num                                               navn registreringsdato  mva_registrert  ...  maalform             hjemmeside  stiftelsesdato  siste_innsendt_årsregnskap
		# 0        922924368  - A THOUSAND WORDS - ØDEGÅRDEN GJERRUD TRANSLA...        2019-06-19            True  ...    Bokmål                    NaN             NaN                         NaN
		# 1        911963582                - TTT- WINES TORE EUGEN KRISTIANSEN        2013-05-25           False  ...    Bokmål                    NaN             NaN                         NaN
		# 2        988539473                              -EBE- DATA Eyolf Berg        2005-08-20           False  ...    Bokmål       www.ebe-data.com             NaN                         NaN
		# 3        913460197                                          -MINUS AS        2014-04-03            True  ...    Bokmål                    NaN      2014-03-05                      2020.0
		# 4        922936919                 -VEIEN- MED ANITA HELLEBØ-STOREIDE        2019-06-21           False  ...    Bokmål                    NaN             NaN                         NaN
		# ...            ...                                                ...               ...             ...  ...       ...                    ...             ...                         ...
		# 1077928  998858135                                    OLAV LILLESKARE        2012-09-20            True  ...   Nynorsk                    NaN             NaN                         NaN
		# 1077929  995928825                                         POLYBOS AS        2010-10-23            True  ...    Bokmål                    NaN      2010-10-01                      2021.0
		# 1077930  996001997                                    PRESTEGÅRDEN AS        2010-09-30           False  ...    Bokmål  www.tuneprestegard.no      2010-09-01                      2019.0
		# 1077931  998195675  RAYMA AGENTURER, SUKKERSPINNBODEN.NO RAYMOND M...        2012-04-02           False  ...    Bokmål                    NaN             NaN                         NaN
		# 1077932  999590985                                    SAKURA SUSHI AS        2013-01-28           False  ...    Bokmål                    NaN      2013-01-01                      2019.0

		# [1077933 rows x 15 columns]

		#     editing complete

		# uploading to database..
		#     upload complete

		# Display results:

		#            org_num                                               navn registreringsdato  mva_registrert  ...  maalform             hjemmeside  stiftelsesdato  siste_innsendt_årsregnskap
		# 0        922924368  - A THOUSAND WORDS - ØDEGÅRDEN GJERRUD TRANSLA...        2019-06-19            True  ...    Bokmål                    NaN             NaN                         NaN
		# 1        911963582                - TTT- WINES TORE EUGEN KRISTIANSEN        2013-05-25           False  ...    Bokmål                    NaN             NaN                         NaN
		# 2        988539473                              -EBE- DATA Eyolf Berg        2005-08-20           False  ...    Bokmål       www.ebe-data.com             NaN                         NaN
		# 3        913460197                                          -MINUS AS        2014-04-03            True  ...    Bokmål                    NaN      2014-03-05                      2020.0
		# 4        922936919                 -VEIEN- MED ANITA HELLEBØ-STOREIDE        2019-06-21           False  ...    Bokmål                    NaN             NaN                         NaN
		# ...            ...                                                ...               ...             ...  ...       ...                    ...             ...                         ...
		# 1077928  998858135                                    OLAV LILLESKARE        2012-09-20            True  ...   Nynorsk                    NaN             NaN                         NaN
		# 1077929  995928825                                         POLYBOS AS        2010-10-23            True  ...    Bokmål                    NaN      2010-10-01                      2021.0
		# 1077930  996001997                                    PRESTEGÅRDEN AS        2010-09-30           False  ...    Bokmål  www.tuneprestegard.no      2010-09-01                      2019.0
		# 1077931  998195675  RAYMA AGENTURER, SUKKERSPINNBODEN.NO RAYMOND M...        2012-04-02           False  ...    Bokmål                    NaN             NaN                         NaN
		# 1077932  999590985                                    SAKURA SUSHI AS        2013-01-28           False  ...    Bokmål                    NaN      2013-01-01                      2019.0

		# [1077933 rows x 15 columns]


		#            org_num                                               navn registreringsdato  mva_registrert  ...  maalform             hjemmeside  stiftelsesdato  siste_innsendt_årsregnskap
		# 0        922924368  - A THOUSAND WORDS - ØDEGÅRDEN GJERRUD TRANSLA...        2019-06-19            True  ...    Bokmål                   None            None                         NaN
		# 1        911963582                - TTT- WINES TORE EUGEN KRISTIANSEN        2013-05-25           False  ...    Bokmål                   None            None                         NaN
		# 2        988539473                              -EBE- DATA Eyolf Berg        2005-08-20           False  ...    Bokmål       www.ebe-data.com            None                         NaN
		# 3        913460197                                          -MINUS AS        2014-04-03            True  ...    Bokmål                   None      2014-03-05                      2020.0
		# 4        922936919                 -VEIEN- MED ANITA HELLEBØ-STOREIDE        2019-06-21           False  ...    Bokmål                   None            None                         NaN
		# ...            ...                                                ...               ...             ...  ...       ...                    ...             ...                         ...
		# 1077928  998858135                                    OLAV LILLESKARE        2012-09-20            True  ...   Nynorsk                   None            None                         NaN
		# 1077929  995928825                                         POLYBOS AS        2010-10-23            True  ...    Bokmål                   None      2010-10-01                      2021.0
		# 1077930  996001997                                    PRESTEGÅRDEN AS        2010-09-30           False  ...    Bokmål  www.tuneprestegard.no      2010-09-01                      2019.0
		# 1077931  998195675  RAYMA AGENTURER, SUKKERSPINNBODEN.NO RAYMOND M...        2012-04-02           False  ...    Bokmål                   None            None                         NaN
		# 1077932  999590985                                    SAKURA SUSHI AS        2013-01-28           False  ...    Bokmål                   None      2013-01-01                      2019.0

		# [1077933 rows x 15 columns]


		# |                                  Finished in: 84.96 second(s)                           |


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

# [TRASH] from updateDataBase()
	# 	# df = updateAPI(url)
	# 	# print(f'{df}\n')	
	# 	# print("    dataframe complete")
	# 	# print()


	# 	# ''' * ANNBEFALING FRA BRREG IHT OPPDATERING
	# 	# 	Vi anbefaler følgende bruk: Filtrer på dato for første gangs uthenting, slik at man unngår enheter tidligere enn eventuell siste kopi. 
	# 	# 	Filtrer så på updateid for å hente neste sett av resultater. (Her kan man trygt bruke updateid+1). 
	# 	# 	Page+size kan benyttes for mer presis navigering i en updateid- eller dato-spørring.
		
	# 	# 	PAGINERING
	# 	# 		Det er mulig å filtrere og bla gjennom resultatsettet via page+size, dato og/eller updateid, men med visse begrensninger. 
	# 	# 		(Page+1)*size kan ikke overskride 10 000 og det kan finnes flere elementer med samme dato. Updateid kan bare forekomme en gang, 
	# 	# 		men disse er gjenbrukt på tvers av underenheter og enheter og kan ha gap på flere tusen id’er.
	# 	# '''


	# 	# print("making dataframe..")
	# 	# data = json_file_name #FIXME --> [TEMP] while testing
	# 	# df = jsonDataframe(data = json_file_name)
	# 	# print(f'{df}\n')	
	# 	# print("    dataframe complete")
	# 	# print()

	# 	# print("editing dataframe..")
	# 	# df = datasetEditor(df)
	# 	# print(f'{df}\n')	
	# 	# print("    editing complete")
	# 	# print()
		
	# 	# print("uploading to database..")
	# 	# databaseManager(df, tablename)
	# 	# print('    upload complete')
	# 	# print()

	# 	# print(f'Display results:\n\n{df}\n\n')
	# 	# db_table = fetchData(tablename)
	# 	# print(f'{db_table}\n')	
	# 	# print()

	# 	# # cleanup; check for duplicates
	# 	# # TODO: insert this 
	# 	# print("_"*91)
	# 	# print(f"|			Update Complete. 			  |")
	# 	# print(f"|			Finished in {round(time.perf_counter() - start, 2)} second(s)				  |")
	# 	# print("_"*91)
	# 	# print()