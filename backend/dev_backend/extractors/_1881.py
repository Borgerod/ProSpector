import json
# from SQL.models.insert import Insert
# from SQL.
import SQL.db as db
from SQL.query import Insert, getAll1881Industries
from SQL.reset import Reset
import requests
import pandas as pd
from tqdm import tqdm
from bs4 import BeautifulSoup
from multiprocessing import Pool
from pprint import pprint
import re 

# TODO [ ] implement phone number 


''' 
____ Track_record ____
	tot. time:  609.630s (10.16m)
'''

''' NOTE
It would probably be a good idea to save the id_number from the profilelinks, (and profile_name while were at it) e.g.: 
	"100347174S1" <--https://www.1881.no/adopsjon/adopsjon-agder/adopsjon-kristiansand-s/inor-adopt_100347174S1/"
		and "adopsjon-kristiansand-s" 
if I already have those then i don't need to extract those links anymore, and can just generate them myself. 
'''


class SecondLevelThread:
	'''
	is spawned by _1881Extractor-thread
	concurently iterates through the pages for each industry. 
	'''

class _1881Extractor:
	
	def __init__(self) -> None:
		self.base_url = "https://www.1881.no"   
		self.industry = None
		self.url = None
		self.profile_url = None
		self.has_next = True
		self.reached_limit = False
		self.profile_url_snippet = None
		# self.profile_name = None
		self.header = {
				"cookie": "__uzma=e69d520f-a8db-46ec-b5d1-7d2e26930e28; __uzmc=163051371814; __uzmb=1668010547; __uzmd=1668010570;captchaResponse=1; Expires=null; Path=/; Domain=www.1881.no",
				"authority": "cdn.pbstck.com",
				"accept": "*/*",
				"accept-language": "en-US,en;q=0.9",
				"cache-control": "no-cache",
				"origin": "https://www.1881.no",
				"pragma": "no-cache",
				"referer": "https://www.1881.no/sitemap/industries-a/",
				"sec-ch-ua": "^\^Google",
				"sec-ch-ua-mobile": "?0",
				"sec-ch-ua-platform": "^\^Windows^^",
				"sec-fetch-dest": "empty",
				"sec-fetch-mode": "cors",
				"sec-fetch-site": "cross-site",
				"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
			}

	def getSoup(self, url:str = None) -> BeautifulSoup:
		response = requests.request("GET", 'https://www.1881.no/Error/PageNotFound', headers = self.header)	#Just for returning a empty/useless soup 
		if url:
			''' gets profile '''
			try:
				response = requests.request("GET", url, headers = self.header)
			except requests.exceptions.TooManyRedirects as e:
				print(f"""
				ERROR TooManyRedirects:
				{url}

				{e}

				""")
		else:
			''' gets profile list '''
			response = requests.request("GET", self.url, headers = self.header)
		return BeautifulSoup(response.content, "html.parser")

	def checkForPayedEnrtryInProfile(self, profile:BeautifulSoup) -> BeautifulSoup:
		return 'Søkeord' in profile.text 

	def checkForPayedEnrtryInList(self, row):
		return row.find("div", class_ = "listing-logo")

	def setProfileLink(self, row):
		h2 = row.find('h2', class_ = "listing-name")
		self.profile_url = self.base_url + h2.find('a')['href']



	#> TESTING NEW SIMPLIFIED VERSION
	def extractPage(self):
		soup = self.getSoup()
		if 'Det finnes ingen side med denne adressen ' in soup.text:
			self.reached_limit = True
			# print('Det finnes ingen side med denne adressen')
		'''
		gets list profiles from industry (page x)
		'''
		false_counter, company_row_count = 0, 0 #reset counter
		for row in soup.find_all("div", class_ = "box listing listing--business"):
			self.setProfileLink(row)
			company_row_count += 1
			if row.find("div", class_ = "listing-logo") or self.checkForPayedEnrtryInProfile(self.getSoup(self.profile_url)): # checks if any rows in profile-list-page has contains a company-logo (payed entry)
				print(self.profile_url)
				
				# #> substityte test
				# self.findMatchForAddressInInputTable()
				# break
				# self.findMatchForProfileNameInBrreg()
				self.getAndInsertCompanyInfoToDb()
				# print(f"is_customer = True --> {self.profile_url}")
			else:
				false_counter += 1
				# print(f"is_customer = False --> {self.profile_url}")
				if false_counter == company_row_count: #break if whole profile-list-page is free-entry  
					self.reached_limit = True
					# print("LIMIT REACHED")
					break


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


	#>TEST		
	def fetchAdress(self):
		profile_soup = self.getSoup(self.profile_url)
		details__body = profile_soup.find('div', class_ = 'details__body')
		search_loc = details__body.find('a', class_="link-icon-text").text.split(',')[0].split('/')[0]
		search_loc = " ".join(search_loc.split())
		try:
			search_post = details__body.find_all('p', class_="listing-address")[1].text.split(',')[0].replace('        ', '')
			search_post = " ".join(search_post.split())
		except IndexError:
			search_post = None
		return search_loc, search_post 	

	# >TEST
	def findMatchForAddressInInputTable(self):
		search_loc, search_post = self.fetchAdress()
		try:
			company_name, org_num = Search().match_adress_in_input_table(search_loc, search_post)
			if org_num:
				print("match found")
				Insert().to1881(org_num, company_name)
			else:
				self.findMatchForProfileNameInBrreg()
		except:
			print(search_loc, search_post)

	#> TEST: substitute for "getAndInsertCompanyInfoToDb()"
	def findMatchForProfileNameInBrreg(self): #, profile_name:str):
		'''
		Will take company name from the profile-page and try and find a 
		match for it in brregTable instead of scraping Rengskapstall.no.
		Which could save almost 1/3 of the runtime.
		'''

		
		'''Attempt 1: try filter.contains (easy but needs to be exact)'''
		profile_name = self.profile_url.split("/")[-2].split("_")[0].replace("-", " ")
		# search_result = Search().match_company_name_in_input_table(profile_name)
		
		print(profile_name)
		

	def getAndInsertCompanyInfoToDb(self):
		''' gets company_name & org_num from regnskapstall.no, since we already getting org_num from there. 
			++ then we get the full legal name of the company, sometimes 1881 name is wrong, e.g."1 default"
		'''
		regnskapstall_soup = self.requestRegnskapstall()
		try:
			org_num = int(regnskapstall_soup.find("th", string = " Org nr ").find_next().text.replace('\xa0', ''))
			company_name =  regnskapstall_soup.find("th", string = " Juridisk selskapsname ").find_next().text
			tlf = regnskapstall_soup.find("th", string = "Telefon").find_next().text
			# class="call-button"
		except AttributeError: #! This might not be needed anymore 
			print(f"""
			ERROR:

			{self.profile_url_snippet}
			{self.profile_url}
			
			""")
			org_num = 404
			company_name = "Error"
		Insert().to1881(org_num, company_name, tlf)

	def requestRegnskapstall(self):
		# self.profile_url_snippet = (self.profile_url.split("/")[-2]).replace("_", "-")
		self.profile_url_snippet = self.profile_url.split("/")[-2].replace("_", "-")
		regnskapstall_url = f"https://www.regnskapstall.no/informasjon-om-{self.profile_url_snippet}"
		response = requests.request("GET", regnskapstall_url, headers = self.header)
		return BeautifulSoup(response.content, "html.parser")

	def worker(self, industry):
		self.industry = industry
		self.url = f"{self.base_url}/{self.industry}"
		self.extractPage()
		page_num = 1
		while self.reached_limit == False:
			page_num += 1
			self.url = f"{self.base_url}/{self.industry}?page={page_num}"
			self.extractPage()
			if self.reached_limit:
				break

	def runExtraction(self) -> None:
		Reset()._1881()
		industries = getAll1881Industries()[:3] #TEMP deactivated while testing
		# industries = ['akustisk-utstyr']
		# pprint(industries)
		with Pool() as pool:
			list(tqdm(pool.imap_unordered(self.worker, industries), total = len(industries)))


