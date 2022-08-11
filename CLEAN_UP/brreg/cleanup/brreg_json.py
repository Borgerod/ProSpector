import json
import gzip
import pandas as pd 
import pprint
import ast

inpt = {'http://example.org/about': {'http://purl.org/dc/terms/title':
                                     [{'type': 'literal', 'value': "Anna's Homepage"}]}}

json_data = ast.literal_eval(json.dumps(inpt))

print(type(json_data))



''' ____ USING: FULL DATASET ____________________________________________ '''
def getDataset(file):
	''' 
	imports dataset from a json.gz file (gz needs to be decoded)
	'''
	with gzip.open(file, 'r') as f:                             # 4. gzip --> unzips the json, removing ".gz" file from the json file  (gz = gzip)
		json_bytes = f.read()                                   # 3. bytes (i.e. UTF-8)
	json_str = json_bytes.decode('utf-8')                       # 2. dict   -> string   string (i.e. JSON)
	data = json.loads(json_str)                                 # 1. string -> json
	return data

def makeDataframe(data):
	return pd.json_normalize(data)
	
# TEMOPRARY DISABLED
if __name__ == '__main__':
	files = ['enheter_alle.json.gz','underenheter_alle.json.gz']
	data = getDataset(files[0])
	df = makeDataframe(data)
	print(df)




''' ____ USING: DATASET SNIPPET ____________________________________________ '''
def getDataSnippet():
	''' snippet from brreg dataset (data[0]) as a JSON (STRING) '''
	data_snippet = "{'organisasjonsnummer': '922924368', 'navn': '- A THOUSAND WORDS - ØDEGÅRDEN GJERRUD TRANSLATIONS', 'organisasjonsform': {'kode': 'ENK', 'beskrivelse': 'Enkeltpersonforetak', 'links': []}, 'registreringsdatoEnhetsregisteret': '2019-06-19', 'registrertIMvaregisteret': True, 'naeringskode1': {'beskrivelse': 'Oversettelses- og tolkevirksomhet', 'kode': '74.300'}, 'antallAnsatte': 0, 'forretningsadresse': {'land': 'Norge', 'landkode': 'NO', 'postnummer': '3060', 'poststed': 'SVELVIK', 'adresse': ['Storgaten 120'], 'kommune': 'DRAMMEN', 'kommunenummer': '3005'}, 'institusjonellSektorkode': {'kode': '8200', 'beskrivelse': 'Personlig næringsdrivende'}, 'registrertIForetaksregisteret': False, 'registrertIStiftelsesregisteret': False, 'registrertIFrivillighetsregisteret': False, 'konkurs': False, 'underAvvikling': False, 'underTvangsavviklingEllerTvangsopplosning': False, 'maalform': 'Bokmål', 'links': []}"
	return data_snippet 

def convertToJson(data_dict):
	''' convert: dict -> json (str) '''
	return json.dumps(data_dict)

def convertToDict(data_json):
	''' convert: json (str) -> dict '''
	return json.loads(data_json)

def ast_eval()


if __name__ == '__main__':
	data_snippet = getDataSnippet()             #data-type: JSON (string)
	data_dict = convertToDict(data_snippet)     #converts JSON -> dict
	# data_json = convertToJson(data_snippet)   #converts dict -> JSON
	





# '''
# 	___ POSTGRES TEST __________________________________________________________  
# 	GOAL OF TEST: 

# 		[1] successfully put "data_snippet" in the database.
# 			- convert to right format
# 			- drop & change column names
# 			- insert to database

# 		[2] Preferably: have python create a new table inside the database,
# 			based on the dataframe created from data_snippet <-- if the the datatable does not exsist 
# '''


# ''' ___ imports for: postgres ________ '''
# import json
# import psycopg2
# from psycopg2.extras import Json
 
# ''' ___ imports for: get json from path ________ '''
# import gzip
# import pandas as pd 
# import pprint


# # ''' ___ local imports ________ '''
# # from Config import payload  #Saving for later
# # print(payload)


# ''' TEMPORARY PAYLOAD REPLACEMENT: '''
# payload = { 'dbname'   : 'media_vest',
# 			'host'     : 'localhost',
# 			'user'     : 'postgres',
# 			'password' : 'Orikkel1991',
# 			'tablename': 'brreg_table',  }

# def parseConfig():
# 	dbname = payload['dbname']
# 	host = payload['host']
# 	user = payload['user']
# 	password = payload['password']
# 	tablename = payload['tablename']
# 	return dbname, host, user, password, tablename

# def getConnection():
# 	return psycopg2.connect(
# 		dbname = dbname, 
# 		host = host, 
# 		user = user, 
# 		password = password)

# def getCursor(conn):
# 	''''''
# 	return conn.cursor() # returns cursor

