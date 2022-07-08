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

# progressbar test
from tqdm import tqdm


BASE_URL = 'https://www.proff.no'
print("="*91)
print("|											  |")
print("|				STARTING PROFF.NO SCRAPER 				  |")
print("|											  |")
print("="*91)
print(f" Amount of industries scraping: {len(industries)}")
print()
print()
	




def nextPageUrl(soup):
	try:
		a = soup.find('a',{'class': 'arrow ssproff-right'})
		next_page_token = a['href']
		next_page_url = BASE_URL + next_page_token
	except TypeError:
		next_page_url = ""
	return next_page_url

def getPage(url):
	soup = pullRequest(url)
	next_page_url = nextPageUrl(soup)
	return next_page_url

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
		soup=""
	return soup



# def scarper(url):
# 	next_page_url = getPage(url)
# 	next_url = next_page_url
# 	url_list = [url, next_url]
# 	while next_url != "":
# 		next_page_url = getPage(next_url)
# 		next_url = next_page_url
# 		url_list.append(next_page_url)
# 	df = pd.DataFrame(url_list)
# 	return df



def scarper(url):
	next_page_url = getPage(url)
	next_url = next_page_url
	url_list = [url, next_url]
	while True:
	        next_page_url = getPage(next_url)
	        next_url = next_page_url
	        url_list.append(next_page_url)
	        if next_url == '':
	            break


	return url_list

def genUrls(industries):
	urls = []
	for ind in industries:
		url = f'https://www.proff.no/bransjes%C3%B8k?q={ind}'
		urls.append(url)
	return urls

# MAIN TEST (MAP)
# industries = ['Adresseringsleverandører', 'Advokater og juridiske tjenester', 'Agenturhandel - annet','Akvakultur']
# industries = ['Advokater og juridiske tjenester']
def firstThreader():
	df_main = pd.DataFrame()
	urls = genUrls(industries)
	print('	loading, please wait..')
	print()
	index=0
	with concurrent.futures.ThreadPoolExecutor() as executor:
		results = executor.map(scarper, urls)
		for result in results:
			index+=1
			print(f'progress:{index}')
			df = pd.DataFrame(result)
			df_main = pd.concat([df_main, df], axis = 0)
	print(df_main)
	df_main.to_csv('links.csv', index = False)
	print(f"|				   Finished in {round(time.perf_counter() - start, 2)} second(s)				  |")
firstThreader()



# MAIN
# with concurrent.futures.ThreadPoolExecutor() as executor:
# 	results = [executor.submit(scarper, ind) for ind in industries]
# 	for f in concurrent.futures.as_completed(results):
# 		# print()
# 		# notification()
# 		print(f.result())

# 	print(f"|				   Finished in {round(time.perf_counter() - start, 2)} second(s)				  |")


