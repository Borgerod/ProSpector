# for postgres
import json
import psycopg2

# for json from path 
import json
import gzip
import pandas as pd 
import pprint


''' __________________________ POSTGRES PAYLOAD __________________________ '''

# Payload:
payload = {	'dbname'   : 'Telegram_data',
			'host' 	   : 'localhost',
			'user'	   : 'postgres',
        	'password' : 'Orikkel1991',
        	'tablename': 'daily_monitor',  }



''' ___ POSTGRES BOILERPLATE ____________________________________________________ '''

import psycopg2
from psycopg2.extras import Json

# ___ local imports ________
# from Config import payload  #Saving for later
# print(payload)


''' ___ PREP _______________________________________________ '''
def parseConfig():
	dbname = payload['dbname']
	host = payload['host']
	user = payload['user']
	password = payload['password']
	tablename = payload['tablename']
	return dbname, host, user, password, tablename



def getCursor(conn):
	return conn.cursor() # returns cursor

def getConnection():
	return psycopg2.connect(
		dbname = dbname, 
		host = host, 
		user = user, 
		password = password)

def createTable(conn, tablename):
	curr = conn.cursor()
	create_table = """CREATE TABLE {} (id VARCHAR PRIMARY KEY, 
									   json_col VARCHAR,)
									   ;""".format(tablename)
	curr.execute(create_table)
	conn.commit()

def tryCreateTable(conn):
	try:
		createTable(conn)
	except (Exception, psycopg2.DataError) as error:
		print(error)
		conn = getConnection()

''' ___ POSTGRESS DATA MANAGEMENT __________________________ '''

''' ___ INSERT ___ '''
def insertData(curr, id, dict_obj, tablename):
	# '''optional printing'''
		# print()
		# print("_"*50)
		# print('Dictionary being inserted to database:')
		# print(dict_obj)
		# print("_"*50)
		# print()
	curr.execute(f'''
		INSERT INTO
			{tablename}(id, json_col) 
		VALUES
			('{id}', %s)
	''', [Json(dict_obj)])


''' ___ FETCH ___ '''
def fetchData(curr):  
	# yesterday_ids = ['ethclassic','FTX_Official']
	# yesterday_ids = (str(yesterday_ids)[1:-1])
	curr.execute("SELECT * FROM daily_monitor;") 
	conn.close()


''' ___ TEMPORARY: IMPORT DATA FROM FILE ___ '''
def getDataFromFile():





''' ___ DATAFRAME CONVERTER _______________________________ '''
def dataframeConverter(db_data):
	return pd.read_json(db_data)


def datasetEditor(df):
	df = df.drop([
		'maalform', 
		'links', 
		'postadresse.land', 
		'postadresse.landkode',
		'postadresse.postnummer',
		'postadresse.poststed',
		'postadresse.adresse',
		'postadresse.kommune',
		'postadresse.kommunenummer',
		'naeringskode2.beskrivelse',
		'naeringskode2.kode',
		'naeringskode2.hjelpeenhetskode',
		'frivilligMvaRegistrertBeskrivelser',
		'naeringskode1.hjelpeenhetskode',
		'naeringskode3.beskrivelse',
		'naeringskode3.kode',
		'naeringskode3.hjelpeenhetskode', 
		'organisasjonsform.links',      
				], axis = 1, inplace = True)
	
	df = df.rename(columns = {	'organisasjonsnummer': 'org_num',
								'navn': 'navn',
								'registreringsdatoEnhetsregisteret': 'registreringsdato',
								'registrertIMvaregisteret': 'mva_registrert',
								'antallAnsatte': 'antall_ansatte',
								'registrertIForetaksregisteret': 'foretaks_registeret',
								'registrertIStiftelsesregisteret': 'stiftelses_registeret',
								'registrertIFrivillighetsregisteret': 'frivillighets_registeret',
								'konkurs': 'konkurs',
								'underAvvikling': 'under_avvikling',
								'underTvangsavviklingEllerTvangsopplosning': 'under_tvangsavvikling_eller_oppløsning',
								'organisasjonsform.kode': 'organisasjonsform_kode',
								'organisasjonsform.beskrivelse': 'organisasjonsform_beskrivelse',
								'naeringskode1.beskrivelse': 'naeringskode1_beskrivelse',
								'naeringskode1.kode': 'naeringskode1_kode',
								'forretningsadresse.land': 'land',
								'forretningsadresse.landkode': 'landkode',
								'forretningsadresse.postnummer': 'postnummer',
								'forretningsadresse.poststed': 'poststed',
								'forretningsadresse.adresse': 'adresse',
								'forretningsadresse.kommune': 'kommune',
								'forretningsadresse.kommunenummer': 'kommunenummer',
								'institusjonellSektorkode.kode': 'sektorkode_kode',
								'institusjonellSektorkode.beskrivelse': 'sektorkode_beskrivelse',
								'hjemmeside': 'hjemmeside',
								'stiftelsesdato': 'stiftelsesdato',
								'sisteInnsendteAarsregnskap': 'siste_innsendt_årsregnskap',
								'overordnetEnhet': 'overordnet_enhet',})#, inplace = True })
	return df 

