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
			# self.profile_url = url
			# self.profile_name = self.profile_url.split("/")[-2].split("_")[0].replace("-", " ")
			self.profile_name = name.replace("-", " ")
			search_results = self.match_company_name_in_input_table()
			print(search_results)
			if not search_results:
				print("found no matches")
			else:
				for search_result in search_results:
					print(search_result.navn)
					print(search_result.organisasjonsnummer)
		# for url in urls:
		# 	self.profile_url = url
		# 	self.profile_name = self.profile_url.split("/")[-2].split("_")[0].replace("-", " ")
		# 	search_results = self.match_company_name_in_input_table()
		# 	if not search_results:
		# 		print("found no matches")
		# 	else:
		# 		for search_result in search_results:
		# 			print(search_result.navn)
		# 			print(search_result.organisasjonsnummer)
		
		'''
		profile_name = barberern as
		'''
			# print(getAllInputTable())
		'''	what im looking for is:
				BARBERER'N AS 
				992980516
		'''

	

	def match_company_name_in_input_table(self):
		# self.profile_name
		# search_result =  session.query(db.InputTable).filter(db.InputTable.navn.match(f'%{self.profile_name}%')).all()
		# search_result =  session.query(db.InputTable).filter(db.InputTable.navn.contains(f'%{self.profile_name}%')).all()
		
		# search_result =  session.query(db.InputTable).filter(db.InputTable.navn.match(f'%advokatfirmaet riisa%')).all()
		# search_result =  session.query(db.InputTable).filter(db.InputTable.navn.match(search_string)).all()
		
		profile_names =[
			# 'barberern as',
			'advokatfirmaet-riisa',
			'advokatfirmaet-nicolaisen-og-co-ans',
			'advisio-advokat-as',
		]
		# search_strings = ['advokatfirmaet', 'riisa']
		# search_string = f'%advokatfirmaet riisa%'
		# search_string = 'advokatfirmaet riisa'
		for search_string in profile_names:
			# search_string = search_string.replace("-", " ")
			
			search_string_split = search_string.split("-")[0]
			search_string = search_string.replace("-", " ")
			# search_string = [f'%{i}%' for i in search_string]
			# search_string = "advokatfirmaet riisa"
			# search_string = ['advokatfirmaet', 'riisa']
			print(search_string_split)
			# # search_result = session.query(db.InputTable).filter(literal(search_string).contains(db.InputTable.navn)).all()
			# # print(search_result)
			# # search_result =  session.query(db.InputTable).filter(db.InputTable.navn.contains(literal(search_string))).all()
			# # print(search_result)
			# # search_result =  session.query(db.InputTable).filter(db.InputTable.navn.contains(literal(search_string))).all()
			# # print(search_result)
			# # search_result =  session.query(db.InputTable).filter(db.InputTable.navn.contains(search_string)).all()
			## print(search_result)




			# search_result =  session.query(db.InputTable).filter(db.InputTable.navn.match(search_string)).all()
			# pprint([i.navn for i in search_result])	

			# search_result =  session.query(db.InputTable).filter(db.InputTable.navn.match(literal(search_string))).all()
			# pprint([i.navn for i in search_result])		

			# search_result =  session.query(db.InputTable).filter(db.InputTable.navn.ilike(literal(search_string))).all()
			# pprint([i.navn for i in search_result])	
			search_result =  session.query(db.InputTable).filter(db.InputTable.navn.ilike(f'%{search_string_split}%')).all()
			search_result = [i.navn for i in search_result]
			pprint(len(search_result))	
			# print(search_string)
			# rank = difflib.get_close_matches(search_string, search_result)	
			# rank = difflib.get_close_matches(search_string, search_result, cutoff=.35)
			candicates =[]
			for i in search_string.split("-"):
				print(i)
				rank = difflib.get_close_matches(i, search_result, cutoff=.35)
				rank.append(candicates)
			# rank = difflib.get_close_matches(search_string_split, search_result, cutoff=.35)
			print(candicates)	
			# search_result = session.query(db.InputTable).filter_by(navn = search_string).all()
			# pprint([i.navn for i in search_result])	
			print("_"*20)
			# break
			# return search_result




import re
from collections import Counter

def words(text): return re.findall(r'\w+', text.lower())

# WORDS = Counter(words(open('big.txt').read()))


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

if __name__ == '__main__':
	WORDS = ['hello there', 'Hallo', 'hi', 'house', 'key', 'screen', 'hallo', 'question', 'format']
	bixtext= "I was looking at this answer for getting a closest match from a list or possible alternatives of"


	# print(WordMatcher(bixtext).candidates('form a list'))
	# Test().test()
	Test().match_company_name_in_input_table()


	# print(difflib.get_close_matches('Hello', words))
	# import difflib

	# words_list = ['sprite','coke','lemon sparkling water']
	# print(difflib.get_close_matches('lemon watter',words_list,cutoff=.35))

