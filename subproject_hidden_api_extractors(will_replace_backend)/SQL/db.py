from sqlalchemy import Column, String, Integer, Boolean

# ___ local imports ___
from SQL.config import engine, base

# from config import Dev 
# engine = Dev().engine
# base = Dev().base
from SQL.config import Dev as dev
engine = dev.engine
base = dev.base

class Categories(base):
	''' Categories used by Gulesider
	'''
	__tablename__ = "categories"
	categories = Column(String, unique = True, index = True, primary_key = True)

	def __init__(self, categories):
		self.categories = categories

class Gulesider(base):
	__tablename__ = "gulesider"
	org_num = Column(Integer, unique = True, index = True, primary_key = True)
	navn = Column(String, index = True)
	is_premium = Column(Boolean, index = True) 
	tlf = Column(String, index = True)
	
	def __init__(self, org_num, navn, is_premium, tlf):
		self.org_num = org_num
		self.navn = navn
		self.is_premium = is_premium
		self.tlf = tlf

class Proff(base):
	__tablename__ = "proff"
	org_num = Column(Integer, unique = True, index = True, primary_key = True)
	navn = Column(String, index = True)
	
	def __init__(self, org_num, navn):
		self.org_num = org_num
		self.navn = navn

class IndustryProff(base):
	''' Industries used by Proff
	'''
	__tablename__ = "proff_industries"
	industries = Column(String, unique = True, index = True, primary_key = True)

	def __init__(self, industries):
		self.industries = industries

class Industry1881(base):
	''' Industries used by Proff
	'''
	__tablename__ = "1881_industries"
	industries = Column(String, unique = True, index = True, primary_key = True)

	def __init__(self, industries):
		self.industries = industries
	
class _1881(base):
	__tablename__ = "1881"
	org_num = Column(Integer, unique = True, index = True, primary_key = True)
	navn = Column(String, index = True)
	
	def __init__(self, org_num, navn):
		self.org_num = org_num
		self.navn = navn


#! OLD InputTable
# class InputTable(base):
# 	__tablename__ = "input_table"
# 	# org_num = Column(Integer, unique = True, index = True, primary_key = True)
# 	organisasjonsnummer = Column(Integer, unique = True, index = True, primary_key = True)
# 	navn = Column(String, index = True)
# 	postadresse = Column(String, index = True, nullable = True) #! maybe wrong parameter
# 	forretningsadresse = Column(String, index = True)

# 	def __init__(self, organisasjonsnummer, navn, postadresse, forretningsadresse):
# 		self.organisasjonsnummer = organisasjonsnummer
# 		self.navn = navn
# 		self.postadresse = postadresse
# 		self.forretningsadresse = forretningsadresse

#* NEW InputTable
from sqlalchemy.dialects import postgresql
class InputTable(base):
	__tablename__ = "input_table"
	organisasjonsnummer = Column(Integer, unique = True, index = True, primary_key = True)
	navn = Column(String, index = True)
	forretningsadresse = Column(postgresql.JSON, index = True)
	# postadresse = Column(String, index = True, nullable = True) #! maybe wrong parameter
	adresse_short = Column(String, index=True)
	postboks = Column(String, index=True)

	def __init__(self, organisasjonsnummer, navn, postadresse, forretningsadresse, adresse_short, postboks):
		self.organisasjonsnummer = organisasjonsnummer
		self.navn = navn
		# self.postadresse = postadresse
		self.forretningsadresse = forretningsadresse
		self.adresse_short = adresse_short
		self.postboks = postboks 








# class BrregTable(base):
# 	__tablename__ = "brreg_table"
# 	organisasjonsnummer = Column(Integer, unique = True, index = True, primary_key = True)
# 	navn = Column(String, index = True)
# 	konkurs = Column(Boolean(), index = True)
# 	underAvvikling = Column(Boolean(), index = True)
# 	underTvangsavviklingEllerTvangsopplosning = Column(Boolean(), index = True)
# 	postadresse = Column(String, index = True, nullable = True) #! maybe wrong parameter
# 	forretningsadresse = Column(String, index = True)



base.metadata.create_all(engine)




# class Google(base):
# 	__tablename__ = "gulesider"
# 	org_num = Column(Integer, unique = True, index = True, primary_key = True)
# 	navn = Column(String, index = True)
# 	tlf = Column(String, index = True)
	
# 	def __init__(self, org_num, navn, tlf):
# 		self.org_num = org_num
# 		self.navn = navn
# 		self.tlf = tlf
