from sqlalchemy.orm import sessionmaker

# ___ local imports ___
import SQL.db as db

# Create new Session
Session = sessionmaker(bind = db.engine)
session = Session()

def getAllProffIndustries():
    return [s.industries for s in session.query(db.IndustryProff).all()]

def getAll1881Industries():
    return [s.industries for s in session.query(db.Industry1881).all()]

def getAllCategories():
    return [s.categories for s in session.query(db.Categories).all()]

def getAllGulesider():
    return [[s.org_num, s.navn, s.is_premium, s.tlf] for s in session.query(db.Gulesider).all()]

def getAll1881():
    return [[s.org_num, s.navn, ] for s in session.query(db._1881).all()]

def getAllInputTable():
    return [[s.org_num, s.navn, ] for s in session.query(db.InputTable).all()]



class Search:
    '''
    Currently used by _1881Extracto().rextractPage() <- (./backend/_1881.py)
    Will take company name from the profile-page and try and find a 
    match for it in brregTable instead of scraping Rengskapstall.no.
    Which could save almost 1/3 of the runtime.
    '''
    def match_company_name_in_input_table(self, profile_name:str):
        # return session.query.filter(db.InputTable.navn.contains(profile_name))
        # session.query(db.InputTable).filter_by(name = profile_name)
        row =  session.query(db.InputTable).filter(db.InputTable.navn.contains(profile_name))#.all()
        return [[s.org_num, s.navn, ] for s in row]













# import pandas as pd
# from SQL.config import engine, base
# def getAllAsPandas(tablename:str) -> pd:
#     return pd.read_sql(
#         tablename,
#         con = engine
#         )















'''#! ORIGINAL 
'''
# for s in session.query(db.Gulesider).all():
#     print(s.org_num, s.navn, s.tlf)



# print("*"*20)
# print("Gulesider med alle som begynner på 'B': ")

# # Selective data
# for s in session.query(db.Gulesider).filter(db.Gulesider.navn.startswith('B')).all():
#     print(s.org_num, s.navn, s.tlf)
