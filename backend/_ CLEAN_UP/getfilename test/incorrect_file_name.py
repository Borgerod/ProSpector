import re
from inspect import currentframe, getframeinfo, stack
# import inspect

# local 
from config import tablenames


''' ____ NEW EXPERIMENTAL: parse tablename & settings  ____________________________'''

def parseTablenames(file_name):
	''' parses file specific tablename from settings --> settings'''
	return tablenames[file_name]


''' ____ EXPERIMENTAL: Self Referance  ____________________________'''

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
