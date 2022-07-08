# '''
# Config
# Postgres & Scraper Configuration file, containing: 

# 	____ Postgres ____
# 	- payload 

# 	____ Scraper ____ 	
# 	- cred 

# 	____ Common ____ 	
# 	- proxies


# information:
# 	"payload" = Postgres connection credentials (password, user, host, dbname)
	
# 	"cred"	  = Login credentials for the telegram scraper, 
# 				(it logs into a telegram account and uses it to accsess the data).

# 	"proxies" = There are three different proxies, 
# 				"proxies" is the common proxy and is the default,
# 				use "p_proxies" and "s_proxies" if you wish to use different proxies.
# 				Warning: switching proxies will require some edits of the code. 
# '''

# __________________________ (CRED) API KEYS __________________________


# Cred 
cred =  { 'google': {  'API_KEY': 'AIzaSyC3N7q2PIVMA3OdBDfkxqxjQFY1VVIXNUE',
		               'API_ID': 'xxxxx',
		               'App_name': 'Mediavest_Places',
		               'IP_restriction': '192.168.68.76',  },}


# # __________________________ POSTGRES __________________________

# # Payload:
# payload = {	'dbname'   : 'Telegram_data',
# 			'host' 	   : 'localhost',
# 			'user'	   : 'postgres',
#         	'password' : 'xxxxxxx',
#         	'tablename': 'daily_monitor',  }


# # __________________________ COMMON __________________________

# # Proxies
# proxies = { 'http'  : 'http://10.10.1.10:3128', 
#             'https' : 'https://10.10.1.11:1080', 
#             'ftp'   : 'ftp://10.10.1.10:3128',   }

