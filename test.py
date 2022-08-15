# import time; start = time.perf_counter() #Since it also takes time to Import libs, I allways start the timer asap. 
# import os
# import re
# import string
# import pandas as pd
# import numpy as np
# from os import path
# from tqdm import tqdm
# import concurrent.futures
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from inspect import currentframe, getframeinfo
# import json
# import psycopg2
# from psycopg2.extras import Json
# from sqlalchemy import create_engine
# from tqdm import tqdm
# import pandas as pd 
# import requests 
# from bs4 import BeautifulSoup
# import numpy as np
# import pandas as pd 
# import json
# import psycopg2
# from psycopg2.extras import Json
# from sqlalchemy import create_engine
# import concurrent.futures
# from tqdm import tqdm

import time; start = time.perf_counter() #Since it also takes time to Import libs, I allways start the timer asap. 
import pandas as pd 
import requests 
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd 
import json
import psycopg2
from psycopg2.extras import Json
from sqlalchemy import create_engine
import concurrent.futures
from tqdm import tqdm
import gzip
import pprint
import ast

# ___ local imports __________
from config import payload, tablenames, settings
from postgres import databaseManager, cleanUp, fetchData, checkForTable, postLastUpdate, replacetData
from file_manager import *
import os 


print(fetchData('google_table'))
# print(os.cpu_count() or 1)
# def extractionManager(chunk):
# 	return chunk


# input_array = fetchData('input_table').to_numpy()
# print(f'full input_array: {len(input_array)}')
# chunks = input_array
# # chunks = input_array[:600] #TEMP - while testing
# print(f'current run uses {len(chunks)}')
# print(f'current run uses {len(chunks[0])}')
# print(f'example; first element in the first chunk: {chunks[0][0]}')
# with concurrent.futures.ThreadPoolExecutor() as executor:
# # with concurrent.futures.ThreadPoolExecutor(max_workers=-1) as executor:
# 	results = executor.map(extractionManager, chunks)

'''! DONT DELETE THIS _________________________________________________________
'''

# '''BOILERPLATE CODE FOR input_table updater
# '''

# ''' liste 1 original'''
# # lst1 = [[98908098, 'company1', 10],
# # [55508098, 'company2', 20],
# # [95454008, 'company3', 30],
# # [92228098, 'company4', 40],]


# ''' liste 1 men med slettet enhet'''
# lst1 = [[98908098, 'company1', 10],
# [55508098, 'company2', 20],
# [95454008, 'company3', 30],
# [92228098, 'company4', 40],]
# # _____________________________________

# ''' liste 2 original'''
# # lst2 = [[98908098, 'company1', 10],
# # [55508098, 'company2', 666],
# # [95454008, 'company3', 666],
# # [92228098, 'company4', 40],]

# # ''' liste 2 men med slettet enhet'''
# lst2 = [[98908098, 'company1', 10],
# [55508098, 'company2', 666],
# [95454008, 'company3', 666],
# [66255098, 'company5', 50],]

# # # ''' liste 2 men med ny enhet'''
# # lst2 = [[98908098, 'company1', 10],
# # [55508098, 'company2', 666],
# # [95454008, 'company3', 666],
# # [92228098, 'company4', 40],
# # [66255098, 'company5', 50],]
# # _____________________________________


# df1 = pd.DataFrame(lst1, columns=['org_num', 'company_name', 'value'])
# print(df1)
# df2 = pd.DataFrame(lst2, columns=['org_num', 'company_name', 'value'])
# print(df2)
# print()
# print()
# ''' 

# '''
# common = df1.merge(df2,on=['org_num','company_name'])
# print(common)

# deleted = df1[(~df1.org_num.isin(common.org_num))&(~df1.company_name.isin(common.company_name))]
# print(df)

# new = df2[~(df1.org_num.isin(df2.org_num))&(~df1.company_name.isin(df2.company_name))]
# print(df)



# '''
#     makes a dataframe from all differences
# '''


# # df = pd.concat([df1, df2])
# # df = df.reset_index(drop = True)

# # df_gpby = df.groupby(list(df.columns))

# # idx = [x[0] for x in df_gpby.groups.values() if len(x) == 1]

# # df = df.reindex(idx)
# # print(df)
# # df = df.drop_duplicates(subset = 'org_num', keep = 'last')
# # print(df)


'''! _____________________________________________________________________________________________
'''