# def getDataSnippet():
# 	''' snippet from brreg dataset (data[0]) as a JSON (STRING) '''
# 	# data_snippet = "{'organisasjonsnummer': '922924368', 'navn': '- A THOUSAND WORDS - ØDEGÅRDEN GJERRUD TRANSLATIONS', 'organisasjonsform': {'kode': 'ENK', 'beskrivelse': 'Enkeltpersonforetak', 'links': []}, 'registreringsdatoEnhetsregisteret': '2019-06-19', 'registrertIMvaregisteret': True, 'naeringskode1': {'beskrivelse': 'Oversettelses- og tolkevirksomhet', 'kode': '74.300'}, 'antallAnsatte': 0, 'forretningsadresse': {'land': 'Norge', 'landkode': 'NO', 'postnummer': '3060', 'poststed': 'SVELVIK', 'adresse': ['Storgaten 120'], 'kommune': 'DRAMMEN', 'kommunenummer': '3005'}, 'institusjonellSektorkode': {'kode': '8200', 'beskrivelse': 'Personlig næringsdrivende'}, 'registrertIForetaksregisteret': False, 'registrertIStiftelsesregisteret': False, 'registrertIFrivillighetsregisteret': False, 'konkurs': False, 'underAvvikling': False, 'underTvangsavviklingEllerTvangsopplosning': False, 'maalform': 'Bokmål', 'links': []}"
# 	# NB !!!! skal egentlig være 46 columns
# 	data_snippet = {	'Organisasjonsnummer': '922924368',
# 						'Navn': '- A THOUSAND WORDS - ØDEGÅRDEN GJERRUD TRANSLATIONS',
# 						'Organisasjonsform.kode': 'ENK',
# 						'Organisasjonsform.beskrivelse': 'Enkeltpersonforetak',
# 						'Næringskode 1': '74.300',
# 						'Næringskode 1.beskrivelse': 'Oversettelses- og tolkevirksomhet',
# 						'Næringskode 2': '',
# 						'Næringskode 2.beskrivelse': '',
# 						'Næringskode 3': '',
# 						'Næringskode 3.beskrivelse': '',
# 						'Hjelpeenhetskode': '',
# 						'Hjelpeenhetskode.beskrivelse': '',
# 						'Antall ansatte': '0',
# 						'Hjemmeside': '',
# 						'Postadresse.adresse': '',
# 						'Postadresse.poststed': '',
# 						'Postadresse.postnummer': '',
# 						'Postadresse.kommune': '',
# 						'Postadresse.kommunenummer': '',
# 						'Postadresse.land': '',
# 						'Postadresse.landkode': '',
# 						'Forretningsadresse.adresse': 'Storgaten 120',
# 						'Forretningsadresse.poststed': 'SVELVIK',
# 						'Forretningsadresse.postnummer': '3060',
# 						'Forretningsadresse.kommune': 'DRAMMEN',
# 						'Forretningsadresse.kommunenummer': '3005',
# 						'Forretningsadresse.land': 'Norge',
# 						'Forretningsadresse.landkode': 'NO',
# 						'Institusjonell sektorkode': '8200',
# 						'Institusjonell sektorkode.beskrivelse': 'Personlig næringsdrivende',
# 						'Siste innsendte årsregnskap': '',
# 						'Registreringsdato i Enhetsregisteret': '2019-06-19',
# 						'Stiftelsesdato': '',
# 						'FrivilligRegistrertIMvaregisteret': '',
# 						'Registrert i MVA-registeret': 'JA',
# 						'Registrert i Frivillighetsregisteret': 'NEI',
# 						'Registrert i Foretaksregisteret': 'NEI',
# 						'Registrert i Stiftelsesregisteret': 'NEI',
# 						'Konkurs': 'NEI',
# 						'Under avvikling': 'NEI',
# 						'Under tvangsavvikling eller tvangsoppløsning': 'NEI',
# 						'Overordnet enhet i offentlig sektor': '',
# 						'Målform': 'Bokmål',}	
# 	return data_snippet 

# def convertToJson(data_dict):
# 	''' convert: dict -> json (str) '''
# 	return json.dumps(data_dict)

# def convertToDict(data_json):
# 	''' convert: json (str) -> dict '''
# 	return json.loads(data_json)

# def dataframeConverter(data_snippet):
# 	'''
# 		makes dataframe from dict data
# 	'''
# 	# return pd.read_json(data_snippet)
# 	return pd.json_normalize(data_snippet).T
# 	# return pd.DataFrame.from_dict(data_snippet, orient = 'index').T