'''	___ Time_Estimates ___
NOTE: "enh" betyr "industry" 
		30_enh_tid:		19.920s	( base + 30 enh )
		10_enh_tid:		33.640s	( base + 10 enh )
		526_enh_tid:   224.250s	(0.39195230998509687034277198211624 % of total enh)	

(sek)	est.tot.tid:   572.136s	(526_enh_tid / 0.39195230998509687034277198211624)
(min)	est.tot.tid:     9.536m	(est.tot.tid / 60)
		
		diff = 			 0.570s	( diff = (base + 1 enh) - (base + 3 enh) = 2 enh )
		est.enh.tid: 	 0.285s	( diff / 2 enh )
		est.base.tid:	10.015s	( 1_enh_tid - est.enh.tid )
		tot. enh: 	  1342 stk	( len(industries) ) 
(sek)	est.tot.tid:  4708.772s	( tot.enh / est.enh.tid )
(min) 	est.tot.tid: 	78.480m	( est.tot.tid / 60 )
(hr)	est.tot.tid:	 1.308h	( est.tot.tid / 60 / 60 )
'''

'''
virker som regnskapstall.no er eid av google, så er mulig jeg kan skippe mellommannen og finne ut om en profil har betalt oppføring direkte derfra.
da slipper jeg å gjøre 3 reguests for hver eneste bedrift. 
'''

