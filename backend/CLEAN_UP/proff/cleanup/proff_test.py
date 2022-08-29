import time
start = time.perf_counter()
import requests
from bs4 import BeautifulSoup
from fake_headers import Headers
import pandas as pd
import pprint
import re 
from industry_list import industries
import json
import concurrent.futures
BASE_URL = 'https://www.proff.no'




# progressbar test
from tqdm import tqdm


# pd.set_option('display.max_colwidth', None)
# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', None)



'''
TODO:

	[ ] lag base amount funksjon 
	[ ] integrer getLenResults i scraper() firstPage() og nextPages()
	[ ] lag postgres database 
	[ ] Bytt ut csv løsning med postgres 
	[ ] Lag en progressbar 
'''

# def getBaseAmount():
# 	base_amount = pd.read_csv('base_amount.csv')
# 	return int(base_amount.columns[0])


# def updateBaseAmount(base_amount):
# 	base_amount = pd.read_csv('base_amount.csv')


'''
first run
'''



# def getLenResults(url):
# 	soup = BeautifulSoup(requests.get(url).content, "html.parser")
# 	len_results = [element.text for element in soup.findAll('span','ui-wide') if "treff" in element.text]
# 	len_results = int(len_results[0].replace("- ", "").replace(" treff", ""))  
# 	return len_results
# 	# num_of_pages = round(len_results/25)
# 	# if num_of_pages == 0:
# 	# 	num_of_pages = 1
# 	# return num_of_pages


def pullRequest(url):
	try:
		r = requests.get(url, timeout=10)
		soup = BeautifulSoup(r.content, "html.parser")
	   # soup = BeautifulSoup(requests.get(url,
						 # timeout=10), "html.parser", features="lxml")
						 # headers={'Cache-Control': 'nocache', 'Pragma': 'nocache'}))
						 # headers = getHDR()))

		r.raise_for_status()#, headers={'Cache-Control': 'nocache', 'Pragma': 'nocache'}).raise_for_status()
	except (requests.exceptions.RequestException, ValueError) as e:
		# print('Error caught!') 
		# print(e)
		print("="*91)
		print("|											  |")
		print("|				WARNING: ERROR CAUGHT! 				  |")
		print("|											  |")
		print("="*91)
		print(f'					{print(e)}')
	return soup


def getPage(url):
	df = pd.DataFrame(		 index = [ 'bedrift',
										'avdeling',
										'telefon',
										'bransje',
										'org num', ] ).T
	soup = pullRequest(url)
	# content = soup.findAll('div', {'class':"search-container clear  low-priority"})
	# content = soup.findAll('div', {"class":"search-block-info"})
	# content = soup.findAll('div',{"class":"search-block-wrap"})
	content = soup.findAll('div', {"class":"search-block"})
	content = [i for i in content]

	with concurrent.futures.ThreadPoolExecutor() as executor:
		results = executor.map(pageWorker, content) 
		for data_list in results:
			row = pd.DataFrame(data_list, index = [ 'bedrift',
													'avdeling',
													'telefon',
													'bransje',
													'org num', ] ).T
			df = pd.concat([df, row], axis = 0)
	next_page_url = nextPageUrl(soup)
	df = df.reset_index(drop = True)
	# print(df_firstPage)
	return df, next_page_url

def pageWorker(cont):
	# cont = content
	data_list = []
	# ___ NAME ___________
	name = [element.text for element in cont.find('a','addax addax-cs_hl_hit_company_name_click')]
	data_list.append(name)

	# ___ BRANCH ___________
	try:
		company_data = [item['data-company'] for item in cont.find_all('a', attrs = {'data-company' : True})]
		branch = [json.loads(company_data[0])['location']['county']]
	except:
		branch = ""
	data_list.append(branch)
	
	# ___ TELEPHONE ___________
	try: 
		tlf = [element.text for element in cont.find('a','addax addax-cs_hl_hit_phone_click')]
		data_list.append(tlf)
	except TypeError:
		tlf = ""
		data_list.append(tlf)
	
	# ___ INDUSTRY ___________
	industry = [[element.text for element in cont.find('a','addax addax-cs_hl_hit_industry_click')]]
	data_list.append(industry)
	
	# ___ ORG_NUM ___________
	org_num = [item['data-id'] for item in cont.find_all('div', attrs = {'data-id' : True})]
	data_list.append(org_num)

	return data_list


def nextPageUrl(soup):
	try:
		a = soup.find('a',{'class': 'arrow ssproff-right'})
		next_page_token = a['href']
		next_page_url = BASE_URL + next_page_token
	except TypeError:
		next_page_url = ""
	return next_page_url





'''
Next runs
'''