# def datasetEditor(df):
# 	'''
# 		Drops unwanted columns, then renames the remaining columns. 
# 	'''
# 	# try:
# 	# 	df  = df.drop([
# 	# 		'Maalform', 
# 	# 		'Postadresse.land', 
# 	# 		'Postadresse.landkode',
# 	# 		'Postadresse.postnummer',
# 	# 		'Postadresse.poststed',
# 	# 		'Postadresse.adresse',
# 	# 		'Postadresse.kommune',
# 	# 		'Postadresse.kommunenummer',
# 	# 		'Naeringskode 2.beskrivelse',
# 	# 		'Naeringskode 2.kode',
# 	# 		'Naeringskode 2.hjelpeenhetskode',
# 	# 		'FrivilligRegistrertIMvaregisteret',
# 	# 		'Naeringskode 1.hjelpeenhetskode',
# 	# 		'Naeringskode 3.beskrivelse',
# 	# 		'Naeringskode 3.kode',
# 	# 		'Naeringskode 3.hjelpeenhetskode', 
# 	# 				# ], axis = 0, inplace = True)
# 	# 				], axis = 1)
# 	# except:
# 	# 	pass
# 	# try: 
# 	# 	df  = df.drop([
# 	# 		'Målform', 
# 	# 		'Postadresse.land', 
# 	# 		'Postadresse.landkode',
# 	# 		'Postadresse.postnummer',
# 	# 		'Postadresse.poststed',
# 	# 		'Postadresse.adresse',
# 	# 		'Postadresse.kommune',
# 	# 		'Postadresse.kommunenummer',
# 	# 		'Næringskode 2.beskrivelse',
# 	# 		'Næringskode 2.kode',
# 	# 		'Næringskode 2.hjelpeenhetskode',
# 	# 		'FrivilligRegistrertIMvaregisteret',
# 	# 		'Næringskode 1.hjelpeenhetskode',
# 	# 		'Næringskode 3.beskrivelse',
# 	# 		'Næringskode 3.kode',
# 	# 		'Næringskode 3.hjelpeenhetskode', 
# 	# 				# ], axis = 0, inplace = True)
# 	# 				], axis = 1)
# 	# except:
# 	# 	pass
# 	# try:
# 	# 	df  = df.drop([
# 	# 		'Målform', 
# 	# 		'Postadresse.land', 
# 	# 		'Postadresse.landkode',
# 	# 		'Postadresse.postnummer',
# 	# 		'Postadresse.poststed',
# 	# 		'Postadresse.adresse',
# 	# 		'Postadresse.kommune',
# 	# 		'Postadresse.kommunenummer',
# 	# 		'Næringskode 2.beskrivelse',
# 	# 		'Næringskode 2.',
# 	# 		'FrivilligRegistrertIMvaregisteret',
# 	# 		'Næringskode 3.beskrivelse',
# 	# 		'Næringskode 3.',
# 	# 				# ], axis = 0, inplace = True)
# 	# 				], axis = 1)
# 	# except:
# 	# 	print("none of the tries worked")
# 	try:
# 		df  = df.drop([
# 					'Næringskode 2',
# 					'Næringskode 2.beskrivelse',
# 					'Næringskode 3',
# 					'Næringskode 3.beskrivelse',
# 					'Postadresse.adresse',
# 					'Postadresse.poststed',
# 					'Postadresse.postnummer',
# 					'Postadresse.kommune',
# 					'Postadresse.kommunenummer',
# 					'Postadresse.land',
# 					'Postadresse.landkode',
# 					'FrivilligRegistrertIMvaregisteret',
# 					'Målform',
# 					'Hjelpeenhetskode',
# 					'Hjelpeenhetskode.beskrivelse',
# 					'Hjelpeenhetskode',
# 					'Hjelpeenhetskode.beskrivelse',
# 					], axis = 0)
# 	except:
# 		df  = df.drop([
# 			'Næringskode 2',
# 			'Næringskode 2.beskrivelse',
# 			'Næringskode 3',
# 			'Næringskode 3.beskrivelse',
# 			'Postadresse.adresse',
# 			'Postadresse.poststed',
# 			'Postadresse.postnummer',
# 			'Postadresse.kommune',
# 			'Postadresse.kommunenummer',
# 			'Postadresse.land',
# 			'Postadresse.landkode',
# 			'FrivilligRegistrertIMvaregisteret',
# 			'Målform',
# 			'Hjelpeenhetskode',
# 			'Hjelpeenhetskode.beskrivelse',
# 			'Hjelpeenhetskode',
# 			'Hjelpeenhetskode.beskrivelse',
# 			], axis = 1)
# 	# df = df.rename(index={	'organisasjonsnummer': 'org_num',
# 								# 'navn': 'navn',
# 								# 'registreringsdatoEnhetsregisteret': 'registreringsdato',
# 								# 'registrertIMvaregisteret': 'mva_registrert',
# 								# 'antallAnsatte': 'antall_ansatte',
# 								# 'registrertIForetaksregisteret': 'foretaks_registeret',
# 								# 'registrertIStiftelsesregisteret': 'stiftelses_registeret',
# 								# 'registrertIFrivillighetsregisteret': 'frivillighets_registeret',
# 								# 'konkurs': 'konkurs',
# 								# 'underAvvikling': 'under_avvikling',
# 								# 'underTvangsavviklingEllerTvangsopplosning': 'under_tvangsavvikling_eller_oppløsning',
# 								# 'organisasjonsform.kode': 'organisasjonsform_kode',
# 								# 'organisasjonsform.beskrivelse': 'organisasjonsform_beskrivelse',
# 								# 'naeringskode1.beskrivelse': 'naeringskode1_beskrivelse',
# 								# 'naeringskode1.kode': 'naeringskode1_kode',
# 								# 'forretningsadresse.land': 'land',
# 								# 'forretningsadresse.landkode': 'landkode',
# 								# 'forretningsadresse.postnummer': 'postnummer',
# 								# 'forretningsadresse.poststed': 'poststed',
# 								# 'forretningsadresse.adresse': 'adresse',
# 								# 'forretningsadresse.kommune': 'kommune',
# 								# 'forretningsadresse.kommunenummer': 'kommunenummer',
# 								# 'institusjonellSektorkode.kode': 'sektorkode_kode',
# 								# 'institusjonellSektorkode.beskrivelse': 'sektorkode_beskrivelse',
# 								# 'hjemmeside': 'hjemmeside',
# 								# 'stiftelsesdato': 'stiftelsesdato',
# 								# 'sisteInnsendteAarsregnskap': 'siste_innsendt_årsregnskap',
# 								# 'overordnetEnhet': 'overordnet_enhet',})#, inplace = True })
# 	df = df.T
# 	df = df.rename(columns = {	'Organisasjonsnummer': 'org_num',
# 								'Navn': 'navn',
# 								'Registreringsdato i Enhetsregisteret': 'registreringsdato',
# 								'Registrert i MVA-registeret': 'mva_registrert',
# 								'AntallAnsatte': 'antall_ansatte',
# 								'Registrert i Frivillighetsregisteret':  'frivillighets_registeret ',
# 								'Registrert i Foretaksregisteret':  'foretaks_registeret',
# 								'Registrert i Stiftelsesregisteret':  'stiftelses_registeret',
# 								'Konkurs': 'konkurs',
# 								'UnderAvvikling': 'under_avvikling',
# 								'UnderTvangsavviklingEllerTvangsopplosning': 'under_tvangsavvikling_eller_oppløsning',
# 								'Organisasjonsform.kode': 'organisasjonsform_kode',
# 								'Organisasjonsform.beskrivelse': 'organisasjonsform_beskrivelse',
# 								'Næringskode1.beskrivelse': 'næringskode1_beskrivelse',
# 								'Næringskode1.kode': 'næringskode1_kode',
# 								'Forretningsadresse.land': 'land',
# 								'Forretningsadresse.landkode': 'landkode',
# 								'Forretningsadresse.postnummer': 'postnummer',
# 								'Forretningsadresse.poststed': 'poststed',
# 								'Forretningsadresse.adresse': 'adresse',
# 								'Forretningsadresse.kommune': 'kommune',
# 								'Forretningsadresse.kommunenummer': 'kommunenummer',
# 								'Institusjonell sektorkode':  'sektorkode',
# 								'Institusjonell sektorkode.beskrivelse':  'sektorkode_beskrivelse',
# 								'Hjemmeside': 'hjemmeside',
# 								'Stiftelsesdato': 'stiftelsesdato',
# 								'SisteInnsendteAarsregnskap': 'siste_innsendt_årsregnskap',
# 								'OverordnetEnhet': 'overordnet_enhet',
# 								'Næringskode 1' : 'næringskode',
# 								'Næringskode 1.beskrivelse' : 'næringskode_beskrivelse',
# 								'Antall ansatte' : 'antall_ansatte',
# 								'Siste innsendte årsregnskap' : 'siste_innsendt_årsregnskap',
# 								'Under avvikling' : 'under_avvikling',
# 								'Under tvangsavvikling eller tvangsoppløsning' : 'under_tvangsavvikling_eller_oppløsning',
# 								'Overordnet enhet i offentlig sektor' : 'overordnet_enhet',})#, inplace = True })
		
