import time

import pandas as pd

from backend._1881 import _1881Extractor; start = time.perf_counter() #Since it also takes time to Import libs, I allways start the timer asap. 

from backend.bransjer_proff import IndustryProffExtractor
from backend.bransjer_1881 import Industry1881Extractor
from SQL.config import Dev#, DevSettings, Settings, engine, base
from SQL.query import getAll1881, getAll1881Industries, getAllAsPandas, getAllCategories, getAllProffIndustries
from backend.gulesider import GulesiderExtractor
from backend.proff import ProffExtractor
from backend.categories import CategoryExtractor

from SQL.insert import Insert


class Print:

	def intro(self, name = None) -> None:
		print("\n")
		if name:
			''' Sub intro print '''
			# print("_"*62)   
			print(f"                  Starting: {name} Extractor                ")
			print("_"*62)
			print() 
		else:
			''' Main intro print '''
			print("="*80)
			print(f"                  	Starting: Data Extraction                ")
			print("="*80)
			print()
	
	def outro(self, name = None) -> None:
		print("\n")
		if name:
			''' sub outro print'''  
			print("_"*62)
			print(f"               	  {name} Extraction Complete.                 ")
			print(f"                  Finished in {round(time.perf_counter() - start, 2)} second(s)                 ")
			print("_"*62)
			print()
		else:  
			''' Main outro print'''  
			print("="*80)
			print("                   	Data Extraction Complete.                 ")
			print(f"                  	Finished in {round(time.perf_counter() - start, 2)} second(s)                 ")
			print("="*80)
			print()

	def industries1881(self): 
		'''check categories 
		'''
		print(getAll1881Industries())

	def industriesProff(self): 
		'''check categories 
		'''
		print(getAllProffIndustries())


	def categories(self): 
		'''check categories 
		'''
		print(getAllCategories())

	def _1881(self):
		# print(getAll1881())
		print(pd.DataFrame(getAll1881()))
		
			
def extractCategories():
	'''grab categories and insert to db
	'''
	Print().intro('gulesider: categories')
	CategoryExtractor().fetchCategories()
	Print().outro('category')

def extractGulesider():
	'''resets "gulesider" in db, then extractes gulersider.no by category
	'''
	Print().intro('Gulesider')
	GulesiderExtractor().runExtraction()
	Print().outro('Gulesider')

def extractProffIndustries():
	'''grab categories and insert to db
	'''
	Print().intro('proff: industries')
	IndustryProffExtractor().fetchIndustries()
	Print().outro('industry')

def extractProff():
	'''resets "proff" in db, then extractes proff.no by industry
	'''
	Print().intro('Proff')
	ProffExtractor().runExtraction()
	Print().outro('Proff')

def extract1881():
	Print().intro('1881')
	_1881Extractor().runExtraction()
	Print().outro('1881')

def extractIndustries1881():
	Industry1881Extractor().fetchIndustries()

if __name__ == '__main__':
	Print().intro()

	# extractCategories()
	# Print().categories()

	# Print().intro('Gulesider')
	extractGulesider()
	# Print().outro('Gulesider')
	# extractProffIndustries()
	# Print().industriesProff()

	# Print().intro('Proff')
	# extractProff()
	# Print().outro('Proff')

	# # extractIndustries1881()
	# # extract1881()
	# # Print()._1881()
	Print().outro()





''' 
____ Track_record ____
	time spent per extractor for whole data extraction 
	brreg:				xx.xxxs
	
	gulesider:			xx.xxxs
	proff:				49.620s
	1881:				xx.xxxs

	industries_1881: 	xx.xxxs
	industries_proff:	xx.xxxs
	categories: 		xx.xxxs
	
	google: 			xx.xxxs

	TOT. TIME =   		xx.xxxs
'''


