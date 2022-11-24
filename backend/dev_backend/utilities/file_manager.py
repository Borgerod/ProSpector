import re
from inspect import currentframe, stack

# ___ local imports __________
# from ..SQL.core.__config import tablenames, settings
# from postgres import fetchData


''' ____ NEW EXPERIMENTAL: parse tablename & settings  ____________________________'''

def parseTablenames(file_name, **kwargs):
	''' parses file specific tablename from settings --> settings'''
	return tablenames[file_name]
	
def parseSettings(file_name):
	''' parses file specific settings from settings --> settings'''
	return settings[f'{file_name}_settings']

''' ____ EXPERIMENTAL: Self Referance  ____________________________'''

def getLineNumber():
	''' gets current line number --> linenumberpath '''
	return currentframe().f_back.f_lineno

def getFilePath():
	''' gets current filepath --> filepath '''
	return stack()[1].filename 

def getRelativePath():
	''' gets relative filepath for current file --> short_path '''
	return '/'.join(map(str, stack()[1].filename.split('\\')[-2:]))

def getFileName():
	''' gets filename for current file --> file_name '''
	return re.split("[/,.]+", ('/'.join(map(str, stack()[1].filename.split('\\')[-2:]))))[1]

def getLastUpdate(col_name):
	'''
		gets the date for when a table was last modified from update_tracker
		- "update_tracker" is a seperate small table that is updated after each sucsessfull run
		
		Note:  to avoid confusion, the variable "tablename" passed when calling getLastUpdate(tablename) is renamed to col_name, 
			   since fetchData() also uses "tablename"		
	'''
	df = fetchData(tablename = parseTablenames('update_tracker')) # fetches tablename for "update_tracker" from config, then fetchess df for database
	return df.iloc[0][col_name] # fetches date-cell for "col_name" returns -> str 

