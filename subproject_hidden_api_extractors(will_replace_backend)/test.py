import difflib
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re 
import json


import requests
import pandas as pd
import sqlalchemy
from tqdm import tqdm
from bs4 import BeautifulSoup
from multiprocessing import Pool
from pprint import pprint
import re 
from SQL.query import Search
import SQL.db as db
from sqlalchemy.orm import sessionmaker
from sqlalchemy import literal
import re
from collections import Counter


Session = sessionmaker(bind = db.engine)
session = Session()

class Test:
	def __init__(self) -> None:
		self.reached_limit = False
		self.base_url = "https://www.1881.no"
		self.industry = "advokat"
		self.company_name = None
		self.profile_url = None
		self.profile_url_snippet = None
		self.profile_name = None
		self.url = 'https://www.1881.no/adopsjon/?page=1'
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
	
	def test(self):
		profile_name = "barberern as"
		profile_url = "https://www.1881.no/akustisk-utstyr/akustisk-utstyr-agder/akustisk-utstyr-kristiansand-s/barberern-as_101488216S1/"
		ind_url = "https://www.1881.no/akustisk-utstyr"
		urls = [
			"https://www.1881.no/akustisk-utstyr/akustisk-utstyr-agder/akustisk-utstyr-kristiansand-s/barberern-as_101488216S1/",
			# "https://www.1881.no/adopsjon/adopsjon-oslo/adopsjon-solli/adopsjonsforum_100352913S1/",
			# "https://www.1881.no/adopsjon/adopsjon-innlandet/adopsjon-hamar/adopsjonsforum_100352913S15/",
			# "https://www.1881.no/adopsjon/adopsjon-vestfold-og-telemark/adopsjon-porsgrunn/adopsjonsforum_100352913S14/",
			# "https://www.1881.no/adopsjon/adopsjon-innlandet/adopsjon-kapp/danielsen-tak-og-bygg-v-tommy-danielsen_101394646S1/",
			# "https://www.1881.no/adopsjon/adopsjon-rogaland/adopsjon-stavanger/hinna-auto-nilsen_106938558S1/",
			# "https://www.1881.no/adopsjon/adopsjon-agder/adopsjon-kristiansand-s/inor-adopt_100347174S1/",
		]	
		profile_names =[
			'barberern as',
			'advokatfirmaet-riisa',
			'advokatfirmaet-nicolaisen-og-co-ans',
			'advisio-advokat-as',
		]
		for name in profile_names:
			self.profile_name = name.replace("-", " ")
			search_results = self.match_company_name_in_input_table()
			print(search_results)
			if not search_results:
				print("found no matches")
			else:
				for search_result in search_results:
					print(search_result.navn)
					print(search_result.organisasjonsnummer)
		

		'''	
		SOME HELPER INFO ABOUT TEST:
			profile_name = barberern as
			
			what im looking for is:
					BARBERER'N AS 
					992980516
		'''

	

	def match_company_name_in_input_table(self): #belongs to WordMatcher
		profile_names =[
			'barberern as',
			'advokatfirmaet-riisa',
			'advokatfirmaet-nicolaisen-og-co-ans',
			'advisio-advokat-as',
		]
		for search_string in profile_names:			
			search_string_split = search_string.split("-")[0]
			search_string = search_string.replace("-", " ")
			print(search_string_split)
	
			search_result =  session.query(db.InputTable).filter(db.InputTable.navn.ilike(f'%{search_string_split}%')).all()
			search_result = [i.navn for i in search_result]
			pprint(len(search_result))	
			candicates =[]
			for i in search_string.split("-"):
				print(i)
				rank = difflib.get_close_matches(i, search_result, cutoff=.35)
				rank.append(candicates)
			# rank = difflib.get_close_matches(search_string_split, search_result, cutoff=.35)
			# search_result = session.query(db.InputTable).filter_by(navn = search_string).all()
			# pprint([i.navn for i in search_result])	
			# break
			# return search_result

