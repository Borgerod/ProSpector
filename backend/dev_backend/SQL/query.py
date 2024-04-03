import site
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker
import pandas as pd

''' ___ local imports ___ '''
import SQL.db as db
from SQL.db import InputTable, Gulesider, _1881, Proff
from backend.dev_backend.SQL.models.insert import Insert

# Create new Session
Session = sessionmaker(bind = db.engine)
session = Session()

'''#* ___ NEW Query Solutions ________________________________ '''



# class Query:
# 	# > Try: test out @dataclass
# 		# > Comment: Apperently, according to this article "https://towardsdatascience.com/battle-of-the-data-containers-which-python-typed-structure-is-the-best-6d28fde824e"
# 		# >			 the overall most efficiant way to make and run classes are with slots, so i will try that instead.	
# 	# todo: [ ] integrate new solution for rest of code. 

# 	__slots__ = 'get_industries', '', '',
	
# 	def __init__(self) -> None:
# 		self.get_industries = False
	
# 	def getFuncFromArg(self, name):
# 		match name:
# 			case 'proff':
# 				if self.get_industries:
# 					return "db.ProffIndustries"
# 				else:
# 					return "db.Proff"

# 			case 'Gulesider':
# 				if self.get_industries:
# 					return "db.GulesiderIndustries"
# 				else:
# 					return "db.Gulesider"

# 			case '1881':
# 				if self.get_industries:
# 					return "db._1881Industries"
# 				else:
# 					return "db._1881"

# 			case 'google':
# 				return "db.Google"

# 			case 'InputTable':
# 				return "db.InputTable"

# 	# def getFuncFromIndustryTables(self, name):
# 	# 		match name:
# 	# 			case 'proff':
# 	# 				return ...

# 	# 			case 'Gulesider':
# 	# 				return ...	

# 	# 			case '1881':
# 	# 				return ...
	
# 	@property
# 	def industries(self):
# 		self.get_industries = True
	
# 	# def getIndustry(self, name):
# 	# 	func = self.getFuncFromArg(name)
# 	# 	data = func()

# 	def get(self, name):
# 		func = self.getFuncFromArg()
# 		# if self.get_industries:
# 		# func = self.getFuncFromMainTables(name)
# 		# else:
# 		# 	func = self.getFuncFromIndustryTables(name)


# # data = Query('industry').get('Gulesider')


# data = Query().get('Gulesider').industries
# print(data)



class Query:
	def __init__(self, *type) -> None:
		self.type = type 
		self.name = None
		self.type_variants = [
			'industry',
			'Industry',
			'industries',
			'Industries',
			]

	def getTable(self):
		return getattr(db, self.name)

	def get(self, name, ) -> list:
		self.name = name
		self.checkType()
		# query = session.query(getattr(db, self.name)).all()
		# return pd.read_sql(query)
		return session.query(getattr(db, self.name)).all()
		# return [s.industries for s in session.query(getattr(db, self.name)).all()]

	def checkType(self):
		if any(variant in self.type for variant in self.type_variants):
			self.name = 'Industry' + self.name

# x = Query('industry').get('Gulesider')


'''
Query().get("gulesider").industry
Query().get.industry()
Query().industries.get()
'''

'''#! ___ OLD Query Solutions ________________________________ '''
def getAllProffIndustries():
	return [s.industries for s in session.query(db.IndustryProff).all()]

def getAll1881Industries():
	return [s.industries for s in session.query(db.Industry1881).all()]

def getAllGulesiderIndustries():
	return [s.industries for s in session.query(db.IndustryGulesider).all()]

def getAllGulesider():
	return [[s.org_num, s.name, s.is_premium, s.tlf] for s in session.query(db.Gulesider).all()]

def getSimpleGulesider():
	return [[s.org_num, s.name, s.tlf] for s in session.query(db.Gulesider).all()]

def getAll1881():
	return [[s.org_num, s.name, s.tlf] for s in session.query(db._1881).all()]

def getAllProff():
	return [[s.org_num, s.name, s.tlf] for s in session.query(db.Proff).all()]

def getAllBrregTable():
	# TODO MAKE db.BrregTable
	return [[s.org_num, s.name, ] for s in session.query(db.BrregTable).all()]

def getInputTableShort():
	return [[s.org_num, s.name, ] for s in session.query(db.InputTable).all()]

def getAllInputTable():
	return [[s.org_num, s.name, s.loc] for s in session.query(db.InputTable).all()]

def getCompanyFromInputTableByOrgNum(org_num:int) -> list:
	row =  session.query(db.InputTable).filter(db.InputTable.org_num==org_num)
	return [[s.org_num, s.name, s.loc,] for s in row]

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


# # TODO [ ] change org_num to org_num (and translate the other names)
# class Search():
# 	'''
# 	example:
# 		Search(InputTable).company_by_org_num(998767571)

# 	NOTE: imports needed to use this;
# 			from SQL.db import InputTable, Industries, Gulesider, _1881, Proff
# 			from backend.dev_backend.SQL.query import Search 
# 	'''
# 	def __init__(self, table) -> None:
# 		self.table = table

# 	def company_by_org_num(self, org_num:int) -> dict:
# 		return session.query(self.table).filter_by(org_num = org_num).first().__dict__
	
# 	def company_by_name(self, name:str) -> dict:
# 		'''non-case sentitive name search'''
# 		return session.query(self.table).filter(func.lower(self.table.name) == func.lower(name)).first().__dict__




# # # Search(input_table).for_company_by_org_num()
# # class Search:
# # 	'''
# # 	Currently used by _1881Extracto().rextractPage() <- (./extractors/_1881.py)
# # 	Will take company name from the profile-page and try and find a 
# # 	match for it in brregTable instead of scraping Rengskapstall.no.
# # 	Which could save almost 1/3 of the runtime.
# # 	'''
# # 	def get_company_by_org_num_in_input_table(self, org_num:int):
# # 		row =  session.query(db.InputTable).filter(db.InputTable.org_num.contains(org_num))#.all()
# # 		return [[s.org_num, s.name, s.loc, s.loc] for s in row]

# # 	def match_company_name_in_input_table(self, profile_name:str):
# # 		row =  session.query(db.InputTable).filter(db.InputTable.name.contains(profile_name))#.all()
# # 		return [[s.org_num, s.name, ] for s in row]

# # 	#> TEST
# # 	def match_address_in_input_table(self, search_loc_, search_post_):

# # 		if search_post_ == None:
# # 			print("True", search_loc_, search_post_)
# # 			search_res = session.query(db.InputTable).filter(
# # 			db.InputTable.adresse_short.ilike('{"'+search_loc_+'"}')
# # 			).all()
# # 		else:
# # 			print("False", search_loc_, search_post_)
# # 			search_res = session.query(db.InputTable).filter(
# # 				db.InputTable.adresse_short.ilike('{"'+search_loc_+'"}'), 
# # 				db.InputTable.postboks.ilike('{"'+search_post_+'"}')
# # 				).all()
# # 		if len(search_res) == 1:
# # 			company = search_res[0]
# # 			return company.name, company.org_num
