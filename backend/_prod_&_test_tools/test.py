# import time; start = time.perf_counter() #Since it also takes time to Import libs, I allways start the timer asap. 
# import pandas as pd 
# import requests 
# from bs4 import BeautifulSoup
# import numpy as np
# import json
# import gzip
# import ast
# import psycopg2
# from psycopg2.extras import Json
# from sqlalchemy import create_engine
# import concurrent.futures
# from tqdm import tqdm
# import datetime as dt

# # ___ local imports __________
# from config import payload, tablenames, settings
# from postgres import databaseManager, cleanUp, fetchData, checkForTable, postLastUpdate, deleteData, replacetData
# from file_manager import *







for i in range(0,40):

	print(f'''_callstate{i} = prefs.getBool('ff_callstate{i}') ?? _callstate{i};''')

  # bool _callstate = false;
  # bool get callstate => _callstate5;
  # set callstate(bool _value) {
  #   _callstate = _value;
  #   prefs.setBool('ff_callstate5', _value);
  # }