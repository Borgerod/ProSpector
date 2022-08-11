import pandas as pd 
import numpy as np
import pandas as pd 
import json
import psycopg2
from psycopg2.extras import Json
from sqlalchemy import create_engine
import concurrent.futures
from inspect import currentframe, getframeinfo
import re
import time; start = time.perf_counter() #Since it also takes time to Import libs, I allways start the timer asap. 
import re
import pandas as pd
import numpy as np
from tqdm import tqdm
import concurrent.futures
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from inspect import currentframe, getframeinfo


# ___ local imports __________
from config import tablenames
from file_manager import *



def inputTableManager():
	# print(getFilePath())
	# print(getRelativePath())
	# print(getFileName())
	# print(get_caller_info())
	tablename = parseTablenames(getFileName())
	print(tablename)
	print(f'full filepath: {getFilePath()}')
	print(f'relative filepath: {getRelativePath()}')
	print(f'filename: {getFileName()}')


if __name__ == '__main__':
	inputTableManager()
