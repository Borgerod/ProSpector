from sqlalchemy.orm import sessionmaker

# ___ local imports ___
import SQL.db as db

# Create new Session
Session = sessionmaker(bind = db.engine)
session = Session()

def getAllIndustries():
    return [s.industries for s in session.query(db.Industry).all()]



def getAllCategories():
    return [s.categories for s in session.query(db.Categories).all()]
# print(getAllCategories())

def getAllGulesider():
    return [[s.org_num, s.navn, s.tlf] for s in session.query(db.Gulesider).all()]
# print(getAllGulesider())

import pandas as pd
from SQL.config import engine, base
def getAllAsPandas(tablename:str) -> pd:
    return pd.read_sql(
        tablename,
        con = engine
        )
# df = getAllAsPandas(tablename = 'gulesider')
# print(df)



'''#! ORIGINAL 
'''
# for s in session.query(db.Gulesider).all():
#     print(s.org_num, s.navn, s.tlf)



# print("*"*20)
# print("Gulesider med alle som begynner på 'B': ")

# # Selective data
# for s in session.query(db.Gulesider).filter(db.Gulesider.navn.startswith('B')).all():
#     print(s.org_num, s.navn, s.tlf)