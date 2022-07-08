import pandas as pd 



pd.set_option('display.max_colwidth', 10)		# Columns  (width)
pd.set_option('display.max_columns', None)		# column display border
pd.set_option('display.width', 800)	
df = pd.read_csv('../_output_data/gulesider_data.csv')
# df = df.dropna( subset='')
df = df.drop_duplicates()
print(df)




# def pullRequest(url, source):
# 	'''
# 	1. makes a pull request from gulesider.no.
# 	2. then checks the connection.
# 	3. then returns a soup.
# 	'''
# 	# print(url)
# 	try:
# 		r = requests.get(url, timeout=10)
# 		soup = BeautifulSoup(r.content, "html.parser")
# 		r.raise_for_status()

# 	except (requests.exceptions.RequestException, ValueError) as e:
# 		''' 
# 		if exception occurred:
# 			- prints error & related url
# 			- sends the faulty url (++) to errorSave() from error_save.py for later use
# 			- returns an empty soup
# 		'''	
# 		print("="*91)
# 		print("|											  |")
# 		print("|				WARNING: ERROR CAUGHT! 				  |")
# 		print("|											  |")
# 		print("="*91)
# 		print(f'					{print(e)}')
# 		# errorSave(url, e, source) #Currently not in nuse (not yet finished)
# 		# soup = ""
# 		pass 
# 	return soup

# import time; start = time.perf_counter() #Since it also takes time to Import libs, I allways start the timer asap. 
# import requests
# from bs4 import BeautifulSoup
# from fake_headers import Headers
# import pandas as pd
# import pprint
# import os.path
# from os import path
# from tqdm import tqdm
# import concurrent.futures
# import os.path


# # class="yextLink"

# import re


# def phoneNumber():
# 	url = 'https://www.gulesider.no/lang+j%C3%B8rn+g+smykkeverkstedet+oslo/84674394/bedrift?page=1&query=oslo%20mynthandel%20as'
# 	source='gulesider'
# 	soup = pullRequest(url, source)

# 	# class="phoneNumber"
# 	# phone_number = soup.find('div', { 'class': "phoneList"})
# 	phone_number = [item.text for item in soup.find('div', { 'class': "phoneList"})][0]
# 	print(phone_number)
# 	# print(phone_number.prettify())

# 	# hrefs = [item['href'] for item in soup.findAll('a', { 'class': "yextLink", 'href': True })] 
# 	# phone_number = ""
# 	# for href in hrefs:
# 	# 	if "phoneNumber" in href:
# 	# 		phone_number = re.split('phoneNumber=|&street',href)[1]
# phoneNumber()

# 	# https://nettsjekk.gulesider.no/?utm_source=gulesider&utm_medium=corefront&utm_campaign=netcheck&companyName=Lang%20J%C3%B8rn%20G%20Smykkeverkstedet&phoneNumber=22 26 18 61&street=B%C3%B8lerlia%20101&postCode=0689&postArea=Oslo

# 		# print(i.prettify())
# 	# print(phone_number)
# 	# print(phone_number.prettify())