def words(text): return re.findall(r'\w+', text.lower()) #belongs to WordMatcher

class WordMatcher:

	def __init__(self, big_text):
		self.WORDS=Counter(words(big_text))
		self.N = sum(self.WORDS.values())

	def P(self, word):
		"Probability of `word`."
		return self.WORDS[word] / self.N

	def correction(self, word):
		"Most probable spelling correction for word."
		return max(self.candidates(word), key=self.P)

	def candidates(self, word):
		"Generate possible spelling corrections for word."
		return (self.known([word]) or self.known(self.edits1(word)) or self.known(self.edits2(word)) or [word])

	def known(self, words):
		"The subset of `words` that appear in the dictionary of WORDS."
		return set(w for w in words if w in self.WORDS)

	def edits1(self, word):
		"All edits that are one edit away from `word`."
		letters    = 'abcdefghijklmnopqrstuvwxyz'
		splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
		deletes    = [L + R[1:]               for L, R in splits if R]
		transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
		replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
		inserts    = [L + c + R               for L, R in splits for c in letters]
		return set(deletes + transposes + replaces + inserts)

	def edits2(self, word):
		"All edits that are two edits away from `word`."
		return (e2 for e1 in self.edits1(word) for e2 in self.edits1(e1))



def SearchBrregByAddress():
	'''
	same concept as previous only it searched brreg by Address, 
	since Addresses is less likely to have variations in the formatting. 
	
	test subject: Barberer'n AS --> two adresses:
	forretningsadresse:	Rådhusgata 5, 4611 KRISTIANSAND S
	Postadresse: Postboks 60, 4661 KRISTIANSAND S

	#! source of error (feilkidler):
		phonenumber could be a private number, and that person could own multiple companies. 
	'''
	full_adresses =[
		'Rådhusgata 5, 4611 KRISTIANSAND S',
		'Postboks 60, 4661 KRISTIANSAND S',
	]
	only_address =[
		'Rådhusgata 5',
		'Postboks 60',
	]
	only_post =[
		'4611 KRISTIANSAND S',
	]
	for search_string in full_adresses:

		search_string_split = search_string.split("-")[0]
		search_string = search_string.replace("-", " ")
		print(search_string_split)
		#> Test_1 forretningsadresse
		search_result =  session.query(db.InputTable).filter(db.InputTable.forretningsadresse.ilike(f'%{search_string_split}%')).all()

		# search_result =  session.query(db.InputTable).filter(db.InputTable.navn.ilike(f'%{search_string_split}%')).all()
		search_result = [i.navn for i in search_result]
		pprint(len(search_result))	
		candicates =[]
		for i in search_string.split("-"):
			print(i)
			rank = difflib.get_close_matches(i, search_result, cutoff=.35)
			rank.append(candicates)

# TEMP 


'''
{'land': 'Norge', 
'landkode': 'NO', 
'postnummer': '4611', 
'poststed': 'KRISTIANSAND S', 
'adresse': ['R�dhusgata 5'], 
'kommune': 'KRISTIANSAND', 
'kommunenummer': '4204'}
'''

import ast

def getBarberenAS(): #! NOT IN USE
	business_location = '4611 KRISTIANSAND S'
	business_address = 'Rådhusgata 5'
	loc, zip  = splitZipCode(business_location)
	address_list = [business_address, loc, zip ]
	org_num = 992980516
	# company = session.query(db.InputTable).filter(db.InputTable.organisasjonsnummer.ilike('992980516')).all()
	address_dict = getaddressFromInput(org_num)
	for search_string in address_list:
		search_res = search(address_dict, search_string)
		if search_res:
			print(f"{search_string}: True")
		else:
			print(f"{search_string}: False")


	
def getaddressFromInput(org_num):
	company = session.query(db.InputTable).get(org_num)
	return ast.literal_eval(company.forretningsadresse)

def splitZipCode(business_location):
	lst = business_location.split(' ')
	return ' '.join([i for i in lst if not i.isdigit()]), ''.join([i for i in lst if i.isdigit()]) 

