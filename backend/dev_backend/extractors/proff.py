import json
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

# TODO [ ] implement phone number 

''' 
____ Track_record ____
	tot. time:  49.620s 
'''

class ProffExtractor:
	def __init__(self) -> None:
		self.has_next = False
		self.is_first = True
		self.is_last = False
		self.base_url = 'https://proff.no/s%C3%B8k-etter-bransje/'
		self.url = None
		self.profile_url = None
		self.industry = None
		self.soup = None
		self.false_limit_reached = False
		
		self.company_name =None
		self.org_num =None
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

	def getData(self):
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

	def getOrgNum(self, row) -> int:
		org_num_dirty = row.find('div', class_="org-number").text
		org_num_clean = org_num_dirty.replace('\n', '').replace('Org nr ', '').replace(' ', '')
		return int(org_num_clean)



	def extractPage(self):
		self.soup = self.getData() 
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
							self.company_name = row.find('a', class_="addax addax-cs_hl_hit_company_name_click").text
							# print(f"https://www.gulesider.no/{self.company_name}/bedrifter")
							self.org_num = self.getOrgNum(row)
							self.org_num =  int((row.find('div', class_="org-number").text)['data-id'])
							self.tlf = self.getPhoneNumber(row) #TEMP 
							print([self.company_name, self.org_num, self.tlf])
							Insert().toProff(self.org_num, self.company_name, self.tlf)
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



# https://proff.no/s%C3%B8k-etter-bransje/
# /selskap/advokatfirmaet-mageli-da/lillestr%C3%B8m/advokater-og-juridiske-tjenester/IEKB3H207U6-3/
# https://proff.no/selskap/advokatfirmaet-mageli-da/lillestr%C3%B8m/advokater-og-juridiske-tjenester/IEKB3H207U6-3/
# https://proff.no/selskap/advokatfirmaet-mageli-da/lillestr%C3%B8m/advokater-og-juridiske-tjenester/IEKB3H207U6-3/



# /selskap/tut-for-top20-da/stabekk/adresseringsleverand%C3%B8rer/IG8M3FT07U7/

	def getPhoneNumber(self, row) -> str:
		try:
			# tries to find number in company list 
			return row.find('a', class_="addax addax-cs_hl_hit_phone_click").text
		except:
			try:
				# WILL MAKE NUMBER SEARCH ON GULESIDER:
				self.url = f"https://www.gulesider.no/{self.company_name}/bedrifter"
				script = self.getData().find('script', id = "__NEXT_DATA__")
				return json.loads(script.contents[0])['props']['pageProps']['initialState']['companies'][0]['phones'][0]['number']
			except:
				pass
				# print(f"""ERROR; could not find tlf for:
				# {self.profile_url}
				# """)



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

	# TEMP WHILE TESTING
	def runExtraction(self):
		'''
		starting off with resetting the old table, to be replaced with new data
		'''
		# Reset().proff()
		industries = getAllProffIndustries()
		industries = industries[:3]#TEMP
		with Pool() as pool:
			list(tqdm(pool.imap_unordered(self.worker, industries), total = len(industries)))


	#* ORIGINAL 
	# def runExtraction(self):
	# 	'''
	# 	starting off with resetting the old table, to be replaced with new data
	# 	'''
	# 	Reset().proff()
	# 	industries = getAllProffIndustries()
	# 	with Pool() as pool:
	# 		list(tqdm(pool.imap_unordered(self.worker, industries), total = len(industries)))

if __name__ == '__main__':
	ProffExtractor().runExtraction()