# 	# 	df = df.rename(columns={
# 	# 'org_num': 
# 	# 'navn': 
# 	# 'organisasjonsform_kode': 
# 	# 'organisasjonsform_beskrivelse': 
# 	# 'Næringskode 1': 
# 	# 'Næringskode 1.beskrivelse': 
# 	# 'Antall ansatte': 
# 	# 'hjemmeside': 
# 	# 'adresse': 
# 	# 'poststed': 
# 	# 'postnummer': 
# 	# 'kommune': 
# 	# 'kommunenummer': 
# 	# 'land': 
# 	# 'landkode': 
# 	# 'Institusjonell sektorkode': 

# 	# 'Siste innsendte årsregnskap': 
# 	# 'Registreringsdato i Enhetsregisteret': 
# 	# 'stiftelsesdato': 

# 	# 'konkurs': 
# 	# 'Under avvikling': 
# 	# 'Under tvangsavvikling eller tvangsoppløsning': 
# 	# 'Overordnet enhet i offentlig sektor'


# 	# 'org_num', 'navn', 'organisasjonsform_kode',
# 	# 'organisasjonsform_beskrivelse', 'Næringskode 1',
# 	# 'Næringskode 1.beskrivelse', 'Antall ansatte', 'hjemmeside', 'adresse',
# 	# 'poststed', 'postnummer', 'kommune', 'kommunenummer', 'land',
# 	# 'landkode', 'sektorkode', 'sektorkode_beskrivelse',
# 	# 'Siste innsendte årsregnskap', 'registreringsdato', 'stiftelsesdato',
# 	# 'mva_registrert', 'frivillighets_registeret ', 'foretaks_registeret',
# 	# 'stiftelses_registeret', 'konkurs', 'Under avvikling',
# 	# 'Under tvangsavvikling eller tvangsoppløsning',
# 	# 'Overordnet enhet i offentlig sektor'



