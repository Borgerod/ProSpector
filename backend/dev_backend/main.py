import time

start = time.perf_counter() #Since it also takes time to Import libs, I allways start the timer asap. 
import pandas as pd

''' Local Imports'''
from SQL.config import Dev
from SQL.insert import Insert
from SQL.query import getAll1881, getAll1881Industries, getAllCategories, getAllGulesider, getAllProffIndustries, getAllGoogle, getAllProff, getAllBrregTable, getAllInputTable
from extractors.bransjer_proff import IndustryProffExtractor
from extractors.proff import ProffExtractor
from extractors.bransjer_1881 import Industry1881Extractor
from extractors._1881 import _1881Extractor
from extractors.gulesider import GulesiderExtractor
from extractors.categories import CategoryExtractor
from extractors.google import GoogleExtractor
from extractors.brreg import BrregExtractor

class Print:

	def intro(self, name = None) -> None:
		print("\n")
		if name:
			''' Sub intro print '''
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

	def inputTable(self):
		print(pd.DataFrame(getAllBrregTable()))

	def inputTable(self):
		print(pd.DataFrame(getAllInputTable()))

	def gulesider(self):
		print(pd.DataFrame(getAllGulesider()))

	def proff(self):
		print(pd.DataFrame(getAllProff()))

	def _1881(self):
		print(pd.DataFrame(getAll1881()))	

	def googleInput(self):
		print(pd.DataFrame(getAllGoogle()))


def extractBrreg():
	''' downloads brreg data and creates brreg_table and input_table
	'''
	Print().intro('Brreg')
	BrregExtractor().runExtraction()
	Print().outro('Brreg')

def extractCategories():
	'''grab categories and insert to db
	'''
	Print().intro('gulesider: categories')
	CategoryExtractor().fetchCategories()
	Print().outro('gulesider: categories')

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
	Print().outro('proff: industries')

def extractProff():
	'''resets "proff" in db, then extractes proff.no by industry
	'''
	Print().intro('Proff')
	ProffExtractor().runExtraction()
	Print().outro('Proff')

def extractIndustries1881():
	Print().intro('1881: industries')	
	Industry1881Extractor().fetchIndustries()
	Print().outro('1881: industries')

def extract1881():
	Print().intro('1881')
	_1881Extractor().runExtraction()
	Print().outro('1881')

def extractGoogle():
	Print().intro('Google')
	GoogleExtractor().runExtraction()
	Print().outro('Google')

if __name__ == '__main__':
	
	Print().intro()

	''' ____ Gulesider ____ '''
	# extractCategories()
	# Print().categories()

	# extractGulesider()
	# Print().gulesider()


	''' ____ Proff ____ '''
	# extractProffIndustries()
	# Print().industriesProff()

	
	# extractProff()
	# Print().proff()


	''' ____ 1881 ____ '''
	# extractIndustries1881()
	# Print().proindustries1881()

	# extract1881()
	# Print()._1881()


	''' ____ Google ____'''
	# genGoogleInputTable()
	# Print().googleInput()
	# extractGoogle()

	''' ____ Brreg ____ '''
	# Print().inputTable()
	extractBrreg()

	Print().outro()





''' 
____ Track_record ____
	time spent per extractor for whole data extraction 
	brreg:				294.28s  (141.04s if .to_sql() is used) 
	
	gulesider:			178.880s
	proff:				49.620s
	1881:				609.630s

	industries_1881: 	3.590s
	industries_proff:	5.510s
	categories: 		5.050s
	
	google: 			3876.000s

	TOT. TIME =   		5022.559s
'''
