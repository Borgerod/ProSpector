import time



import pandas as pd
start = time.perf_counter() #Since it also takes time to Import libs, I allways start the timer asap. 

''' Local Imports'''
from SQL.config import Dev
from SQL.insert import Insert
from SQL.query import Query, getAll1881, getAll1881Industries, getAllGulesiderIndustries, getAllGulesider, getAllProffIndustries, getAllGoogle, getAllProff, getAllBrregTable, getAllInputTable
# from extractors.industries_proff import IndustryProffExtractor
# from extractors.proff import ProffExtractor
# from extractors.industries_1881 import Industry1881Extractor
# from extractors._1881 import _1881Extractor
from extractors.gulesider import GulesiderExtractor
from extractors.industries_gulesider import IndustryGulesiderExtractor
from extractors.brreg import BrregExtractor



from extractors.google import GoogleExtractor

# # TODO [ ] Finish testing all of the extractors 

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
		'''check industries 
		'''
		print(pd.DataFrame(Query('industry').get('_1881')))

	def industriesProff(self): 
		'''check industries 
		'''
		print(pd.DataFrame(Query('industry').get('Proff')))

	def industriesGulesider(self): 
		'''check industries 
		'''
		print(pd.DataFrame(Query('industry').get('Gulesider')))

	def inputTable(self):
		print(pd.DataFrame(Query.get('Gulesider')))

	def inputTable(self):
		print(pd.DataFrame(Query().get('Gulesider')))

	def gulesider(self):
		print(pd.DataFrame(Query().get('Gulesider')))

	def proff(self):
		print(pd.DataFrame(Query().get('Gulesider')))

	def _1881(self):
		print(pd.DataFrame(Query().get('Gulesider')))	

	def googleInput(self):
		print(pd.DataFrame(Query().get('Gulesider')))

def extractBrreg():
	''' downloads brreg data and creates brreg_table and input_table
	'''
	Print().intro('Brreg')
	BrregExtractor().runExtraction()
	Print().outro('Brreg')

def extractGulesiderIndustries():
	'''grab industries and insert to db
	'''
	Print().intro('gulesider: industries')
	IndustryGulesiderExtractor().fetchIndustries()
	Print().outro('gulesider: industries')

def extractGulesider():
	'''resets "gulesider" in db, then extractes gulersider.no by category
	'''
	Print().intro('Gulesider')
	GulesiderExtractor().runExtraction()
	Print().outro('Gulesider')

def extractProffIndustries():
	'''grab industries and insert to db
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

from utilities.chromedriver_installer import Chrome


if __name__ == '__main__':
	

	''' ____ Gulesider ____ '''
	extractGulesiderIndustries()
	# Print().industriesGulesider()

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
	# extractBrreg()

	# Print().outro()

'''
ALT Query test:
	Print().intro()
	from SQL.query import Query
	x = Query('industry').get('Gulesider', 'first')
	# x = Query.get('Gulesider')
	print(x)
	# print(pd.DataFrame(x))

'''



''' 
____ Track_record ____
	time spent per extractor for whole data extraction 
	brreg:				294.28s  (141.04s if .to_sql() is used) 
	
	gulesider:			178.880s
	proff:				49.620s
	1881:				609.630s

	industries_1881: 	3.590s
	industries_proff:	5.510s
	industries: 		5.050s
	
	google: 			3876.000s

	TOT. TIME =   		5022.559s
'''
