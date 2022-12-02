import site
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker
import pandas as pd

# ___ local imports ___
import SQL.db as db
from SQL.db import InputTable, Categories, Gulesider, _1881, Proff
from SQL.insert import Insert

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
	return [[s.org_num, s.navn, s.tlf] for s in session.query(db.Gulesider).all()]

def getAll1881():
	return [[s.org_num, s.navn, s.tlf] for s in session.query(db._1881).all()]

def getAllProff():
	return [[s.org_num, s.navn, s.tlf] for s in session.query(db.Proff).all()]

def getAllBrregTable():
	# TODO MAKE db.BrregTable
	return [[s.organisasjonsnummer, s.navn, ] for s in session.query(db.BrregTable).all()]

def getInputTableShort():
	return [[s.organisasjonsnummer, s.navn, ] for s in session.query(db.InputTable).all()]

def getAllInputTable():
	return [[s.organisasjonsnummer, s.navn, s.forretningsadresse] for s in session.query(db.InputTable).all()]

def getCompanyFromInputTableByOrgNum(org_num:int) -> list:
	row =  session.query(db.InputTable).filter(db.InputTable.organisasjonsnummer==org_num)
	return [[s.organisasjonsnummer, s.navn, s.forretningsadresse,] for s in row]

def genGoogleInputTable():
	master_list = getSimpleGulesider()+ getAllProff()+ getAll1881()
	_input = pd.DataFrame(master_list, columns = ['org_num', 'name', 'tlf'])
	_input = _input.drop_duplicates(keep = 'first')
	_info = pd.DataFrame(getAllInputTable(), columns = ['org_num','name','loc'])
	_info = _info.drop_duplicates(keep = 'first')
	output = _info.loc[(_info.org_num.isin(_input['org_num'])),:].reset_index(drop=True)
	Insert().toGoogle(output.to_numpy())
	
def getAllGoogle():
	return [[s.org_num, s.name, s.tlf, s.loc] for s in session.query(db.Google).all()]


# TODO [ ] change organisasjonsnummer to org_num (and translate the other names)
class Search():
	'''
	example:
		Search(InputTable).company_by_org_num(998767571)

	NOTE: imports needed to use this;
			from SQL.db import InputTable, Categories, Gulesider, _1881, Proff
			from SQL.query import Search 
	'''
	def __init__(self, table) -> None:
		self.table = table

	def company_by_org_num(self, org_num:int) -> dict:
		return session.query(self.table).filter_by(organisasjonsnummer = org_num).first().__dict__
	
	def company_by_name(self, name:str) -> dict:
		'''non-case sentitive name search'''
		return session.query(self.table).filter(func.lower(self.table.navn) == func.lower(name)).first().__dict__




# # Search(input_table).for_company_by_org_num()
# class Search:
# 	'''
# 	Currently used by _1881Extracto().rextractPage() <- (./extractors/_1881.py)
# 	Will take company name from the profile-page and try and find a 
# 	match for it in brregTable instead of scraping Rengskapstall.no.
# 	Which could save almost 1/3 of the runtime.
# 	'''
# 	def get_company_by_org_num_in_input_table(self, org_num:int):
# 		row =  session.query(db.InputTable).filter(db.InputTable.organisasjonsnummer.contains(org_num))#.all()
# 		return [[s.organisasjonsnummer, s.navn, s.forretningsadresse, s.forretningsadresse] for s in row]

# 	def match_company_name_in_input_table(self, profile_name:str):
# 		row =  session.query(db.InputTable).filter(db.InputTable.navn.contains(profile_name))#.all()
# 		return [[s.org_num, s.navn, ] for s in row]

# 	#> TEST
# 	def match_address_in_input_table(self, search_loc_, search_post_):

# 		if search_post_ == None:
# 			print("True", search_loc_, search_post_)
# 			search_res = session.query(db.InputTable).filter(
# 			db.InputTable.adresse_short.ilike('{"'+search_loc_+'"}')
# 			).all()
# 		else:
# 			print("False", search_loc_, search_post_)
# 			search_res = session.query(db.InputTable).filter(
# 				db.InputTable.adresse_short.ilike('{"'+search_loc_+'"}'), 
# 				db.InputTable.postboks.ilike('{"'+search_post_+'"}')
# 				).all()
# 		if len(search_res) == 1:
# 			company = search_res[0]
# 			return company.navn, company.organisasjonsnummer