# 	# 		})

# 	# print(df.columns)
# 	# print(df.T)
# 	return df 

# # ''' ___ INSERT ___ --> IF DATA IS JSON (STRING) '''
# # # def insertData(conn, id, data_json, tablename):		# data as json (string)
# # # def insertData(conn, data_json, df, tablename):		# data as json (string)
# # def insertData(conn, dict_obj, tablename):
# # 	print()
# # 	print("_"*50)
# # 	print(f'inserting data_json to {tablename}:')
# # 	print('data inserted:')
# # 	pprint.pprint(dict_obj)
# # 	print("_"*50)
# # 	print()
# # 	print(" NOT FINISHED ")
# # 	curr = conn.cursor()
# # 	# PS NEEDS TO BE CHANGED!!! using a different datastructure from boilerplate
# # 	curr.execute(f'''
# # 		INSERT INTO
# # 			{tablename}(org_num,
# # 						navn,
# # 						organisasjonsform_kode,
# # 						organisasjonsform_beskrivelse,
# # 						næringskode1_beskrivelse,
# # 						næringskode1_kode,
# # 						antall_ansatte,
# # 						hjemmeside,
# # 						adresse,
# # 						poststed,
# # 						postnummer,
# # 						kommune,
# # 						kommunenummer,
# # 						land,
# # 						landkode,
# # 						sektorkode,
# # 						sektorkode_beskrivelse,
# # 						siste_innsendte_årsregnskap,
# # 						registreringsdato,
# # 						stiftelsesdato,
# # 						mva_registrert,
# # 						frivillighets_registeret,
# # 						foretaks_registeret,
# # 						stiftelses_registeret,
# # 						konkurs,
# # 						under_avvikling,
# # 						under_tvangsavvikling_eller_oppløsning,
# # 						overordnet_enhet_i_offentlig_sektor) 	
# # 			VALUES('{id}', %s)'''; [json.dumps(dict_obj)])


# # 	# curr.execute(f'''
# # 	# 	INSERT INTO
# # 	# 		{tablename}(org_num,
# # 	# 					navn,
# # 	# 					organisasjonsform_kode,
# # 	# 					organisasjonsform_beskrivelse,
# # 	# 					næringskode1_beskrivelse,
# # 	# 					næringskode1_kode,
# # 	# 					antall_ansatte,
# # 	# 					hjemmeside,
# # 	# 					adresse,
# # 	# 					poststed,
# # 	# 					postnummer,
# # 	# 					kommune,
# # 	# 					kommunenummer,
# # 	# 					land,
# # 	# 					landkode,
# # 	# 					sektorkode,
# # 	# 					sektorkode_beskrivelse,
# # 	# 					siste_innsendte_årsregnskap,
# # 	# 					registreringsdato,
# # 	# 					stiftelsesdato,
# # 	# 					mva_registrert,
# # 	# 					frivillighets_registeret,
# # 	# 					foretaks_registeret,
# # 	# 					stiftelses_registeret,
# # 	# 					konkurs,
# # 	# 					under_avvikling,
# # 	# 					under_tvangsavvikling_eller_oppløsning,
# # 	# 					overordnet_enhet_i_offentlig_sektor) 
# # 	# 	VALUES( %(org_num)s,
# # 	# 			%(navn)s,
# # 	# 			%(organisasjonsform_kode)s,
# # 	# 			%(organisasjonsform_beskrivelse)s,
# # 	# 			%(næringskode1_beskrivelse)s,
# # 	# 			%(næringskode1_kode)s,
# # 	# 			%(antall_ansatte)s,
# # 	# 			%(hjemmeside)s,
# # 	# 			%(adresse)s,
# # 	# 			%(poststed)s,
# # 	# 			%(postnummer)s,
# # 	# 			%(kommune)s,
# # 	# 			%(kommunenummer)s,
# # 	# 			%(land)s,
# # 	# 			%(landkode)s,
# # 	# 			%(sektorkode)s,
# # 	# 			%(sektorkode_beskrivelse)s,
# # 	# 			%(siste_innsendte_årsregnskap)s,
# # 	# 			%(registreringsdato)s,
# # 	# 			%(stiftelsesdato)s,
# # 	# 			%(mva_registrert)s,
# # 	# 			%(frivillighets_registeret)s,
# # 	# 			%(foretaks_registeret)s,
# # 	# 			%(stiftelses_registeret)s,
# # 	# 			%(konkurs)s,
# # 	# 			%(under_avvikling)s,
# # 	# 			%(under_tvangsavvikling_eller_oppløsning)s,
# # 	# 			%(overordnet_enhet_i_offentlig_sektor)s) ''', [json.dumps(dict_obj)])
# # 	# 	conn.commit()
# # 	# 	curr.close()



