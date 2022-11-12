import time
from SQL.insert import Insert
import SQL.db as db
from SQL.query import getAllProffIndustries
from SQL.reset import Reset; start = time.perf_counter() #Since it also takes time to Import libs, I allways start the timer asap. 
import requests
import pandas as pd
from tqdm import tqdm
from bs4 import BeautifulSoup
from multiprocessing import Pool
from pprint import pprint



''' 
____ Track_record ____
	tot. time:  49.6200s 
'''

class ProffExtractor:
	def __init__(self) -> None:
		self.has_next = False
		self.is_first = True
		self.is_last = False
		self.base_url = 'https://proff.no/s%C3%B8k-etter-bransje/'
		self.url = None
		self.industry = None
		self.soup = None
		self.false_limit_reached = False
		self.header = {
			"cookie": "_hjSessionUser_1569514=eyJpZCI6ImZjZGEyYWI0LWFlMGMtNWQxMS1hOTZiLTdlNDQwZWUxYmRmYiIsImNyZWF0ZWQiOjE2NTY2NzM5NDE5MzgsImV4aXN0aW5nIjp0cnVlfQ==; euconsent-v2=CPhHQPEPhHQPEAKAXBNOClCgAAAAAH_AABpwAAARvABIFS4gAbAoMCSAAIgEQIgrAAIAUAEAAACBAAAAAAAQAgEqAIAAAAAAAABAAwBQAQCAAAAAAAAAAAAgQAAACAAAAAAAAAAAEAAIIACgMAgABAJAAAAgAACAgAACAABAAAgACAAgIAAoAJBTCAAEAAAABCQEACAAAAAAAAAgMAQAACRAQQAAAAAAAAAAAAQAAAAA.YAAAAAAAAAAA; _pa=PA2.0370463469796563; JSESSIONID=D83F04B5C695B4C327334C5C247C2B6F; _gid=GA1.2.1949323138.1667834959; _pk_ses.2.d737=1; ln_or=d; _pk_id.2.d737=84b3886ac0cec608.1667313613.2.1667835574.1667834959.; _ga=GA1.2.810621682.1666167700; _gat=1; _ga_JKQ3JPCECD=GS1.1.1667834959.12.1.1667835718.0.0.0; AWSALB=gnCHn+q27D1uOnOaLty8yUB9fZc1Ngnx7BsLvpfoLKsOzQIq70b0V7Yik2veJEpg/xoDqI55hS+9S37Jk70Xdk51ptQX5kCzpAtnKsmGO2zHnsC3SxYROxaIsLGK; AWSALBCORS=gnCHn+q27D1uOnOaLty8yUB9fZc1Ngnx7BsLvpfoLKsOzQIq70b0V7Yik2veJEpg/xoDqI55hS+9S37Jk70Xdk51ptQX5kCzpAtnKsmGO2zHnsC3SxYROxaIsLGK",
			"authority": "proff.no",
			"accept": "*/*",
			"accept-language": "en-US,en;q=0.9",
			"cache-control": "no-cache",
			"pragma": "no-cache",
			"referer": "https://proff.no/s^%^C3^%^B8k-etter-bransje/adresseringsleverand^%^C3^%^B8rer/I:10159/?q=Adresseringsleverand^%^C3^%^B8rer",
			"sec-ch-ua": "^\^Google",
			"sec-ch-ua-mobile": "?0",
			"sec-ch-ua-platform": "^\^Windows^^",
			"sec-fetch-dest": "empty",
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-origin",
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
		}

	def setUrl(self):
		self.url = f"https://proff.no/bransjes%C3%B8k?q={self.industry}"

	def setNextHeader(self):
		self.header = {"cookie": "AWSALB=2iWR8RxS7C8uIcRLei2d%2FJOASl9w18tZmcOFb7QbD23mgClQMPif7z9AvbR%2BrmD9IWcqGNWsfOoSiobdunkNSxXcPofA8%2BqZDd7JSQTRytytS5nfjEH8SXHVkAeO; AWSALBCORS=2iWR8RxS7C8uIcRLei2d%2FJOASl9w18tZmcOFb7QbD23mgClQMPif7z9AvbR%2BrmD9IWcqGNWsfOoSiobdunkNSxXcPofA8%2BqZDd7JSQTRytytS5nfjEH8SXHVkAeO; JSESSIONID=6D6C6C1B5081003249B99A12208B7E48"}

	def getData(self, req):
		req = requests.request("GET", self.url, headers = self.header)
		# return requests.request("GET", url, headers=self.getHeaders(), verify=True)
		return BeautifulSoup(req.content, "html.parser") #* -> self.soup

	def checkIfNextPageButton(self):
		''' will look for this section in html:
			<a href="/s%C3%B8k-etter-bransje/YLoFmCo_zvNZxJID58xbvLFl_00WkiF1YhtKdVP2DH7q9ML7fkP1mBywa54Z7cJoB95okX8KgB_jyc8RyUuAEbEunxKnGneeVGNEa7RQfm8/" class="arrow ssproff-right">
		'''
		try:
			next_button = self.soup.find('a', class_ = "arrow ssproff-right")
			if next_button:
				self.url =  self.base_url+next_button['href']
				self.is_first = False
				self.has_next = True
				self.setNextHeader()
			else:
				self.has_next = False
				self.is_last = True
		except:
			self.has_next = False 
			self.is_last = True

	def extractPage(self):
		self.soup = self.getData(self.url) 
		wrapper = self.soup.find('div', class_="search-container-wrap")
		false_counter = 0 		#reset counter
		company_row_count = 0 	#reset counter		
		try:
			for row in wrapper:
				try:
					''' checks if row has a company in it, some rows has ads or are empty 
					'''
					if row.find('a', class_="addax addax-cs_hl_hit_company_name_click"):  
						company_row_count +=1
						if 'search-container clear low-priority' not in str(row):
							company_name = row.find('a', class_="addax addax-cs_hl_hit_company_name_click").text
							org_num = row.find('div', class_="org-number")
							Insert().toProff(int(org_num['data-id']), company_name)
						else:
							false_counter += 1
							if false_counter == company_row_count:
								self.false_limit_reached = True
				except:
					pass
			
			self.checkIfNextPageButton()
		except:
			print(f"""


			ERROR WRAPPER WAS NONETYPE:
			{self.industry}
			{self.url}


			{wrapper}
			

			""")
				
	def worker(self, industry):
		self.industry = industry
		self.setUrl()
		self.extractPage()
		while self.has_next:
			self.extractPage()
			if self.false_limit_reached:
				break
			
	

	def splitlist(self, _industries:list, size:int) -> list[list]:
		return [_industries[i:i + size] for i in range(0, len(_industries), size)]   

	def runExtraction(self):
		'''
		starting off with resetting the old table, to be replaced with new data
		'''
		Reset().proff()
		industries = getAllProffIndustries()
		with Pool() as pool:
			list(tqdm(pool.imap_unordered(self.worker, industries), total = len(industries)))

if __name__ == '__main__':
	ProffExtractor().runExtraction()




''' TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP 
							
*						_____ WHERE I LEFT OF _____
-						[17.08.2022]


*						_____ EXTRACTION RECORD _______
*						Extracts (1000) units -->  	26.5 second(s) 				  | => (1000) :  26.50 sec | [0.027 s/unit]
*						Extracts (483.500) units -->  	22029.89 second(s)		  | => (1000) :  45.60 sec | 0.0456 s/unit]	
						967 * 500 = 483500 [6:07:07]
*						Extracts (975500) units -->  	36402.69 second(s)		  | => (1000) :  37.30 sec | 0.0373 s/unit]	
						1951 * 500 = 975500 [10:06:42]

*						_____ ESTIMATIONS _______
*						Estimated length of input_list: 						1.069.577 rows / [1069577]
*						Estimated total extraction time: 						[13:32:52] / 812.88 minutes 
* 						ACTUAL TOTAL EXTRACTION TIME: 							[10:06:42] / 606.71 minutes
	
TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP TEMP'''




