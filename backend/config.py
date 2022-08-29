'''
Config
Postgres & Scraper Configuration file, containing: 

	____ POSTGRES ____
	- payload 
	- tablenames

	____ Extractors ____ 	
	- settings 

	____ Common ____ 	
	- proxies
'''

# # _____ API KEYS ________________________CURRENTLY NOT IN USE____________________________________
# # cred =  { 'google': {  'API_KEY': 'AIzaSyC3N7q2PIVMA3OdBDfkxqxjQFY1VVIXNUE',
# # 		               'API_ID': 'xxxxx',
# # 		               'App_name': 'Mediavest_Places',
# # 		               'IP_restriction': '192.168.68.76',  },}

''' _____ POSTGRES ____________________________________________________________ '''
payload = { 	'test_dbname': 'Mediavest_test_env',
				#'dbname'   : 'Mediavest',	#[new] dbname [inactive]
				'dbname'   : 'media_vest',  #! soon to be depricated
				'host'     : 'localhost',
				'user'     : 'postgres',
				'password' : 'Orikkel1991',  }

tablenames = {	'google' 	   			: 'google_output_table',
				'brreg' 	   			: 'brreg_table',
				'gulesider'    			: 'gulesider_table',
				# 'input_table'  			: 'input_table',
				# 'output_table' 			: 'output_table',
				'input'  				: 'input_table',
				'output' 				: 'output_table',
				'I88I' 					: '1881_table',
				'proff' 				: 'proff_table',
				'google_input' 			: 'google_input_table',
				'gulesider_error_table' : 'gulesider_error_table',
				'update_tracker' 		: 'update_tracker',		  
				'call_list' 			: 'call_list',
				'I88I_output_table'		: 'I88I_output_table',
				'gulesider_output_table' : 'gulesider_output_table',	}


'''
	dict of all the extractor filenames (.py files), listed in chronological order.  
'''
extractor_filenames = {	'input' 					: ['brreg', 'input_table',],
						'first_output' 				: ['1881', 'gulesider', 'proff', 'output_table'],
						'second_output'    			: 'google',
						'final' 		   			: 'call_list',										}

extractor_filenames = {	'first' 					: 'brreg',
						'second' 					: ['1881', 'gulesider', 'proff'],
						'third'						: 'google',											}

table_managers = {	'first' 					: 'brreg',
					'input'    					: 'input_table',
					'second' 					: ['1881', 'gulesider', 'proff'],
					'first_output'				: 'output_table',
					'third'						: 'google',
					'final_output'    			: 'call_list',
					'second_output'    			: 'call_list',
					'final' 		   			: 'call_list',											}

# test_tablenames = {
# 	'general':'test_table',
# 	'brreg':'brreg_test_table',
# 	'google':'google_test_table',
# 	'gulesider':'gulesider_test_table',
# 	'I88I':'1881_test_table',
# 	'proff':'proff_test_table',
# 	'':'',
# }

''' _____ EXTRACTORS ____________________________________________________________'''
settings =  {	'google_settings'	 : {'chunk_size' : 50,	},
				'brreg_settings' 	 : {'chunk_size' : 1, 	},
				'gulesider_settings' : {'chunk_size' : 500, 	},
				'proff_settings' 	 : {'chunk_size' : 500, 	},
				'I88I_settings' 	 : {'chunk_size' : 500, },  }


'''
Mediavest_test_env

old: media_vest
new: Mediavest
'''