# # 	# curr = conn.cursor()
# # 	# # PS NEEDS TO BE CHANGED!!! using a different datastructure from boilerplate
# # 	# curr.execute(f'''
# # 	# 	INSERT INTO
# # 	# 		{tablename}(org_num,
# # 	# 					navn,
# # 	# 					registreringsdato,
# # 	# 					mva_registrert,
# # 	# 					antall_ansatte,
# # 	# 					foretaks_registeret,
# # 	# 					stiftelses_registeret,
# # 	# 					frivillighets_registeret,
# # 	# 					konkurs,
# # 	# 					under_avvikling,
# # 	# 					under_tvangsavvikling_eller_oppløsning,
# # 	# 					organisasjonsform_kode,
# # 	# 					organisasjonsform_beskrivelse,
# # 	# 					naeringskode1_beskrivelse,
# # 	# 					naeringskode1_kode,
# # 	# 					land,
# # 	# 					landkode,
# # 	# 					postnummer,
# # 	# 					poststed,
# # 	# 					adresse,
# # 	# 					kommune,
# # 	# 					kommunenummer,
# # 	# 					sektorkode_kode,
# # 	# 					sektorkode_beskrivelse,
# # 	# 					hjemmeside,
# # 	# 					stiftelsesdato,
# # 	# 					siste_innsendt_årsregnskap,
# # 	# 					overordnet_enhet) 
# # 	# 	VALUES('{id}', %s)''', [json.dumps(dict_obj)])
# # 	# curr.close()

# # 	''' ___ INSERT ___ ALTERNATIVE --> IF DATA IS DICTIONARY '''
# # 		# def insertData(conn, id, data_dict, tablename):		# data as dict
# # 		# 	print()
# # 		# 	print("_"*50)
# # 		# 	print(f'inserting data_dict to {tablename}:')
# # 		# 	print('data inserted:')
# # 		# 	print(data_dict)
# # 		# 	print("_"*50)
# # 		# 	print()
# # 		#	# PS NEEDS TO BE CHANGED!!! using a different datastructure from boilerplate
# # 		# 	curr.execute(f'''
# # 		# 		INSERT INTO
# # 		# 			{tablename}(id, json_col) 
# # 		# 		VALUES
# # 		# 			('{id}', %s)
# # 		# 	''', [Json(data_dict)])
# # 		# 	curr.close()


# # 	# def createNewTable(conn, tablename):
# # 	# 	curr = conn.cursor()
# # 	# 	create_table = """CREATE TABLE {} (	org_num VARCHAR PRIMARY KEY,
# # 	# 										navn VARCHAR,
# # 	# 										registreringsdato VARCHAR,
# # 	# 										mva_registrert VARCHAR,
# # 	# 										antall_ansatte VARCHAR,
# # 	# 										foretaks_registeret VARCHAR,
# # 	# 										stiftelses_registeret VARCHAR,
# # 	# 										frivillighets_registeret VARCHAR,
# # 	# 										konkurs VARCHAR,
# # 	# 										under_avvikling VARCHAR,
# # 	# 										under_tvangsavvikling_eller_oppløsning VARCHAR,
# # 	# 										organisasjonsform_kode VARCHAR,
# # 	# 										organisasjonsform_beskrivelse VARCHAR,
# # 	# 										naeringskode1_beskrivelse VARCHAR,
# # 	# 										naeringskode1_kode VARCHAR,
# # 	# 										land VARCHAR,
# # 	# 										landkode VARCHAR,
# # 	# 										postnummer VARCHAR,
# # 	# 										poststed VARCHAR,
# # 	# 										adresse VARCHAR,
# # 	# 										kommune VARCHAR,
# # 	# 										kommunenummer VARCHAR,
# # 	# 										sektorkode_kode VARCHAR,
# # 	# 										sektorkode_beskrivelse VARCHAR,
# # 	# 										hjemmeside VARCHAR,
# # 	# 										stiftelsesdato VARCHAR,
# # 	# 										siste_innsendt_årsregnskap VARCHAR,
# # 	# 										overordnet_enhet VARCHAR)
# # 	# 									   ;""".format(tablename)
# # 	# 	curr.execute(create_table)
# # 	# 	conn.commit()
# # 	# 	curr.close()


