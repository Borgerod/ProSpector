import json
import pandas as pd
from tqdm import tqdm
from multiprocessing import Pool
import requests
from tqdm import tqdm



# ___ Local Imports ___
from SQL.query import getAllCategories
from SQL.insert import Insert

def	throwTracker(throws):
	'''
	keeps track of all thrown businesses
	'''
	throwTracker.counter += throws

class ProffExtractor:
	
    # TODO
	def urlBuidler(self, category:str, page_num:int) -> str:
		url = f"https://www.gulesider.no/_next/data/338IdBW7dht2IHQ27Ay-p/nb/search/{category}/companies/{page_num}/0.json"
		return url
    
    # TODO
	def getHeader(self, ) -> dict:
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

	def getReq(self, url:str) -> dict:
		return requests.request("GET", url, headers=self.getHeader()).json()
    
    # TODO
	def parseData(self, json_res:json) -> pd.DataFrame:
		return json_res['pageProps']['initialState']['companies']

    # TODO
	def worker(self, category):
		page_num , false_counter = 0 , 0
		while True:
			page_num += 1
			url = self.urlBuidler(category, page_num)
			json_res = self.getReq(url) 
			dataset = self.parseData(json_res)
			for data in dataset:
				if data['customer']:
					Insert().toGulesider(data)
				else:
					false_counter += 1
			if not dataset or false_counter > 20:
				break		

    # TODO 
	def runExtraction(self):
		throwTracker.counter = 0 # initialize throwTracker
		categories = getAllCategories()[:2]
		with Pool() as pool:
			list(tqdm(pool.imap_unordered(self.worker, categories), total = len(categories)))

if __name__ == '__main__':
	ProffExtractor().runExtraction()



