import json
import time

from sqlalchemy import create_engine; start = time.perf_counter() #Since it also takes time to Import libs, I allways start the timer asap. 
import pandas as pd
from tqdm import tqdm
from multiprocessing import Pool
from bs4 import BeautifulSoup
import requests

''' ___ local imports __________'''
# from config import tablenames
# from SQL.postgres import getInputTable, checkIfMissing, deleteData
# from base_extractor import genSearchTerm, pullRequest


''' 
	* CURRENT EXTRACTION TIME *
		- Amount of companies : 6034  
		- Finished in 11.2 second(s)
'''
# tablenames = {
# 	'input':'input_table',
# 	'output':'gulesider_test',
# }


def outroPrint():
	print("_"*62)
	print("                   Data Extraction Complete.                 ")
	print(f"                  Finished in {round(time.perf_counter() - start, 2)} second(s)                 ")
	print("_"*62)
	print()

def getPandasSettins() -> None:
	pd.options.display.max_rows = 10				# Rows 	   (length)
	pd.options.display.max_columns = None				# Columns  (width)
	pd.options.display.max_colwidth = 15			# Columns  (column display border)
	pd.options.display.width = 500		

def urlBuidler(category:str, page_num:int) -> str:
	url = f"https://www.gulesider.no/_next/data/338IdBW7dht2IHQ27Ay-p/nb/search/{category}/companies/{page_num}/0.json"
	return url

def getHeader() -> dict:
	return {
		"cookie": "55f7017582a6e57bfac34dfdb9e53ef4=e574a075ef616796844969c19a9ddd18",
		"Accept": "*/*",
		"Accept-Language": "en-US,en;q=0.9",
		"Cache-Control": "no-cache",
		"Connection": "keep-alive",
		"Cookie": "_hjSessionUser_2847992=eyJpZCI6ImE5ZGVjM2Q1LTZjZGYtNWY0ZC1iODExLTYwYzg3YTg1NzQ4ZCIsImNyZWF0ZWQiOjE2NTY2NzU3MTQyMTIsImV4aXN0aW5nIjp0cnVlfQ==; _hjSessionUser_1215995=eyJpZCI6IjBlZWRlYzcwLThiNDAtNWMxMS1iZjI0LWY3MTM0MjU5NmNjOCIsImNyZWF0ZWQiOjE2NTcxMjIyMDM1MjEsImV4aXN0aW5nIjp0cnVlfQ==; addtl_consent=1~; _enid=sm6dp3v4zv2nwh0fe75jh4626c6s30ogjsz9j49r; _dcid=dcid.1.1666388828330.100705442; euconsent-v2=CPhMsoAPhMsoAAKAsANOCmCgAAAAAH_AABpwAAASIAJMNW4gC7MscGTQMIoEQIwrCQqgUAEFAMLRAYAODgp2VgEuoIEACAUARgRAgwBRgQCAAASAJCIAJACwQAAAiAQAAgARAIQAMDAILACwMAgABANAxACgAECQgyICIpTAgKgSCA1sqEEoKpDTCAOssAKARGRUACIJAQSAAICwcAwBICViwQJMUL5ACMEKAUQAAAIAAAAA.YAAAAAAAAAAA; _cmpRepromptHash=CPhMsoAPhMsoAAKAsANOCmCgAAAAAH_AABpwAAASIAJMNW4gC7MscGTQMIoEQIwrCQqgUAEFAMLRAYAODgp2VgEuoIEACAUARgRAgwBRgQCAAASAJCIAJACwQAAAiAQAAgARAIQAMDAILACwMAgABANAxACgAECQgyICIpTAgKgSCA1sqEEoKpDTCAOssAKARGRUACIJAQSAAICwcAwBICViwQJMUL5ACMEKAUQAAAIAAAAA.YAAAAAAAAAAA.1.KTvSi1ifP7BGbdpiCttXPA==; 55f7017582a6e57bfac34dfdb9e53ef4=bd507cea0a5f1a0a309cc12fc95d926b; _ensess=7xyhqsbxlxis3oztipqi",
		"Pragma": "no-cache",
		"Referer": "https://www.gulesider.no/",
		"Sec-Fetch-Dest": "empty",
		"Sec-Fetch-Mode": "cors",
		"Sec-Fetch-Site": "same-origin",
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
		"sec-ch-ua": "^\^Google",
		"sec-ch-ua-mobile": "?0",
		"sec-ch-ua-platform": "^\^Windows^^"
	}

