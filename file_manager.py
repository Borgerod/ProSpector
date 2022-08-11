import re
from inspect import currentframe, getframeinfo, stack

# ___ local imports __________
from config import tablenames, settings


''' ____ NEW EXPERIMENTAL: parse tablename & settings  ____________________________'''

def parseTablenames(file_name):
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
	# return getframeinfo(currentframe()).filename

	return stack()[1].filename 

def getRelativePath():
	''' gets relative filepath for current file --> short_path '''
	return '/'.join(map(str, stack()[1].filename.split('\\')[-2:]))

def getFileName():
	''' gets filename for current file --> file_name '''
	return re.split("[/,.]+", ('/'.join(map(str, stack()[1].filename.split('\\')[-2:]))))[1]

