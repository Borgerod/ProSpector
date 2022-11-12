from SQL.insert import Insert
import SQL.db as db
from SQL.query import getAll1881Industries
from SQL.reset import Reset
import requests
import pandas as pd
from tqdm import tqdm
from bs4 import BeautifulSoup
from multiprocessing import Pool
from pprint import pprint
import re 

''' 
____ Track_record ____
	tot. time:  xx.xxxs 
'''
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

# TODO: NOTE: burde egentlig inkludere gateaddresse

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
		self.header = {
				"cookie": "__uzma=e69d520f-a8db-46ec-b5d1-7d2e26930e28; __uzmc=163051371814; __uzmb=1668010547; __uzmd=1668010570;captchaResponse=1; Expires=null; Path=/; Domain=www.1881.no",
				"authority": "cdn.pbstck.com",
				"accept": "*/*",
				"accept-language": "en-US,en;q=0.9",
				"cache-control": "no-cache",
				"origin": "https://www.1881.no",
				"pragma": "no-cache",
				"referer": "https://www.1881.no/sitemap/bransjer-a/",
				"sec-ch-ua": "^\^Google",
				"sec-ch-ua-mobile": "?0",
				"sec-ch-ua-platform": "^\^Windows^^",
				"sec-fetch-dest": "empty",
				"sec-fetch-mode": "cors",
				"sec-fetch-site": "cross-site",
				"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
			}
	#> TEST version
	def getSoup(self, url:str = None) -> BeautifulSoup:
		response = requests.request("GET", 'https://www.1881.no/Error/PageNotFound', headers = self.header)	#Just for returning a empty/useless soup 
		# try:

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
		# except UnboundLocalError as e:
		# 	print(e)
		# 	response = requests.request("GET", 'https://www.1881.no/Error/PageNotFound', headers = self.header)	#Just for returning a empty/useless soup 
		return BeautifulSoup(response.content, "html.parser")

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

	def checkForPayedEnrtryInProfile(self, profile:BeautifulSoup) -> BeautifulSoup:
		return 'Søkeord' in profile.text 

	def checkForPayedEnrtryInList(self, row):
		return row.find("div", class_="listing-logo")

	def setProfileLink(self, row):
		h2 = row.find('h2', class_="listing-name")
		self.profile_url = self.base_url + h2.find('a')['href']

	def extractPage(self):
		soup = self.getSoup()
		rows = soup.find_all("div", class_ = "box listing listing--business")
		if not rows:
			self.reached_limit = True
		
		'''
		gets list profiles from industry (page x)
		'''
		link_list = []
		for row in rows:
			self.setProfileLink(row)
			if row.find("div", class_="listing-logo"): # checks if any rows in profile-list-page has contains a company-logo (payed entry)
				# print(f"TRUE (found listing logo): {self.profile_url}")
				self.getAndInsertCompanyInfoToDb()
			else:
				link_list.append(self.profile_url) 	# else it adds to link_list for further digging
		#> testing the removal of "try" 
				# try:
				# 	link_list.append(self.profile_url)
				# except:
				# 	pass
		'''
		gets profiles from link_list (page x)
		'''
		false_counter, company_row_count = 0, 0 #reset counter
		for url in link_list:
			company_row_count += 1
			self.profile_url = url
			profile = self.getSoup(url)
			if self.checkForPayedEnrtryInProfile(profile):
				# print(f"TRUE (found Søkeord) : {self.profile_url}")
				self.getAndInsertCompanyInfoToDb()
			else:
				# print("FALSE")	
				false_counter += 1
				if false_counter == company_row_count: #break if whole profile-list-page is free-entry  
					# print("LIMIT REACHED")	
					self.reached_limit = True
					break
	
	def getAndInsertCompanyInfoToDb(self):
		''' gets company_name & org_num from regnskapstall.no, since we already getting org_num from there. 
			++ then we get the full legal name of the company, sometimes 1881 name is wrong, e.g."1 default"
		'''
		regnskapstall_soup = self.requestRegnskapstall()
		try:
			org_num = int(regnskapstall_soup.find("th", string = " Org nr ").find_next().text.replace('\xa0', ''))
			company_name =  regnskapstall_soup.find("th", string = " Juridisk selskapsnavn ").find_next().text#.replace('\xa0', '')
		except AttributeError: #! This might not be needed anymore 
			print(f"""
			ERROR:

			{self.profile_url_snippet}
			{self.profile_url}
			
			""")
			org_num = 404
			company_name = "Error"
		Insert().to1881(org_num, company_name)

	def requestRegnskapstall(self):
		self.profile_url_snippet = (self.profile_url.split("/")[-2]).replace("_", "-")
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
		industries = getAll1881Industries()#[815:] #TEMP deactivated while testing
		# print(len(industries)) # ''' ['adopsjon', 'adressering', 'advokat'] '''
		# print(industries)
		# industries = ['alternativ-behandling-biopat']
		with Pool() as pool:
			list(tqdm(pool.imap_unordered(self.worker, industries), total = len(industries)))

