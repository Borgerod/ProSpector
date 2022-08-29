import time; start = time.perf_counter() #Since it also takes time to Import libs, I allways start the timer asap. 
import pandas as pd 
import requests 
from bs4 import BeautifulSoup
import numpy as np
import json
import gzip
import ast
import psycopg2
from psycopg2.extras import Json
from sqlalchemy import create_engine
import concurrent.futures
from tqdm import tqdm
import datetime as dt

# ___ local imports __________
from config import payload, tablenames, settings
from postgres import databaseManager, cleanUp, fetchData, checkForTable, postLastUpdate, deleteData, replacetData
from file_manager import *

time.sleep(1)
def outroPrint():
    print("_"*62)
    print("                   Data Extraction Complete.                 ")
    print(f"             Finished in {round(time.perf_counter() - start, 2)} second(s) | [{str(dt.timedelta(seconds=round(time.perf_counter() - start)))}]                ")
    print()
    print("_"*62)
    print()

outroPrint()