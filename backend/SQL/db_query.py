import pandas as pd
import SQL.db as db
from SQL.add_row import getSession
from sqlalchemy import  create_engine, Column, String, Integer, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from SQL.config import settings

session = getSession()

engine = create_engine(settings.DATABASE_URL)

def getAll():
    return pd.read_sql_table(
        'call_list',
        con = engine
        )

def getTest():
    return pd.read_sql_table(
        'call_list_test',
        con = engine
        )