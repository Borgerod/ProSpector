import time

from SQL.query import getAllIndustries; start = time.perf_counter() #Since it also takes time to Import libs, I allways start the timer asap. 
import requests
import pandas as pd
from tqdm import tqdm
from bs4 import BeautifulSoup
from multiprocessing import Pool
from pprint import pprint

def introPrint():
	print("_"*62)
	print("|                  Starting: Proff Extractor                 |")
	print("_"*62)
	print()

def outroPrint():
	print("_"*62)
	print("                  Data Extraction Complete.                 ")
	print(f"                  Finished in {round(time.perf_counter() - start, 2)} second(s)                ")
	print("_"*62)
	print()



class ProffExtractor:
	def __init__(self) -> None:
		self.is_first = True
		self.has_next = False
		self.tag = None
		self.url = None
		self.industry = None
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

	def getNextUrl(self):
		''' #TODO find next url 
		next_button, xpath = "//*[@id="main-content"]/div[3]/ul/li[2]/a" 
		'''
		self.url = "https://proff.no/s%C3%B8k-etter-bransje/YLoFmCo_zvNZxJID58xbvLFl_00WkiF1YhtKdVP2DH7q9ML7fkP1mBywa54Z7cJoB95okX8KgB_jyc8RyUuAEbEunxKnGneeVGNEa7RQfm8/" 
		self.is_first = False
		self.has_next = True

	def checkNext(self):
		if self.has_next:
			return self.setNextUrl(), self.setNextHeader()
		else:
			return self.setUrl()
			
	def setUrl(self):
		self.url=f"https://proff.no/bransjes%C3%B8k?q={self.industry}"
	
	def setNextUrl(self):
		self.url = self.getNextUrl()

	def setNextHeader(self):
		self.header = {"cookie": "AWSALB=2iWR8RxS7C8uIcRLei2d%2FJOASl9w18tZmcOFb7QbD23mgClQMPif7z9AvbR%2BrmD9IWcqGNWsfOoSiobdunkNSxXcPofA8%2BqZDd7JSQTRytytS5nfjEH8SXHVkAeO; AWSALBCORS=2iWR8RxS7C8uIcRLei2d%2FJOASl9w18tZmcOFb7QbD23mgClQMPif7z9AvbR%2BrmD9IWcqGNWsfOoSiobdunkNSxXcPofA8%2BqZDd7JSQTRytytS5nfjEH8SXHVkAeO; JSESSIONID=6D6C6C1B5081003249B99A12208B7E48"}

	def getData(self, req):
		req = requests.request("GET", self.url, headers = self.header)
		# return requests.request("GET", url, headers=self.getHeaders(), verify=True)
		return BeautifulSoup(req.content, "html.parser") #* -> soup

	def getWrapper(self, soup):
		return soup.find('div', class_="search-container-wrap")

	def getTag(self):
		'''
		#TODO: finish this 
		'''
		return promo.div['class'][2]	


	def worker(self, industry):
		# page_num , false_counter = 0 , 0
		# # while True:
		# page_num += 1
		self.industry = industry
		url = self.setUrl()
		soup = self.getData(url) 
		wrapper = soup.find('div', class_="search-container-wrap")
		# print(len(wrapper))
		# print(list(wrapper)[1])
		# //*[@id="main-content"]/div[2]/section/div[3]/div[1]
		
		# a_list = wrapper.findAll('a', class_="addax addax-cs_hl_hit_company_name_click")
		# print(len(a_list))
		# print()
		# for row in list(wrapper)[1:]:



		# <div class="org-number" data-id="965614923">
            
		for row in wrapper:
			try:
				if row.find('a', class_="addax addax-cs_hl_hit_company_name_click"):
					company_name = row.find('a', class_="addax addax-cs_hl_hit_company_name_click").text
					org_num = row.find('div', class_="org-number")
					if not 'search-container clear low-priority' in str(row):
						print(False, company_name, org_num['data-id'])
						# TODO: make insert
					# else:
					# 	print(True, company_name, org_num['data-id'])

			except:
				pass

			# print(str(row))
	
			
			# if 'search-container clear low-priority' in str(row):
			# 	print(True)
			# else:
			# 	print(False)

			# break
			# try:
			# 	tag = row.div['class']
			# 	print(tag)
			# 	# if 'low-priority' in tag:
			# 	# 	print
			# 	# 	print(True)
			# 	# else:
			# 	# 	print(False)
			# except:
			# 	pass
			# tag = self.getTag() 
		# 	if i:
		# 		print(True)
		# 	else: 
		# 		print(False)
		# 	break
			# print(f"""
			# {i}
			# """)
			
		# wrapper_list = self.getWrapper(req)
		# tag = self.getTag()
		# for data in wrapper_list:
		# 	print(data)
		# 	break
		# 	if 'low-priority' in tag:
		# 		print("low-prio")
		# 	else:
		# 		print("high-prio")
			
			# 		Insert().toProff(data)
			# 	else:
			# 		false_counter += 1
			# if not dataset or false_counter > 20:
			# 	break		

    # TODO 
	def runExtraction(self):
		# throwTracker.counter = 0 # initialize throwTracker
		industries = getAllIndustries()[:1]
		
		for industry in industries:
			print(industry)
			self.worker(industry)
			break
		# with Pool() as pool:
		# 	list(tqdm(pool.imap_unordered(self.worker, industries), total = len(industries)))

if __name__ == '__main__':
	ProffExtractor().runExtraction()





# if self.next_url==None:

# 	def getNextBaseUrl(self):
# 		next_base_url = "https://proff.no/s%C3%B8k-etter-bransje/YLoFmCo_zvNZxJID58xbvLFl_00WkiF1YhtKdVP2DH7q9ML7fkP1mBywa54Z7cJoB95okX8KgB_jyc8RyUuAEbEunxKnGneeVGNEa7RQfm8/"

