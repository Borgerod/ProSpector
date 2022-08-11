import os
import re
import string
import time 
import pandas as pd
import numpy as np
from os import path
from tqdm import tqdm
import concurrent.futures
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from inspect import currentframe, getframeinfo
import json
import psycopg2
from psycopg2.extras import Json
from sqlalchemy import create_engine
from tqdm import tqdm
import pandas as pd 
import requests 
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd 
import json
import psycopg2
from psycopg2.extras import Json
from sqlalchemy import create_engine
import concurrent.futures
from tqdm import tqdm
from config import payload, tablenames, settings
from postgres import getInputTable


df1=pd.DataFrame({'org_num':[1,2,3,3],'B':[2,3,4,4]})
df2=pd.DataFrame({'org_num':[1],'B':[2]})
# diff = pd.concat([df1,df2]).drop_duplicates(keep=False)
# print(df1)
# print(df2)
# print(diff)

df = pd.concat([df1, df2])
# df = df.reset_index(drop=True)
# print(df)
# print()
# df_gpby = df.groupby(list(df.columns))
# print(df_gpby)
# idx = [x[0] for x in df_gpby.groups.values() if len(x) == 1]
# df.reindex(idx)
# print(df)
print(df)
print("_____")
d = df.duplicated(subset=['org_num'], keep=False)
# df=df[df-d]
# df=df[-d]
df=df[-d]
print(df)
print("______")
if d.contains(True):
	print(d)
# df = getInputTable('brreg_table')
# print(len(df))
# print(df)

# # df.set_index(['org_num'], inplace = True)
# df = df.drop_duplicates(subset='org_num')
# print(df)

# df = pd.DataFrame([input_array])
''' ___ PART 1, BBREG API ____________________________________________________ '''

	# ## OLD GETREQUEST()
	# # def getRequest():
	# # 	url = 'https://data.brreg.no/enhetsregisteret/api/enheter/?page=3&size=20' #-i -X GET
	# # 	r = requests.get(url, timeout=10)
	# # 	json = r.json()
	# # 	return json

	# # NEW GETREQUEST()
	# def getRequest(next_page):
	# 	url = f'https://data.brreg.no/enhetsregisteret/api/enheter/?page={next_page}&size=20' #-i -X GET
	# 	r = requests.get(url, timeout = 10)
	# 	json = r.json()
	# 	return json


	# def getpage(json):
	# 	page =  json['page']
	# 	return page

	# def getMaxpages(page):
	# 	''' 
	# 		gets the total number of pages from JSON, 
	# 		used for breaking the loop 
	# 	'''
	# 	total_pages = page['totalPages']
	# 	return total_pages


	# def gettotalElements(page):
	# 	''' 
	# 		gets the total number of elements (Companies) from JSON, 
	# 		used for supervising & calculations
	# 	'''
	# 	total_elements = page['totalElements']
	# 	return total_elements

	# def main():
	# 	next_page=0
	# 	json = getRequest(next_page)
	# 	page = getpage(json)
	# 	print(getMaxpages(page))
	# 	print((gettotalElements(page)))
	# 	'''
	# 	totalElements: 1078364
	# 	maxPages: 53919
	# 	'''


	# if __name__ == '__main__':
	# 	main()






''' ____ EXPERIMENTAL: Self Referance  ____________________________'''

# def getLineNumber():
# 	''' gets current line number --> linenumberpath '''
# 	return currentframe().f_back.f_lineno

# def getFilePath():
# 	''' gets current filepath --> filepath '''
# 	return getframeinfo(currentframe()).filename

# def getRelativePath():
# 	''' gets relative filepath for current file --> shortpath '''
# 	return '/'.join(map(str,getFilePath().split('\\')[-2:]))

# def getFileName():
# 	''' gets filename for current file --> filename '''
# 	return re.split("[/,.]+", getRelativePath())[1]



# ''' ____ NEW EXPERIMENTAL: parse tablename & settings  ____________________________'''

# def parseTablenames(file_name):
# 	''' parses file specific tablename from settings --> settings'''
# 	return tablenames[file_name]


# def parseSettings(file_name):
# 	''' parses file specific settings from settings --> settings'''
# 	return settings[f'{file_name}_settings']




# ''' _________________________  MAIN _________________________'''
# def main():
# 	# NOTE: for some interesting dynamics -> consider using getRelativePath() from EXPERIMENTAL: Self Referance. 
# 	file_name = getFileName()
# 	# file_name = 'google' #self reference for parsing the correct settings

# 	# calling parsers 
# 	tablename = parseTablenames(file_name)
# 	settings = parseSettings(file_name)
# 	# specific parsing of settings:
# 	chunk_size = settings['chunk_size']
# 	print(chunk_size)
# 	print(tablename)
# 	print(settings)

# if __name__ == '__main__':
# 	main()

