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
	tlf = Column(String, index = True)
	
	def __init__(self, org_num, navn, tlf):
		self.org_num = org_num
		self.navn = navn
		self.tlf = tlf

# class Proff(base):
# 	__tablename__ = "gulesider"
# 	org_num = Column(Integer, unique = True, index = True, primary_key = True)
# 	navn = Column(String, index = True)
# 	tlf = Column(String, index = True)
	
# 	def __init__(self, org_num, navn, tlf):
# 		self.org_num = org_num
# 		self.navn = navn
# 		self.tlf = tlf

class Industry(base):
	''' Industries used by Proff
	'''
	__tablename__ = "industries"
	industries = Column(String, unique = True, index = True, primary_key = True)

	def __init__(self, industries):
		self.industries = industries
	





# class I88I(base):
# 	__tablename__ = "1881"
# 	org_num = Column(Integer, unique = True, index = True, primary_key = True)
# 	navn = Column(String, index = True)
# 	tlf = Column(String, index = True)
	
# 	def __init__(self, org_num, navn, tlf):
# 		self.org_num = org_num
# 		self.navn = navn
# 		self.tlf = tlf


# class BrregTable(base):
# 	''' NOTE: #todo [ ] burde kanskje bytte om navnene for consistancy!! 
# 	'''
# 	__tablename__ = "brreg_table"
# 	organisasjonsnummer = Column(Integer, unique = True, index = True, primary_key = True)
# 	navn = Column(String, index = True)
# 	konkurs = Column(Boolean(), index = True)
# 	underAvvikling = Column(Boolean(), index = True)
# 	underTvangsavviklingEllerTvangsopplosning = Column(Boolean(), index = True)
# 	postadresse = Column(String, index = True, nullable = True) #! maybe wrong parameter
# 	forretningsadresse = Column(String, index = True)

# class InputTable(base):
# 	__tablename__ = "input_table"
# 	org_num = Column(Integer, unique = True, index = True, primary_key = True)
# 	navn = Column(String, index = True)
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