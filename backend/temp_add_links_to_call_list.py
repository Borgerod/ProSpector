
from dataclasses import replace
import enum
from subprocess import call
import time
from typing import Any
from unicodedata import name; START = time.perf_counter() #Since it also takes time to Import libs, I allways START the timer asap. 
from typing_extensions import Self

import re
import os
import numpy as np
import datetime as dt
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from sqlalchemy.orm.session import Session

'''___ local imports __________
'''
from file_manager import *
from recaptcha_solver import Recaptcha as Recaptcha
from SQL.db_query import getAll, getTest
from SQL.add_row import getSession
import SQL.db as db
import pandas as pd 

import SQL.db as db
from sqlalchemy.orm import sessionmaker



from sqlalchemy import  create_engine, Column, String, Integer, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from SQL.config import settings
print(settings.DATABASE_URL)

engine = "postgresql://postgres:F%K6L51KXGXs@prospector-user-api.cpjevlwuwfix.eu-west-2.rds.amazonaws.com:5432/ProSpector_User_API"
# engine = "postgresql://postgres:Orikkel1991@prospector-user-api.cpjevlwuwfix.eu-west-2.rds.amazonaws.com:5432/ProSpector_User_API"

# engine = create_engine(settings.DATABASE_URL)
call_list = getAll()

def editName(name):
    return name.replace(" ", "+")

url_list = []
for i, name in enumerate(call_list.navn):
    _name = editName(name)
    url = f"https://www.google.com/search?q={_name}+maps&hl=en"    
    call_list.iloc[i].link_til_profil = url
    url_list.append(url)

link_til_profil = pd.DataFrame(url_list, columns=["link_til_profil"])
call_list = pd.concat([call_list, link_til_profil], axis=1)
call_list.to_sql('call_list', con=engine, if_exists='replace')