def search(dict, searchFor):
	for k in dict.values():
		if type(k) is not list:
			k = [k]
		for v in k:
			if searchFor in v:
				return k
	return None

def checkBarberenAS(address_list):

	# company = session.query(db.InputTable).filter(db.InputTable.organisasjonsnummer.ilike('992980516')).all()
	address_dict = getaddressFromInput(org_num)
	
	res = 0 
	for search_string in address_list:
		if search(address_dict, search_string):
			res += 1
		else:
			res += 0
	if res >=2:
		return True

from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy import text
from sqlalchemy import func
def checkTableForAdresslist(address_list):
	search = 'Rådhusgata 5'
	# hit = session.query(db.InputTable).filter(db.InputTable.forretningsadresse.ast.literal_eval(company.forretningsadresse)).all()
	# hit = session.query(db.InputTable.forretningsadresse).get(search)
	# forretningsadresse = session.query(db.InputTable.forretningsadresse).all()
	# hit = ast.literal_eval(forretningsadresse)
	# print(hit) 


	# hit = session.query(db.InputTable.forretningsadresse).filter(text("forretningsadresse->['adresse'] = 'Rådhusgata 5'")).all()
	# hit = session.query(db.InputTable.forretningsadresse).filter(text("'adresse' = 'Rådhusgata 5'")).all()
	# hit = session.query(db.InputTable.forretningsadresse).filter(text("'adresse' = ['Langgata 87']")).all()
	# hit = session.query(db.InputTable.forretningsadresse).filter(text('["Langgata 87"]')).all()
	# hit = session.query(db.InputTable.organisasjonsnummer).get(992980516)
	org_num = 992980516
	company = session.query(db.InputTable).get(org_num)
	# hit.f
	print(type(company.forretningsadresse.))
	# subq = session.query(func.json_array_elements(db.InputTable.forretningsadresse).label('adresse')).subquery()
	# count = session.query(subq).filter(subq.c.adresse.op('->>')('adresse') == 'Rådhusgata 5').count()


	# print(count)
	# for search in address_list:
		
	# 	# hit = session.query(db.InputTable).filter(db.InputTable.forretningsadresse.ilike(search)).all()
	# 	hit = session.query(db.InputTable).filter(db.InputTable.forretningsadresse.ilike(search)).all()


	# 	# hit = session.query(db.InputTable).filter(db.InputTable.forretningsadresse[search].as_boolean() == False)
	# 	print(hit)
		# session.query(db.InputTable).\
    	# filter(db.InputTable.forretningsadresse.astext.cast(db.InputTable) == 1)
		# ast.literal_eval(company.forretningsadresse)


def main():
	business_location = '4611 KRISTIANSAND S'
	business_address = 'Rådhusgata 5'
	address_list = [business_address, splitZipCode(business_location)]
	# org_num = 992980516
	# res = checkBarberenAS(address_list)
	# print(res)
	checkTableForAdresslist(address_list)



def fromForretningsAdresse(): #>TEST
	search_string = 'Rådhusgata 5, 4611 KRISTIANSAND S',
	search_string_split = search_string.split(",")[0]
	search_result =  session.query(db.InputTable).filter(db.InputTable.forretningsadresse.ilike(f'%{search_string_split}%')).all()
	print(search_result)



'''#*  ______ MAIN ____________________________________________________________ *#
'''
if __name__ == '__main__':
	WORDS = ['hello there', 'Hallo', 'hi', 'house', 'key', 'screen', 'hallo', 'question', 'format']
	bixtext= "I was looking at this answer for getting a closest match from a list or possible alternatives of"
	# getBarberenAS()
	main()
	# print(WordMatcher(bixtext).candidates('form a list'))
	# Test().test()
	# Test().match_company_name_in_input_table()


	# print(difflib.get_close_matches('Hello', words))
	# import difflib

	# words_list = ['sprite','coke','lemon sparkling water']
	# print(difflib.get_close_matches('lemon watter',words_list,cutoff=.35))

