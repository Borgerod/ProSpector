'''
 	TEMPORARY TEST FILE THAT QUICKLY GETS BRREG TABLE AND DISPLAYS IT 
'''
'''
copy & paste:
	python print_table.py
'''

from config import payload, tablenames, settings
from postgres import fetchData
import numpy as np
from tabulate import tabulate
import pandas as pd

''' Pandas Settings '''
# df.style.set_properties(**{'text-align': 'center'})
# pd.options.display.max_rows = None				# Rows 	   (length)
pd.options.display.max_columns = None				# Columns  (width)
pd.options.display.max_colwidth = None			# Columns  (column display border)
pd.options.display.width = 2000					# Whole	   (dataframe display border)




'''* __ LIST OF ALL TABLES __ 
	* Main Tables:
	- brreg_table
	- google_table
	- gulesider_table
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


tablename = 'output_table'
df = fetchData(tablename)

print()
print(f"_____ CheckUp-Print: {tablename} _____")
print()
print(f"	COLUMN NAMES:")
print(f"		{np.array(df.columns)}")
print()
print(f"	EXAMPLE ROW:")
print('\t' + str(f"	{pd.DataFrame(df.iloc[1]).T}").replace('\n', '\n\t\t'))
# print('\t' + str(f"	{tabulate(pd.DataFrame(df.iloc[1]).T, headers='keys', tablefmt='psql')}").replace('\n', '\n\t\t'))
print()
print("	TABLE:")
print('\t' + str(f"	{df}").replace('\n', '\n\t\t'))
print("_"*100)
print()