import time; start = time.perf_counter() #Since it also takes time to Import libs, I allways start the timer asap. 
from SQL.config import Dev#, DevSettings, Settings, engine, base
from SQL.query import getAllCategories
from backend.gulesider import GulesiderExtractor, outroPrint

from backend.categories import CategoryExtractor

from SQL.insert import Insert

def extractCategories():
    '''grab categories and insert to db
    '''
    CategoryExtractor().fetchCategories()

def print_categories(): 
    '''check categories 
    '''
    cat = getAllCategories()
    print(cat)

def extractGulesider():
    GulesiderExtractor().runExtraction()
    
def outroPrint():
	print("_"*62)
	print("                   Data Extraction Complete.                 ")
	print(f"                  Finished in {round(time.perf_counter() - start, 2)} second(s)                 ")
	print("_"*62)
	print()


if __name__ == '__main__':
    # extractCategories()
    # print_categories()
    extractGulesider()
    # CategoryExtractor().fetchCategories()
    outroPrint()






