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
import numpy as np



# progressbar test
from tqdm import tqdm


# pd.set_option('display.max_colwidth', None)
# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', None)

def getLinks():
	links = pd.read_csv('links.csv')
	return links.to_numpy()

def pullRequest(url):
	try:
		r = requests.get(url, timeout=10)
		soup = BeautifulSoup(r.content, "html.parser")
		r.raise_for_status()
	except (requests.exceptions.RequestException, ValueError) as e:
		print("="*91)
		print("|											  |")
		print("|				WARNING: ERROR CAUGHT! 				  |")
		print("|											  |")
		print("="*91)
		print(f'					{print(e)}')
		soup = ""
	return soup


def getPage(url):
	df = pd.DataFrame(		 index = [ 'bedrift',
										'avdeling',
										'telefon',
										'bransje',
										'org num', ] ).T
	soup = pullRequest(url)
	try:
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
	except AttributeError:
		pass
	df = df.reset_index(drop = True)
	return df


def pageWorker(cont):
	data_list = []
	# ___ NAME ___________
	try:
		name = [element.text for element in cont.find('a','addax addax-cs_hl_hit_company_name_click')]
		data_list.append(name)
	except TypeError:
		name = ""
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
	try:
		industry = [[element.text for element in cont.find('a','addax addax-cs_hl_hit_industry_click')]]
		data_list.append(industry)
	except TypeError:
		industry = ""
		data_list.append(industry)	
	# ___ ORG_NUM ___________
	org_num = [item['data-id'] for item in cont.find_all('div', attrs = {'data-id' : True})]
	data_list.append(org_num)

	return data_list






def scarper(url):
	# data_list = []
	df_new = getPage(url[0])
	# data_list.append(new_list)

	# print(data_list)
	df_old = pd.DataFrame( index = [ 'bedrift',
											'avdeling',
											'telefon',
											'bransje',
											'org num', ] ).T
	# df_old = pd.read_csv('proff_data.csv', on_bad_lines = 'skip', delim_whitespace=True)
	# print(df_old)

	df_final = pd.concat([df_old, df_new], axis = 0)
	return df_final
	# print(df_final)
	# # df_final = df_final.drop_duplicates(subset = ['org num'], keep = 'first')
	# # df_final = df_final.reset_index(drop = True)
	# # df_final.to_csv('proff_data.csv', index = False)
	# # return df_final
	# print('='*100)
	# print()
	# print()

print("=" * 91)
print("|											  |")
print("|				STARTING PROFF.NO SCRAPER 				  |")
print("|											  |")
print("=" * 91)
print(f" Amount of industries scraping: {len(industries)}")
print()
print()


def firstThreader():
	urls = getLinks()
	index = 0

	print('	loading, please wait..')
	print()
	df_final = pd.DataFrame( index = [ 	'bedrift',
										'avdeling',
										'telefon',
										'bransje',
										'org num', ] ).T
	with tqdm(total = len(urls)) as pbar:
			with concurrent.futures.ThreadPoolExecutor() as executor:
				results = executor.map(scarper, urls)
				for result in results:
					pbar.update(1)
					df_final = pd.concat([df_final, result], axis = 0)
	df_final.to_csv('proff_data.csv', index = False)
	print(f"|				   Finished in {round(time.perf_counter() - start, 2)} second(s)				  |")
	print("Displaying results:")
	print()
	print(df_final)
firstThreader()




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
