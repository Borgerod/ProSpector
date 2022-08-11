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
from postgres import databaseManager, cleanUp
from file_manager import *

'''
* CURRENT EXTRACTION TIME *
		- Amount of companies : 6034  
		- Finished in 11.2 second(s)
'''

'''
FIXME : ISSUES:
	- KeyError: 'page' was raised in getpage() at page 500/1001
	-
'''

'''
TODO :
	- [X] check if '' first run '' is necessary
	-	  update: possibly needed because tqdm needs a total
	-	  but the rest of it might not be needed 
	- [ ] make documentation on "RUNDOWN OF THE PROGRAM", including what postgres.py does
	- [ ] make documentation on "NOTABLE FLAWS"
	- [X] implement loop for getRequests()
	- [X] create multithreaded loop
	- [ ] finish Config
	- [X] implement progressbar
	- [ ] look into and fix freezing issue from "NOTABLE FLAWS"
'''

'''
* RUNDOWN OF THE PROGRAM:
	[...]
	[...]
'''

'''
! NOTABLE FLAWS: 
	- seems to freeze when extracting all_pages 
	-
'''


# NEW GETREQUEST()
def getRequest(next_page):
	''' simple get request based on next_page -> json_dict '''
	url = f'https://data.brreg.no/enhetsregisteret/api/enheter/?page={next_page}&size=20' #-i -X GET
	r = requests.get(url, timeout = 10)
	json = r.json()
	return json

#FIXME [OLD] getpage
	# def getpage(json):
	# 	''' get the page element from json '''
	# 	page =  json['page']
	# 	return page

#FIXME [TEST] getpage
def getpage(json, current_page):
	''' get the page element from json_dict '''
	try: 
		page =  json['page']
	except KeyError as e:
		print("_"*100)
		print(f"KeyError: json['page'] returned {e}")
		print(f'the error was raised on page: {current_page}')
		print()
		print(json)
		print("_"*100)
		pass
	return page

def getMaxpages(page):
	''' 
		gets the total number of pages from JSON, 
		used for breaking the loop 
	'''
	total_pages = page['totalPages']
	return total_pages

def gettotalElements(page):
	''' 
		Not used in code.
		gets the total number of elements (Companies) from JSON, 
		used for supervising & calculations
	'''
	total_elements = page['totalElements']
	return total_elements

def getCurrentpage(page):
	''' gets the current page from JSON '''
	current_page = page['number']
	return current_page

def getnext_page(current_page):
	''' makes next_page from current_page '''
	next_page = current_page + 1
	return next_page

def getData(json):
	''' gets data from JSON '''
	data = json['_embedded']['enheter']
	return data	

def makeDataframe(data):
	''' makes dataframe from json '''
	df = pd.json_normalize(data)
	return df

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

def apiManager(current_page):
	'''
		Manages the api from "Brønnøysynd registeret"
	'''
	tablename = parseTablenames(getFileName())
	json = getRequest(current_page)
	'''pages'''
	# page = getpage(json)
	page = getpage(json, current_page) #FIXME --> TEMP while testing
	total_pages = getMaxpages(page)
	current_page = getCurrentpage(page)	
	next_page = getnext_page(current_page)

	'''data'''
	data = getData(json)
	df = makeDataframe(data)
	df = datasetEditor(df)
	next_result = 0
	#FIXME --> TEMP while testing
	# print(current_page) 
	# print(df)
	# databaseManager(df, tablename)

	while next_result == 0:
		try:
			databaseManager(df, tablename)
			#FIXME --> TEMP while testing
			# print(df)
			next_result = 1
		except:
			continue
		break
	#FIXME --> TEMP while testing
	# print(df)

	return df, total_pages, current_page, next_page



def brregExtractor(testmode):
	print("_"*91)
	print("|											  |")
	print("|			Starting: Brønnøysund Register Extractor 			  |")
	print("|											  |")
	print("_"*91)
	print()

	''' preperations: parse config, connect to database and connect to api manager '''

	''' fetching data from config '''
	file_name = getFileName()	# fetches name of current file 
	tablename = parseTablenames(file_name) # fetches the appropriate tablename for current file
	settings = parseSettings(file_name)	# fetches the appropriate settings for current file

	
	''' first run '''
	first_page = 0
	df, total_pages, current_page, next_page = apiManager(first_page)
	databaseManager(df, tablename)

	''' temporary code for testing '''
	if testmode == "on":
		total_pages = 1

	''' makes list of all page numbers '''
	all_pages = np.arange(next_page-1, total_pages)

	''' Loop, rest of the pages '''
	with tqdm(total = total_pages) as pbar:
		with concurrent.futures.ThreadPoolExecutor() as executor:
			results = executor.map(apiManager, all_pages)
			for result in results:
				databaseManager(result[0], tablename)
				pbar.update(1)


	print("																		"+"_"*91)
	print("																		|											  |")
	print("																		|				   Data Extraction Complete. 				  |")
	print("																		|											  |")
	print("																		"+"_"*91)
	print()
	print(f"|				   Finished in< {round(time.perf_counter() - start, 2)} second(s)				  |")


