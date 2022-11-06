import time; start = time.perf_counter() #Since it also takes time to Import libs, I allways start the timer asap. 
import pandas as pd
from tqdm import tqdm
from multiprocessing import Pool

''' ___ local imports __________'''
# from config import tablenames
# from SQL.postgres import getInputTable, checkIfMissing, deleteData
# from base_extractor import genSearchTerm, pullRequest


''' 
	* CURRENT EXTRACTION TIME *
		- Amount of companies : 6034  
		- Finished in 11.2 second(s)
'''
tablenames = {
    'input':'input_table',
    'output':'gulesider_test',
}




class GulesiderExtractor:
	