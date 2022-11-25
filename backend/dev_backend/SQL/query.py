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


def getSimpleGulesider():
	return [[s.org_num, s.navn,] for s in session.query(db.Gulesider).all()]


def getAll1881():
	return [[s.org_num, s.navn, ] for s in session.query(db._1881).all()]

def getAllProff():
	return [[s.org_num, s.navn, ] for s in session.query(db.Proff).all()]

def getAllInputTable():
	return [[s.organisasjonsnummer, s.navn, ] for s in session.query(db.InputTable).all()]

def getFullInputTable():
	return [[s.organisasjonsnummer, s.navn, s.postadresse, s.forretningsadresse] for s in session.query(db.InputTable).all()]




def getGoogleInputTable():
	master_list = getSimpleGulesider()+ getAllProff()+ getAll1881()
	df = pd.DataFrame(master_list, columns = ['org_num', 'name'])
	return df.drop_duplicates(keep = 'first')
	# _gulesider = getSimpleGulesider() #might need to remove extra columns
	# _proff = getAllProff()
	# _1881 = getAll1881()
	# master_list = []
	# _gulesider = pd.DataFrame()

	



class Search:
	'''
	Currently used by _1881Extracto().rextractPage() <- (./extractors/_1881.py)
	Will take company name from the profile-page and try and find a 
	match for it in brregTable instead of scraping Rengskapstall.no.
	Which could save almost 1/3 of the runtime.
	'''
	def match_company_name_in_input_table(self, profile_name:str):
		row =  session.query(db.InputTable).filter(db.InputTable.navn.contains(profile_name))#.all()
		return [[s.org_num, s.navn, ] for s in row]

	#> TEST
	def match_adress_in_input_table(self, search_loc_, search_post_):

		if search_post_ == None:
			print("True", search_loc_, search_post_)
			search_res = session.query(db.InputTable).filter(
			db.InputTable.adresse_short.ilike('{"'+search_loc_+'"}')
			).all()
		else:
			print("False", search_loc_, search_post_)
			search_res = session.query(db.InputTable).filter(
				db.InputTable.adresse_short.ilike('{"'+search_loc_+'"}'), 
				db.InputTable.postboks.ilike('{"'+search_post_+'"}')
				).all()
		if len(search_res) == 1:
			company = search_res[0]
			return company.navn, company.organisasjonsnummer












import pandas as pd
from SQL.config import engine, base
def getAllAsPandas(tablename:str) -> pd:
	return pd.read_sql(
		tablename,
		con = engine
		)















'''#! ORIGINAL 
'''
# for s in session.query(db.Gulesider).all():
#     print(s.org_num, s.navn, s.tlf)



# print("*"*20)
# print("Gulesider med alle som begynner på 'B': ")

# # Selective data
# for s in session.query(db.Gulesider).filter(db.Gulesider.navn.startswith('B')).all():
#     print(s.org_num, s.navn, s.tlf)