# # 	# def createNewTable(conn, dict_obj, tablename):
# # 	# 	curr = conn.cursor()
# # 	# 	create_table = """CREATE TABLE {} (	org_num VARCHAR PRIMARY KEY,
# # 	# 										navn VARCHAR,
# # 	# 										registreringsdato VARCHAR,
# # 	# 										mva_registrert VARCHAR,
# # 	# 										antall_ansatte VARCHAR,
# # 	# 										foretaks_registeret VARCHAR,
# # 	# 										stiftelses_registeret VARCHAR,
# # 	# 										frivillighets_registeret VARCHAR,
# # 	# 										konkurs VARCHAR,
# # 	# 										under_avvikling VARCHAR,
# # 	# 										under_tvangsavvikling_eller_oppløsning VARCHAR,
# # 	# 										organisasjonsform_kode VARCHAR,
# # 	# 										organisasjonsform_beskrivelse VARCHAR,
# # 	# 										naeringskode1_beskrivelse VARCHAR,
# # 	# 										naeringskode1_kode VARCHAR,
# # 	# 										land VARCHAR,
# # 	# 										landkode VARCHAR,
# # 	# 										postnummer VARCHAR,
# # 	# 										poststed VARCHAR,
# # 	# 										adresse VARCHAR,
# # 	# 										kommune VARCHAR,
# # 	# 										kommunenummer VARCHAR,
# # 	# 										sektorkode_kode VARCHAR,
# # 	# 										sektorkode_beskrivelse VARCHAR,
# # 	# 										hjemmeside VARCHAR,
# # 	# 										stiftelsesdato VARCHAR,
# # 	# 										siste_innsendt_årsregnskap VARCHAR,
# # 	# 										overordnet_enhet VARCHAR)
# # 	# 									   ;""".format(tablename)
# # 	# 	curr.execute(create_table)
# # 	# 	conn.commit()
# # 	# 	curr.close()
# # 	# 	insertData(conn, dict_obj, tablename)

# # def createNewTable(conn, dict_obj, tablename):
# # 	curr = conn.cursor()
# # 	create_table = """CREATE TABLE {} (	org_num VARCHAR PRIMARY KEY,
# # 										navn VARCHAR,
# # 										organisasjonsform_kode VARCHAR,
# # 										organisasjonsform_beskrivelse VARCHAR,
# # 										næringskode1_beskrivelse VARCHAR,
# # 										næringskode1_kode VARCHAR,
# # 										antall_ansatte VARCHAR,
# # 										hjemmeside VARCHAR,
# # 										adresse VARCHAR,
# # 										poststed VARCHAR,
# # 										postnummer VARCHAR,
# # 										kommune VARCHAR,
# # 										kommunenummer VARCHAR,
# # 										land VARCHAR,
# # 										landkode VARCHAR,
# # 										sektorkode VARCHAR,
# # 										sektorkode_beskrivelse VARCHAR,
# # 										siste_innsendte_årsregnskap VARCHAR,
# # 										registreringsdato VARCHAR,
# # 										stiftelsesdato VARCHAR,
# # 										mva_registrert VARCHAR,
# # 										frivillighets_registeret VARCHAR,
# # 										foretaks_registeret VARCHAR,
# # 										stiftelses_registeret VARCHAR,
# # 										konkurs VARCHAR,
# # 										under_avvikling VARCHAR,
# # 										under_tvangsavvikling_eller_oppløsning VARCHAR,
# # 										overordnet_enhet_i_offentlig_sektor VARCHAR)
# # 									   ;""".format(tablename)
# # 	curr.execute(create_table)
# # 	conn.commit()
# # 	curr.close()
# # 	insertData(conn, dict_obj, tablename)

# # # def createNewTable(conn, tablename):
# # 	# curr = conn.cursor()
# # 	# create_table = """CREATE TABLE {} (id VARCHAR PRIMARY KEY, 
# # 	# 								   json_col VARCHAR)
# # 	# 								   ;""".format(tablename)
# # 	# curr.execute(create_table)
# # 	# conn.commit()

# # def checkForTable(conn, tablename):
# # 	table_exists = False
# # 	print(f"checking if {tablename} exists: ")
# # 	try:
# # 		curr = conn.cursor()
# # 		curr.execute("select * from information_schema.tables where table_name=%s", (tablename,))				 	# check table
# # 		# curr.execute("select exists(select * from information_schema.tables where table_name=%s)", (tablename,))	# check table alt
# # 		# curr.execute("select exists(select relname from pg_class where relname='" + table_str + "')")			 	# check table alt
# # 		exists = curr.fetchone()[0]
# # 		table_exists = True
# # 		print(f"    table; {tablename} was found, proceeding to concatenate new data..")
# # 		print(f"    please wait..")
# # 		curr.close()
# # 	# except psycopg2.Error as e:
# # 	except TypeError as e:
# # 		print(f"    Error: table {tablename} does not exsist, proceeding to create a new table..")
# # 		print(f"    please wait..")
# # 	print(f"table_exists = {table_exists}")
# # 	return table_exists

