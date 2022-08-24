'''
 	TEMPORARY TEST FILE THAT QUICKLY GETS BRREG TABLE AND DISPLAYS IT 
'''
'''
copy & paste:
	python print_table.py
'''

from config import payload, tablenames, settings
from postgres import fetchData


'''* __ LIST OF ALL TABLES __ 
	* Main Tables:
	- brreg_table
	- google_table
	- guldesider_table
	  1881_table  [inactive]
	  proff_table [inactive]


	* Input/Output Tables:
	- input_table
	- output_table
	- update_tacker
	  google_input_table [inactive]

	* Test Tables:
	- google_test_table
	- gulesider_test_table
	- test_table

	* Error Tables:
	  google_error_table 	[inactive]
	  gulseider_error_table [inactive]
'''


tablename = 'gulesider_test_table'
df = fetchData(tablename)

print(df)
