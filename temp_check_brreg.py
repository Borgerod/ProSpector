'''
 	TEMPORARY TEST FILE THAT QUICKLY GETS BRREG TABLE AND DISPLAYS IT 
'''
'''
copy & paste:
	python temp_check_brreg.py
'''

from config import payload, tablenames, settings
from postgres import fetchData

tablename = 'brreg_table'
df = fetchData(tablename)

print(df)