# # def tableManager(conn, table_exists, tablename, dict_obj):
# # 	''' IF statement - makes decition based on table_exists from checkForTable():
# # 			a. runs addToDatabase(), if table_exists == True
# # 			b. runs createNewTable(), if table_exists == False
# # 	'''
# # 	if table_exists == True:
# # 		insertData(conn, dict_obj, tablename)
# # 	elif table_exists == False:
# # 		createNewTable(conn, dict_obj, tablename)
# # 	else:
# # 		print(f'    Unknown Error in tableManager(): table_exists was neither True or False, or data_json might be corrupt.')
# # 		print(f'    				Check for errors in "checkForTable()".')

# if __name__ == '__main__':

# 	''' get connectrion '''
# 	# dbname, host, user, password, tablename =  parseConfig()
# 	# conn = getConnection()
	
# 	''' get data '''
# 	data_snippet = getDataSnippet()             #data-type: JSON (string)
# 	# # data_dict = convertToDict(data_snippet)     #converts JSON -> dict
# 	# # data_json = convertToJson(data_snippet)     #converts dict -> JSON
	

# 	# ''' manage database '''
# 	# table_exists = checkForTable(conn, tablename)
# 	df = dataframeConverter(data_snippet)
# 	print(df)
# 	# df = datasetEditor(df)
# 	# dict_obj = df.to_dict()
# 	# tableManager(conn, table_exists, tablename, dict_obj)
	

	
	
# 	# ''' close connection '''
# 	# conn.close()


	




# # def createNewTable(conn, tablename, data_json):
# # 	# print(f"creating new table: {tablename}:")
# # 	curr = conn.cursor()
# # 	try:
# # 		curr.execute(f"CREATE TABLE {tablename} (id serial PRIMARY KEY, num integer, data varchar);")
# # 	except:
# # 		print("	Error: unable to create new table.")
# # 	conn.commit() # <--- makes sure the change is shown in the database
# # 	curr.close()
# # 	# conn.close() #original
# # 	# curr.close() #original


# # ############# CREATE TABLE FROM DATAFRAME TEST #############
# # from sqlalchemy import create_engine

# # def makeCreateEngine():
# # 	# NB: MISSING PORT !!!!
# # 	port = ""
# # 	return create_engine(f'postgresql://{user}:{password}@{host}:{port}/{dbname}')

# # def createNewTable(engine, tablename, data_json):
# # 	df.to_sql(f'{tablename}', engine)

# # ############# CREATE TABLE FROM DATAFRAME TEST #############



# # 	engine = create_engine('postgresql+psycopg2://username:password@host:port/database')

# # 	df.to_sql(f'{tablename}', engine, index = False)
# # 	# df.to_sql(f'{tablename}', engine, if_exists = 'replace', index = False) #drops old table and creates new empty table
# # 	conn = engine.raw_connection()
# # 	cur = conn.cursor()
# # 	output = io.StringIO()
# # 	df.to_csv(output, sep='\t', header=False, index=False)
# # 	output.seek(0)
# # 	contents = output.getvalue()
# # 	cur.copy_from(output, 'table_name', null="") # null values become ''
# # 	conn.commit()





# # org_num VARCHAR,

# # org_num VARCHAR PRIMARY KEY,
# # navn VARCHAR,
# # registreringsdato VARCHAR,
# # mva_registrert VARCHAR,
# # antall_ansatte VARCHAR,
# # foretaks_registeret VARCHAR,
# # stiftelses_registeret VARCHAR,
# # frivillighets_registeret VARCHAR,
# # konkurs VARCHAR,
# # under_avvikling VARCHAR,
# # under_tvangsavvikling_eller_oppløsning VARCHAR,
# # organisasjonsform_kode VARCHAR,
# # organisasjonsform_beskrivelse VARCHAR,
# # naeringskode1_beskrivelse VARCHAR,
# # naeringskode1_kode VARCHAR,
# # land VARCHAR,
# # landkode VARCHAR,
# # postnummer VARCHAR,
# # poststed VARCHAR,
# # adresse VARCHAR,
# # kommune VARCHAR,
# # kommunenummer VARCHAR,
# # sektorkode_kode VARCHAR,
# # sektorkode_beskrivelse VARCHAR,
# # hjemmeside VARCHAR,
# # stiftelsesdato VARCHAR,
# # siste_innsendt_årsregnskap VARCHAR,
# # overordnet_enhet VARCHAR,




# # org_num
# # navn
# # registreringsdato
# # mva_registrert
# # antall_ansatte
# # foretaks_registeret
# # stiftelses_registeret
# # frivillighets_registeret
# # konkurs
# # under_avvikling
# # under_tvangsavvikling_eller_oppløsning
# # organisasjonsform_kode
# # organisasjonsform_beskrivelse
# # naeringskode1_beskrivelse
# # naeringskode1_kode
# # land
# # landkode
# # postnummer
# # poststed
# # adresse
# # kommune
# # kommunenummer
# # sektorkode_kode
# # sektorkode_beskrivelse
# # hjemmeside
# # stiftelsesdato
# # siste_innsendt_årsregnskap
# # overordnet_enhet