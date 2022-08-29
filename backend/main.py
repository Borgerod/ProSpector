'''
	The overall controll panel / manager for the whole extraction process
'''


''' ___ local imports __________'''
from config import payload, tablenames, settings
from postgres import databaseManager, getInputTable
from file_manager import *
from input_table import inputTable
from base_extractor import genSearchTerm, pullRequest

from brreg import brregExtractor
from I88I import opplysningenExtractor
from gulesider import gulesiderExtractor
from google import googleExtractor
from proff import proffExtractor

from multiprocessing import Pool
from itertools import repeat


# [opplysningenExtractor(testmode = True),
# gulesiderExtractor(testmode = True),
# googleExtractor(testmode = True),]

# with concurrent.futures.ThreadPoolExecutor() as executor:
# 	list(tqdm(executor.map(updateAPI, all_pages), total = len(all_pages)))
# # gulesiderExtractor(testmode = True)





def parallelize(n_workers, functions):
    # if you need this multiple times, instantiate the pool outside and
    # pass it in as dependency to spare recreation all over again
    with Pool(n_workers) as pool:
        tasks = zip(functions)
        futures = [pool.apply_async(*t) for t in tasks]
        results = [fut.get() for fut in futures]
    # return results


if __name__ == '__main__':
    N_WORKERS = 3
    functions = opplysningenExtractor, gulesiderExtractor, googleExtractor
    # results = 
    parallelize(N_WORKERS, functions)
    # print(results)