def getReq(url:str) -> dict:
	'''
	__idea__
	for i in category:
		spawn threads that goes through each page_num

	NOTE: alot of companies has probobly multiple categories and will show up multiple times
	'''	
	# res = requests.request("GET", url, headers=getHeader())
	return requests.request("GET", url, headers=getHeader()).json()

def parseData(json_res:json) -> pd.DataFrame:
	data = json_res['pageProps']['initialState']['companies']
	return pd.DataFrame(data)

def	throwTracker(throws):
	'''
	keeps track of all thrown businesses
	'''
	# todo: make throwTracker
	throwTracker.counter += throws

def filterCustomers(df: pd.DataFrame) -> pd.DataFrame:
	'''
		filters custemer = true
	'''
	keep = df.query("customer == True")
	throw = df.query("customer == False")
	if len(throw) > 0:
		throwTracker(throws=len(throw))
	return keep

# def main():
# 	throwTracker.counter = 0 # initialize throwTracker
# 	getPandasSettins()
# 	master_df = pd.DataFrame(
# 		columns = [
# 		'eniroId', 'name', 'phones', 'organisationNumber', 'addresses',
# 		'categories', 'districts', 'products', 'customersNearby', 'keywords',
# 		'customer', 'ranking', 'boughtDistrict', 'statisticCode', 'hitType',
# 		'tracestamps', 'rating'
# 	   ]
# 	)
# 	# TODO: Find all the categories 

# 	# for category in getCategories(): #* Original
# 	for category in getCategories()[:1]: #TEMP while testing 
# 		page_num = 0
# 		while True:
# 			page_num += 1
# 			url = urlBuidler(category, page_num)
# 			json_res = getReq(url) 
# 			df = parseData(json_res)
# 			if df.empty:
# 				print(f"\n NOTE: breaking {category}, no more pages.\n ")
# 				break
# 			df =  filterCustomers(df)
# 			master_df = pd.concat((master_df, df), axis = 0) #make one big df #! bad practice
# 	master_df = master_df.reset_index(drop = True)
# 	master_df.drop_duplicates(subset = ['organisationNumber'], keep = 'first')
	
# 	print(master_df)
# 	print("\n\n\n")
# 	print(master_df.iloc[0])

# 	print("\n\n\n")
# 	print("THROW TRACKER:")
# 	print(f"Number of times a throw occoured {throwTracker.counter}")

def main():
	throwTracker.counter = 0 # initialize throwTracker
	getPandasSettins()
	master_df = pd.DataFrame(
		columns = [
		'eniroId', 'name', 'phones', 'organisationNumber', 'addresses',
		'categories', 'districts', 'products', 'customersNearby', 'keywords',
		'customer', 'ranking', 'boughtDistrict', 'statisticCode', 'hitType',
		'tracestamps', 'rating'
	   ]
	)
	# TODO: Find all the categories 

	# for category in getCategories(): #* Original
	for category in getCategories()[:1]: #TEMP while testing 
		page_num = 0
		while True:
			page_num += 1
			url = urlBuidler(category, page_num)
			json_res = getReq(url) 
			df = parseData(json_res)
			if df.empty:
				print(f"\n NOTE: breaking {category}, no more pages.\n ")
				break
			df =  filterCustomers(df)
			master_df = pd.concat((master_df, df), axis = 0) #make one big df #! bad practice
	master_df = master_df.reset_index(drop = True)
	master_df.drop_duplicates(subset = ['organisationNumber'], keep = 'first')
	
	print(master_df)
	print("\n\n\n")
	print(master_df.iloc[0])

	print("\n\n\n")
	print("THROW TRACKER:")
	print(f"Number of times a throw occoured {throwTracker.counter}")



















def getCategories() -> list[str]:
	DATABASE_URL = f"postgresql://postgres:Orikkel1991@localhost:5432/ProSpector_Dev"
	engine = create_engine(DATABASE_URL)
	return pd.read_sql_table(
		'gulesider_categories',
		con = engine
		).category

if __name__ == '__main__':
	for category in getCategories()[:1]:
		print(category)

	# main()
	# outroPrint()