'''
___ Idé _____________________

	1. Regn ut total_amount på forhånd.
	2. Sett v som en standard mengde med threads.
	3. Integrer getLenResults() inn i getNextPages() og getFirstPage() => num_of_pages
	4. I scraper() regner du ut en ny total_amount [vil trolig vokse fra start til finish]
	5. I scraper() legg til funksjonen:
		if new_total_amount > old_total_amount:
			spawn additional threads
	6. oppdatere old_total_amount = new_total_amount så lagre det nye grunntallet. 

	Note: 
		må splitte opp threadingen i to deler. 
		del 1 threader main per ind in industries. 
		del 2 må regne ut total_amount per bransje, så threade hver side. 

	Altså: 
		Nå vil den ikke sjekke tallet på forhånd som sparer meg 1 min. 
		Den vil spawne X antall threads til å begynne med, fra et grunntall,
		så etterhvert som den jobber vil total_amount bli oppdatert og den 
		vil spawne nye threads etterhvert som proff får flere virksomheter.
		Til slutt vil den nye_total_amount bli lagret over old_total_amount i en egen fil (eller databasen) 

'''

'''
___ NY Idé _____________________
	
	Alternativ til tidligere løsninger iht threading.
	grunnet mangel på sidetall kan man ikke threade sider pga man må innom side 1 for å hente linken til side 2. 
	1. 

	altså:
		Alle sidene består av en liste, og det kan vi iterate igjennom. 
		Så da kan vi derimot threade hvert liste item; at hver worker har sin designerte arbeidsplass på listen:
			worker 1:	skal bare hente list[0]
			worker 2:	skal bare hente list[1]
			...
			worker n-1:	skal bare hente list[n]
			worker n:	henter neste link til neste side (trenger strengt tatt ikke å være en worker)
		Så istedenfor å ha én worker for X antall sider, har vi 28 workers for hver side. (for hver bransje)

'''


def scarper(url, ind):

	'''
	first run:
	'''
	# search_results = getLenResults(url)
	# print(f' len content: {num_of_pages}')
	# print()
	# df_list = []
	df_firstPage, next_page_url = getPage(url)
	# url = next_page_url
	# print(df_firstPage)
	# df_list.append(df_firstPage)
	# return df_firstPage
	next_url = next_page_url
	# index = 0


	'''
	Threading breakdown: 
		function -> getNextPages()
		param -> next_url, list_pos   = len_items
		threadPool -> len_items 
	'''

	# with tqdm(total=range(search_results)) as pbar:

	while next_url != "":
	# if next_url != "":
		df_nextPage, next_page_url = getPage(next_url)
		next_url = next_page_url
		df_firstPage = pd.concat([df_firstPage, df_nextPage], axis = 0)
		# index += 1
		# pbar.update(df_nextPage.index)
	# print(f'No.{index}:	spawned {num_of_pages} threads for "{ind}"')
	df_old = pd.read_csv('proff_data.csv')
	df_new = pd.concat([df_old, df_firstPage], axis = 0)
	df_final = df_new.drop_duplicates(subset = ['org num'], keep = 'first')
	# df_final = df_new.drop_duplicates(subset = ['bedrift','avdeling','telefon','org num'], keep = 'first')
	df_final = df_final.reset_index(drop = True)
	df_final.to_csv('proff_data.csv', index = False)
	print(f'{ind} was succsessfullly saved to "proff_data.csv"')
	# print(df_final)
	return df_final


print("="*91)
print("|											  |")
print("|				STARTING PROFF.NO SCRAPER 				  |")
print("|											  |")
print("="*91)
print(f" Amount of industries scraping: {len(industries)}")
print()
print()




def genUrls(industries):
	urls = []
	for ind in industries:
		url = f'https://www.proff.no/bransjes%C3%B8k?q={ind}'
		urls.append(url)
	# return url
	return urls

# MAIN TEST (MAP)
industries = ['Adresseringsleverandører']#, 'Advokater og juridiske tjenester', 'Agenturhandel - annet','Akvakultur']
industries = ['Advokater og juridiske tjenester']
# industries = ['']
def firstThreader():
	index = 0
	# result_list = []
	urls = genUrls(industries)
	# print(len(urls))
	# print(industries)
	
	# df = pd.DataFrame(index = [ 'bedrift',
	# 							'avdeling',
	# 							'telefon',
	# 							'bransje',
	# 							'org num', ] ).T
	print('	loading, please wait..')
	print()
	# with concurrent.futures.ThreadPoolExecutor() as executor:
	# 	results = executor.map(scarper, urls)
	# 	for result in results:

			# for _ in tqdm(result.index):
			# 	index += 1
				# time.sleep(.00001)
				# print()



	# with ThreadPoolExecutor(max_workers=(len(urls))) as ex:
	# 	futures = [ex.submit(scarper, url) for url in urls]
	# 	for future in as_completed(futures):
	# 		df = future.result()

	# with tqdm(total=len(urls)) as pbar:
	with concurrent.futures.ThreadPoolExecutor() as executor:
		results = executor.map(scarper, urls, industries)
		# for result in results:
		# 	print()
			# print(result)
				# pbar.update(1)

	df = pd.read_csv('proff_data.csv')
	print(f"|				   Finished in {round(time.perf_counter() - start, 2)} second(s)				  |")
	print("Displaying results:")
	print()
	print(df)



firstThreader()



# MAIN
# with concurrent.futures.ThreadPoolExecutor() as executor:
# 	results = [executor.submit(scarper, ind) for ind in industries]
# 	for f in concurrent.futures.as_completed(results):
# 		# print()
# 		# notification()
# 		print(f.result())

# 	print(f"|				   Finished in {round(time.perf_counter() - start, 2)} second(s)				  |")


