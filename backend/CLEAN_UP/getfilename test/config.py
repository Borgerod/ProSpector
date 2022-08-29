# '''
# Config
# Postgres & Scraper Configuration file, containing: 

# 	____ Postgres ____
# 	- payload 

# 	____ Scraper ____ 	
# 	- cred 

# 	____ Common ____ 	
# 	- proxies


# # __________________________ (CRED) API KEYS __________________________


# # Cred 
# cred =  { 'google': {  'API_KEY': 'AIzaSyC3N7q2PIVMA3OdBDfkxqxjQFY1VVIXNUE',
# 		               'API_ID': 'xxxxx',
# 		               'App_name': 'Mediavest_Places',
# 		               'IP_restriction': '192.168.68.76',  },}


## __________________________ POSTGRES __________________________

payload = { 	'dbname'   : 'media_vest',
				'host'     : 'localhost',
				'user'     : 'postgres',
				'password' : 'Orikkel1991',  }

# brreg_payload = { 	'dbname'   : 'media_vest',
# 					'host'     : 'localhost',
# 					'user'     : 'postgres',
# 					'password' : 'Orikkel1991',
# 					'tablename': 'brreg_table',  }

# google_payload = {  'dbname'   : 'media_vest',
# 					'host'     : 'localhost',
# 					'user'     : 'postgres',
# 					'password' : 'Orikkel1991',
# 					'tablename': 'google_table',  }

## TABLENAMES ALT 1:
tablenames = {	'google' 	  : 'google_table',
				'brreg' 	  : 'brreg_table',
				'gulesider'   : 'gulesider_table',
				'correct_file_name' : 'input_table',
				'input_table' : 'input_table',  }


## __________________________ EXTRACTORS SETTINGS __________________________
settings =  {	'google_settings'	 : {'chunk_size' : 5,},
				'brreg_settings' 	 : {	 			 },
				'gulesider_settings' : {	 			 },  }




# ## TABLENAMES ALT 2:			
# ## __________________________ GOOGLE SETTINGS __________________________
# # CHUNK_SIZE = 5
# # google_table = 'google_table'

# # google_settings =	 {	'tablename'  : 'google_table',
# # 					 	'chunk_size' : 5, 				 }
# google_settings = 	 {	'chunk_size' : 5, 				 }

# ## __________________________ BRREG SETTINGS __________________________
# # brreg_table = 'brreg_table'

# # brreg_settings = 	 {	'tablename'  : 'brreg_table',  	  }
# brreg_settings =	 {	 				  }
# ## __________________________ GULESIDER SETTINGS __________________________
# # gulesider_table = 'gulesider_table'

# # gulesider_settings = {	'tablename'  : 'gulesider_table', }
# gulesider_settings = {	 				  }