# 	def getQueryString(self):
# 		querystring = {"q":"Advokater og juridiske tjenester"}
	
# 	def getNextHeaders(self):
# 		headers = {"cookie": "AWSALB=2iWR8RxS7C8uIcRLei2d%2FJOASl9w18tZmcOFb7QbD23mgClQMPif7z9AvbR%2BrmD9IWcqGNWsfOoSiobdunkNSxXcPofA8%2BqZDd7JSQTRytytS5nfjEH8SXHVkAeO; AWSALBCORS=2iWR8RxS7C8uIcRLei2d%2FJOASl9w18tZmcOFb7QbD23mgClQMPif7z9AvbR%2BrmD9IWcqGNWsfOoSiobdunkNSxXcPofA8%2BqZDd7JSQTRytytS5nfjEH8SXHVkAeO; JSESSIONID=6D6C6C1B5081003249B99A12208B7E48"}
















# def getRequest(url):
# 	cookies = { 'ASP.NET_SessionId':'5btxqhyab4kildcfudsowc31',
# 				'__uzma':'c8749bb2-abdf-40b3-b4e2-3377bc4d33ae',
# 				'__uzmb':'1660651793',
# 				'__ssds':'2',
# 				'__uzmaj2':'b50a61ac-fc20-49eb-aea0-9b9f7a292f82',
# 				'__uzmbj2':'1660651794',
# 				'_gid':'GA1.2.1371187027.1660652841',
# 				'__ssuzjsr2':'a9be0cd8e',
# 				'_MBL':'%7B%22u%22%3A%22G6fq8SYahK%22%2C%22t%22%3A1660653383%7D',
# 				'__mbl':'%7B%22u%22%3A%5B%7B%22uid%22%3A%22YEIoShT3dFg6GprZ%22%2C%22ts%22%3A1660653384%7D%2C1660743384%5D%7D',
# 				'_ga_60EFTS75DG':'GS1.1.1660652841.1.1.1660653384.0',
# 				'_ga':'GA1.1.1591735888.1660652841',
# 				'__uzmcj2':'995972548674',
# 				'__uzmdj2':'1660653739',
# 				'captchaResponse':'1',
# 				'__uzmc':'856834036869',
# 				'__uzmd':'1660653747',}
# 	return requests.get(url, cookies=cookies, verify=True) #* -> req 


# def checkPayScore(org_num, search_term, tag ,error):
# 		if 'PRF_PAK_KOMPLETT' in tag:
# 			print("True")
# 			tag_score = 6
# 			return org_num, search_term, tag_score ,error 
# 		elif 'PRF_PAK_TREFF' in tag: 
# 			tag_score = 5
# 			return org_num, search_term, tag_score ,error 
# 		elif 'PRF_PAK_STANDARD' in tag: 
# 			tag_score = 4
# 			return org_num, search_term, tag_score ,error 
# 		elif 'PRF_PAK_BASIS' in tag: 
# 			tag_score = 3
# 			return org_num, search_term, tag_score ,error 
# 		elif 'PRF_PAK_INTRO' in tag: 
# 			tag_score = 2
# 			return org_num, search_term, tag_score ,error 
# 		elif 'PRF_PAK_INFO' in tag: 
# 			tag_score = 1
# 			return org_num, search_term, tag_score ,error 

# def makeChunks(input_array, chunksize):
# 	return [input_array[i:i+chunksize] for i in range(0, len(input_array), chunksize)]  



# def extractionManager(input_array):
# 	'''
# 		finds profile for company, then checks if profile 
# 		contains a promo banner for payed entries
# 	'''
# 	# org_num = input_array[0]
# 	# search_term = input_array[1]
# 	# if not checkIfMissing(org_num):
# 	# source = 'proff.py'
# 	# base_url = 'https://www.proff.no/bransjesøk?q='
# 	url = linkBuilder(industry)       
# 	req = getRequest(url)
# 	soup = getSoup(req)
# 	try:
# 		promo = soup.find('div', class_="search-container-wrap")
# 		tag = promo.div['class'][2]		
# 		if 'low-priority' in tag: 
# 			pass
# 		else:
# 			deleteData(org_num, tablename = "input_table") #* All inputs that are found can be deleted from input_table 
# 			return org_num, search_term 
# 	except AttributeError as e:
# 		errorManager(org_num, search_term, source, url, e)
# 	# else:
# 	# 	pass

# def proffExtractor(**kwargs):
# 	'''
# 		sets up all nessasary functions, then gets list of company names, 
# 		then iterates through the list via multithreading: claimedStatus().
# 	'''
# 	introPrint()


# 	''' making adjustments if testmode '''
# 	if kwargs.get('testmode', None):
# 		input_array = input_array[:1000]
# 	print(f"chunksize: {chunksize}")
# 	print(f"input length: {len(input_array)}")
# 	nested_input_array = makeChunks(input_array, chunksize) 
# 	print(f"number of chunks: {len(nested_input_array)}")
# 	with tqdm(total = len(nested_input_array)) as pbar: 
# 		for input_array in nested_input_array:
# 			with Pool() as pool:
# 				results = list(tqdm(pool.imap_unordered(extractionManager, input_array), total = len(input_array)))
# 				results = [x for x in results if x is not None]
# 				df =  pd.DataFrame(results, columns = ['org_num', 'navn'])
# 				print(df)
# 				databaseManager(df, tablename = "output_table")
# 				pbar.update(1)
# 	outroPrint()

	





# # if __name__ == '__main__':
# # 	proffExtractor(testmode = False)








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




