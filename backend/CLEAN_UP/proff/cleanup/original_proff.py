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
BASE_URL = 'https://www.proff.no'
# industries = ['Adresseringsleverandører']
import threading 


pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)



'''
first run
'''
def firstPage(ind):
	url = f'https://www.proff.no/bransjes%C3%B8k?q={ind}'
	soup = BeautifulSoup(requests.get(url).content, "html.parser")
	section = soup.find("div", {"class": "search-container-wrap"})
	section_content = [i for i in section]
	df = pd.DataFrame( index = ['bedrift',
								'avdeling',
								'telefon',
								'bransje',
								'org num', ] ).T
	for i, cont in enumerate(section_content[1::2]):
		data_list = []
		name = [element.text for element in cont.findAll('a','addax addax-cs_hl_hit_company_name_click')]
		data_list.append(name)

		try:
			company_data = [item['data-company'] for item in cont.find_all('a', attrs = {'data-company' : True})]
			branch = [json.loads(company_data[0])['location']['county']]
		except:
			branch = ""
		data_list.append(branch)

		tlf = [element.text for element in cont.findAll('a','addax addax-cs_hl_hit_phone_click')]
		data_list.append(tlf)

		industry = [[element.text for element in cont.findAll('a','addax addax-cs_hl_hit_industry_click')]]
		data_list.append(industry)

		org_num = [item['data-id'] for item in cont.find_all('div', attrs = {'data-id' : True})]
		data_list.append(org_num)

		row = pd.DataFrame(data_list, index = [ 'bedrift',
												'avdeling',
												'telefon',
												'bransje',
												'org num', ] ).T
		df = pd.concat([df, row], axis = 0)
	df_firstPage = df.reset_index(drop = True)
	next_page_url = nextPageUrl(soup)
	return df_firstPage, next_page_url

def nextPageUrl(soup):
	try:
		a = soup.find('a',{'class': 'arrow ssproff-right'})
		next_page_token = a['href']
		next_page_url = BASE_URL + next_page_token
	except TypeError:
		next_page_url = ""
	return next_page_url


def getNextPages(next_page_url):
	
	soup = BeautifulSoup(requests.get(next_page_url).content, "html.parser")
	section = soup.find("div", {"class": "search-container-wrap"})
	section_content = [i for i in section]
	df = pd.DataFrame( index = ['bedrift',
								'avdeling',
								'telefon',
								'bransje',
								'org num', ] ).T
	for i, cont in enumerate(section_content[1::2]):
		data_list = []
		name = [element.text for element in cont.findAll('a','addax addax-cs_hl_hit_company_name_click')]
		data_list.append(name)

		try:
			company_data = [item['data-company'] for item in cont.find_all('a', attrs = {'data-company' : True})]
			branch = [json.loads(company_data[0])['location']['county']]
		except:
			branch = ""
		data_list.append(branch)

		tlf = [element.text for element in cont.findAll('a','addax addax-cs_hl_hit_phone_click')]
		data_list.append(tlf)

		industry = [[element.text for element in cont.findAll('a','addax addax-cs_hl_hit_industry_click')]]
		data_list.append(industry)

		org_num = [item['data-id'] for item in cont.find_all('div', attrs = {'data-id' : True})]
		data_list.append(org_num)

		row = pd.DataFrame(data_list, index = [ 'bedrift',
												'avdeling',
												'telefon',
												'bransje',
												'org num', ] ).T
		df = pd.concat([df, row], axis = 0)
	next_page_url = nextPageUrl(soup)
	df_firstPage = df.reset_index(drop = True)
		
	return df_firstPage, next_page_url



# def main():
# 	industries = ['Agenturhandel - annet']
# 	for ind in industries:
# 		df_firstPage, next_page_url = firstPage(ind)
# 		next_url = next_page_url
# 		index = 0
# 		while next_url != "":
# 			df_nextPage, next_page_url = getNextPages(next_url)
# 			next_url = next_page_url
# 			df_firstPage = pd.concat([df_firstPage, df_nextPage], axis = 0)
# 			index += 1
# 			print(index)
# 	print(df_firstPage)
# 	df_old = pd.read_csv('proff_data.csv', index = False)
# 	df_new = pd.concat([df_old, df_firstPage], axis = 0)
# 	df_new.drop_duplicates()
# 	print(df_new)
# 	df_new.to_csv('proff_data.csv', index = False)
# main()

# def main():
# 	# industries = ['Agenturhandel - annet']
# 	# for ind in industries:
# 	# print("hei")
# 	# print(industries)
# 	df_firstPage, next_page_url = firstPage(ind)
# 	next_url = next_page_url
# 	index = 0
# 	while next_url != "":
# 		df_nextPage, next_page_url = getNextPages(next_url)
# 		next_url = next_page_url
# 		df_firstPage = pd.concat([df_firstPage, df_nextPage], axis = 0)
# 		index += 1
# 		print(index)
# 	print(df_firstPage)
# 	df_old = pd.read_csv('proff_data.csv', index = False)
# 	df_new = pd.concat([df_old, df_firstPage], axis = 0)
# 	df_new.drop_duplicates()
# 	print(df_new)
# 	df_new.to_csv('proff_data.csv', index = False)

# from multiprocessing.dummy import Pool as ThreadPool


def scarper(ind):
	df_firstPage, next_page_url = firstPage(ind)
	next_url = next_page_url
	index = 0
	while next_url != "":
		df_nextPage, next_page_url = getNextPages(next_url)
		next_url = next_page_url
		df_firstPage = pd.concat([df_firstPage, df_nextPage], axis = 0)
		index += 1
	df_old = pd.read_csv('proff_data.csv', index = False)
	df_new = pd.concat([df_old, df_firstPage], axis = 0)
	df_new.drop_duplicates()
	print(df_new)
	df_new.to_csv('proff_data.csv', index = False)
import concurrent.futures



with concurrent.futures.ThreadPoolExecutor() as executor:
	results = [executor.submit(scarper, ind) for ind in industries]
	for f in concurrent.futures.as_completed(results):
		print(f.result())
	print(f"|				   Finished in {round(time.perf_counter() - start, 2)} second(s)				  |")













# # next_page = class="list-paging paging clear"
# next_page_token = []
# next_page = soup.find('div', {'class':"list-paging paging clear"})
# a = next_page.findAll('a', href=True)
# for href in a:
#     next_page_token.append(href['href'])	
# print(next_page_token)
# # for rows in next_page:
# # 	a = rows.findAll('a', href=True)['href']
# # 	print(a)
# # token = next_page.find('href')
# # print(token.prettify())



# for table in DOC_TABLE:
# 	for row in table.find_all('tr')[0:2]:


# links = []

# for link in soup.findAll('a', attrs={'href': re.compile("bransje/")}):
#     links.append(link.get('href'))

# print(links)