if __name__ == '__main__':
	dbname, host, user, password, tablename = parseConfig()
	conn = getConnection()
	curr = getCursor(conn)
	data = getDataset()
	df = dataframeConverter(data)
	df = datasetEditor(df)
	print(df)




# 'organisasjonsform.links': 'naeringskode1_beskrivelse',

# 'organisasjonsnummer'
# 'navn'
# 'registreringsdatoEnhetsregisteret'
# 'registrertIMvaregisteret'
# 'antallAnsatte'
# 'registrertIForetaksregisteret'
# 'registrertIStiftelsesregisteret'
# 'registrertIFrivillighetsregisteret'
# 'konkurs'
# 'underAvvikling'
# 'underTvangsavviklingEllerTvangsopplosning'
# 'organisasjonsform.kode'
# 'organisasjonsform.beskrivelse'
# 'organisasjonsform.links'
# 'naeringskode1.beskrivelse'
# 'naeringskode1.kode'
# 'forretningsadresse.land'
# 'forretningsadresse.landkode'
# 'forretningsadresse.postnummer'
# 'forretningsadresse.poststed'
# 'forretningsadresse.adresse'
# 'forretningsadresse.kommune'
# 'forretningsadresse.kommunenummer'
# 'institusjonellSektorkode.kode'
# 'institusjonellSektorkode.beskrivelse'
# 'hjemmeside'
# 'stiftelsesdato'
# 'sisteInnsendteAarsregnskap'
# 'overordnetEnhet'




# ''' ___ MAIN _____________________________________________ '''
# if __name__ == '__main__':
#     dbname, host, user, password, tablename =  parse_config()
#     # purge()
#     # insert()
#     # fetch()




















# ''' __________________________ ORIGINAL KODE __________________________ '''

# # pd.set_option('display.max_row', None)          # Rows     (length)
# pd.set_option('display.max_columns', None)      # Columns  (width)
# pd.set_option('display.max_colwidth', 40)       # Columns  (column display border)
# pd.set_option('display.width', 2000)            # Whole    (dataframe display border)


# def getDataset():
# 	with gzip.open('enheter_alle.json.gz', 'r') as fin:         # 4. gzip
# 		json_bytes = fin.read()                                 # 3. bytes (i.e. UTF-8)
# 	json_str = json_bytes.decode('utf-8')                       # 2. string (i.e. JSON)
# 	data = json.loads(json_str)                                 # 1. data
# 	return data


# def makeDataframe(dataset):
# 	return pd.json_normalize(dataset)



# def saveToPostgress(data):
# with psycopg2.connect('') as conn:
# 	with conn.cursor() as cur:
# 		data = get_dataset()
# 		cur.execute(""" create table if not exists json_table(
# 			p_id integer, first_name text, last_name text, p_attribute jsonb,
# 			quote_content text) """)
# 		query_sql = """ insert into json_table
# 			select * from json_populate_recordset(NULL::json_table, %s) """
# 		cur.execute(query_sql, (json.dumps(data),))


# if __name__ == '__main__':
# 	data = getDataset()
# 	print(type(data))

# 	# data = get_dataset()
# 	# # print(data.keys())
# 	# df = make_dataframe(data)
# 	# print(df.iloc[0])
# 	# print()
# 	# print()
# 	# print(df.iloc[0].T)

# 	# dfHead = df.iloc[:1] 

