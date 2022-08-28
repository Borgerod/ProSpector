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

# tablename = 'output_table'
# tablename = 'I88I_output_table'
# tablename = 'gulesider_output_table'
tablename = 'google_input_table'
# tablename = 'output_table'
# tablename = 'input_table' # len(input_table) = 896187
# tablename = 'brreg_table' # len(input_table) = 1069577
df = fetchData(tablename)
# print(len(df)-10_000) 

print()
print(f"_____ CheckUp-Print: {tablename} _____")
print()
print(f"	COLUMN NAMES:")
print(f"		{np.array(df.columns)}")
print()
print(f"	EXAMPLE ROW:")
print('\t' + str(f"	{pd.DataFrame(df.iloc[1]).T}").replace('\n', '\n\t\t'))
# print('\t' + str(f"	{tabulate(pd.DataFrame(df.iloc[1]).T, headers='keys', tablefmt='psql')}").replace('\n', '\n\t\t'))
df = df.iloc[10000:15000]
print()
print("	TABLE:")
print('\t' + str(f"	{df}").replace('\n', '\n\t\t'))
print("_"*100)
print()


'''
TEST 1"
google_testlist = [	[816744342, 'S THORSTENSEN AS',],
				    [816762022, 'TAKSTPLAN AS',],
				    [816795842, 'VOLDENTOLLEFSEN AS',],
				    [816809932, 'ANTI AS',],
				    [816810132, 'SJÅSUND MARINE AS',],
				    [814319962, 'NORSK TAKSERING AS',],
				    [814391132, 'LATOR SKILTFABRIKK AS',],
				    [814398072, 'VARMEISOLERING AS',],
				    [814454932, 'TERAX TRANSPORTSERVICE AS',],
				    [814478912, 'THERESE GIVING',],
				    [999654126, 'A VÅGE AS',],
				    [999662757, 'ANNE MARTHE KALDESTAD HANSTVEIT',],
				    [999665497, 'ANNE KARI ØDEGÅRD',],
				    [999665896, 'BAUNEN FISK OG VILT AS',],
				    [999666612, 'FYSIOTERAPI RENATE MEIJER',],		]
input_array=google_testlist 
'''

'''
TEST 2
input_array= [[941881459, 'PETROLEUMSERVICE Robert Jacobsen',],
[941883680, 'NAMDAL GLASSERVICE AS',],
[941921280, 'TELEMIX AS',],
[941987516, 'PER MULVIK AS',],
[941988954, 'ENGØ GÅRD AS',],
[983152465, 'SHG TRANSPORT AS',],
[983154980, 'AKTIV EIENDOMSMEGLING AS',],
[983155499, 'DAVID LANDSVERK',],
[983163327, 'BUYPASS AS',],
[983164994, 'ARNULF LARSSEN AS',],]
'''