if __name__ == '__main__':
	print("_"*91)
	# print("|											  |")
	print("|			Starting: Brønnøysund Register Extractor 			  |")
	# print("|											  |")
	print("_"*91)
	print()

	''' preperations: parse config, connect to database and connect to api manager '''

	''' fetching data from config '''
	file_name = getFileName()	# fetches name of current file 
	tablename = parseTablenames(file_name) # fetches the appropriate tablename for current file
	settings = parseSettings(file_name)	# fetches the appropriate settings for current file
	
	# FIXME [OLD] '' first run ''
		# ''' first run '''
		# first_page = 0
		# df, total_pages, current_page, next_page = apiManager(current_page = 0)
		# databaseManager(df, tablename)

	# FIXME: [OLD] all_pages
		# ''' makes list of all page numbers '''
		# all_pages = np.arange(next_page, total_pages+1)
		# # print(all_pages)
		# # print(next_page)
		# # print(next_page-1)
		# # print(len(all_pages))

	# * [new] '' first run '' & '' makes list of all page numbers '' ALL-IN-ONE
	''' makes list of all page numbers '''
	df, total_pages, current_page, next_page = apiManager(current_page = 0)
	total_pages = 550	#FIXME --> TEMP while testing
	

	# ! [OLD] all_papges
		# 
		# all_pages = np.arange(0, total_pages + 1)
	
	# * [NEW] all_papges
	# all_pages = np.arange(0, total_pages)
	all_pages = np.arange(450, total_pages) #FIXME --> TEMP while testing
	
	# FIXME: TEMP PRINTING while testing
		# first_page = 0 
		# print(f''' all_pages: \n {all_pages}
		# 		\n first_page: {first_page}
		# 		\n first_page-1: {first_page - 1}
		# 		\n first_page+1: {first_page + 1}
		# 		\n all_pagers length: {len(all_pages)}''')

	''' Loop, rest of the pages '''
	with concurrent.futures.ThreadPoolExecutor() as executor:
		list(tqdm(executor.map(apiManager, all_pages), total = all_pages[-1] ))#len(all_pages)))
	cleanUp(tablename)
	# * [NEW] FINISHED PRINT
	print("_"*91)
	print("|			Starting: Brønnøysund Register Extractor 			  |")
	print(f"|				   Finished in {round(time.perf_counter() - start, 2)} second(s)				  |")
	print("_"*91)
	print()

	# FIXME [OLD] FINISHED Print]
		# print("																		"+"_"*91)
		# print("																		|											  |")
		# print("																		|				   Data Extraction Complete. 				  |")
		# print("																		|											  |")
		# print("																		"+"_"*91)
		# print()
		# print(f"|				   Finished in {round(time.perf_counter() - start, 2)} second(s)				  |")



'''
* [TEST] all_pages, CONCLUTION: 
	WITH LIMIT (300): 
	 all_pages:
	 [  0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17
	  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35
	  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53
	  54  55  56  57  58  59  60  61  62  63  64  65  66  67  68  69  70  71
	  72  73  74  75  76  77  78  79  80  81  82  83  84  85  86  87  88  89
	  90  91  92  93  94  95  96  97  98  99 100 101 102 103 104 105 106 107
	 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125
	 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143
	 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161
	 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179
	 180 181 182 183 184 185 186 187 188 189 190 191 192 193 194 195 196 197
	 198 199 200 201 202 203 204 205 206 207 208 209 210 211 212 213 214 215
	 216 217 218 219 220 221 222 223 224 225 226 227 228 229 230 231 232 233
	 234 235 236 237 238 239 240 241 242 243 244 245 246 247 248 249 250 251
	 252 253 254 255 256 257 258 259 260 261 262 263 264 265 266 267 268 269
	 270 271 272 273 274 275 276 277 278 279 280 281 282 283 284 285 286 287
	 288 289 290 291 292 293 294 295 296 297 298 299 300]

	 first_page: 0

	 first_page-1: -1

	 first_page+1: 1

	 all_pagers length: 301

	WITHOUT LIMIT:
		 all_pages:
		 [    0     1     2 ... 53906 53907 53908]

		 first_page: 0

		 first_page-1: -1

		 first_page+1: 1

		 all_pagers length: 53909
'''


'''
* [TEST] scrape 1000 pages, CONCLUTION:


* TEST OUTPUT: 
___________________________________________________________________________________________
|                       Starting: Brønnøysund Register Extractor                          |
___________________________________________________________________________________________

 98%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▏   | 490/501 [00:14<00:00, 37.25it/s]____________________________________________________________________________________________________
'page'

{'tidsstempel': 1660146687576, 'status': 400, 'feilmelding': 'Feilaktig forespørsel', 'sti': '/enhetsregisteret/api/enheter/', 'antallFeil': 1, 
'valideringsfeil': [{'feilmelding': 'size * (page+1) kan ikke overstige 10_000', 'parametere': ['size', 'page']}]}

'''