'''
___ Current_issues ___
	[1] the url extractor in extractPage() extractes the wrong link for some rows, resulting in:
		'https://www.1881.nohttp://advokateneilarvik.no/'
	assumption: 
		if the row contains a website link, then it will grab that one instead

	[2] Annoying bug: 
		Extractor spawns multiple messages; 		No module named 'aioredis'
													No module named 'httpx'
		possible soplution: https://stackoverflow.com/questions/72978364/modulenotfounderror-no-module-named-httpx		

	[3] company_name error 

	[4]
	1881.no/akupunktur/akupunktur-troendelag/akupunktur-roervik/roervik-akupunktur_100528204S2/
	/akupunktur/akupunktur-troendelag/akupunktur-roervik/roervik-akupunktur_100528204S2/
'''
	#! DO NOT REMOVE BEFORE EXTENSIVLY TESTING IF OUTPUT MATCHES WITH NEW VERSION
	#! OLD VERSION OF WHATS BEING TESTED 
	# def extractPage(self):
	# 	soup = self.getSoup()
	# 	if 'Det finnes ingen side med denne adressen ' in soup.text:
	# 		self.reached_limit = True
	# 	rows = soup.find_all("div", class_ = "box listing listing--business")
	# 	# if not rows:
	# 	# 	self.reached_limit = True
		
	# 	'''
	# 	gets list profiles from industry (page x)
	# 	'''
	# 	link_list = []
	# 	for row in rows:
	# 		self.setProfileLink(row)
	# 		if row.find("div", class_ = "listing-logo"): # checks if any rows in profile-list-page has contains a company-logo (payed entry)
	# 			# print(f"TRUE (found listing logo): {self.profile_url}")
	# 			self.getAndInsertCompanyInfoToDb()
	# 		else:
	# 			link_list.append(self.profile_url) 	# else it adds to link_list for further digging
	# 	#> testing the removal of "try" 
	# 			# try:
	# 			# 	link_list.append(self.profile_url)
	# 			# except:
	# 			# 	pass
	# 	'''
	# 	gets profiles from link_list (page x)
	# 	'''
	# 	false_counter, company_row_count = 0, 0 #reset counter
	# 	for url in link_list:
	# 		company_row_count += 1
	# 		self.profile_url = url
	# 		profile = self.getSoup(url)
	# 		if self.checkForPayedEnrtryInProfile(profile):
	# 			self.getAndInsertCompanyInfoToDb()
	# 		else:
	# 			false_counter += 1
	# 			if false_counter == company_row_count: #break if whole profile-list-page is free-entry  
	# 				self.reached_limit = True
	# 				break
	
	
#! OLD version
	# def getSoup(self, url:str = None) -> BeautifulSoup:
	# 	if url:
	# 		''' gets profile '''
	# 		try:
	# 			response = requests.request("GET", url, headers = self.header)
	# 		except requests.exceptions.TooManyRedirects as e:
	# 			print(f"""
	# 			ERROR TooManyRedirects:
	# 			{url}

	# 			{e}

	# 			""")
	# 			pass
	# 	else:
	# 		''' gets profile list '''
	# 		response = requests.request("GET", self.url, headers = self.header)
	# 	return BeautifulSoup(response.content, "html.parser")