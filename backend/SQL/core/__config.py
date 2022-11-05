
# #+! SECURITY RISK
# 	#! THIS SHOULD NOT BE HERE !!!

# '''
# Config
# '''

# ''' _____ POSTGRES ____________________________________________________________ '''
# payload = {		'dbname'   		: 'ProSpector_Dev',
#  				'dbname2' 	 	: 'ProSpector_User_API',
#  				'test_dbname'	: 'Mediavest_test_env',
# 				'host'     		: 'localhost',
# 				'user'     		: 'postgres',
# 				'password' 		: 'Orikkel1991',  }

# tablenames = {	'brreg' 	   			: 'brreg_table',
# 				'update_tracker' 		: 'update_tracker',		  
				
# 				'I88I_output_table'		: 'I88I_output_table',
# 				'proff_output_table'	: 'proff_output_table',
# 				'gulesider_output_table' : 'gulesider_output_table',	
				
# 				'google' 	   			: 'google_output_table',
# 				'google_input' 			: 'google_input_table',
				
# 				'error_table'			: 'error_table',

# 				'call_list' 			: 'call_list',
# 				'user' 					: 'user',
# 				'overview_mediavest' 	: 'call_list_overview_mediavest',	}
									
# # OLD TABLENAME
# # tablenames = {	'google' 	   			: 'google_output_table',
# 				# 'brreg' 	   			: 'brreg_table',
# 				# 'gulesider'    			: 'gulesider_table',
# 				# 'input'  				: 'input_table',
# 				# 'output' 				: 'output_table',
# 				# 'I88I' 					: '1881_table',
# 				# 'proff' 				: 'proff_table',
# 				# 'google_input' 			: 'google_input_table',
# 				# 'gulesider_error_table' : 'gulesider_error_table',
# 				# 'update_tracker' 		: 'update_tracker',		  
# 				# 'call_list' 			: 'call_list',
# 				# 'I88I_output_table'		: 'I88I_output_table',
# 				# 'gulesider_output_table' : 'gulesider_output_table',	}


# '''
# 	dict of all the extractor filenames (.py files), listed in chronological order.  
# '''
# extractor_filenames = {	'input' 					: [	'brreg', 'input_table',	],
# 						'first_output' 				: [	'1881', 'gulesider', 'proff', 'output_table' ],
# 						'second_output'    			: 	'google',
# 						'final' 		   			: 	'call_list',									}

# extractor_filenames = {	'first' 					: 	'brreg',
# 						'second' 					: [	'1881', 'gulesider', 'proff'	],
# 						'third'						: 	'google',										}

# table_managers = {	'first' 					: 	'brreg',
# 					'input'    					: 	'input_table',
# 					'second' 					: [	'1881', 'gulesider', 'proff'	],
# 					'first_output'				: 	'output_table',
# 					'third'						: 	'google',
# 					'final_output'    			: 	'call_list',
# 					'second_output'    			: 	'call_list',
# 					'final' 		   			: 	'call_list',										}

# ''' _____ EXTRACTORS ____________________________________________________________'''
# settings =  {	'google_settings'	 : {'chunk_size' : 50,		},
# 				'brreg_settings' 	 : {'chunk_size' : 1, 		},
# 				'gulesider_settings' : {'chunk_size' : 500, 	},
# 				'proff_settings' 	 : {'chunk_size' : 500, 	},
# 				'I88I_settings' 	 : {'chunk_size' : 500, 	},  }

