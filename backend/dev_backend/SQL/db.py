from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.dialects import postgresql

# ___ local imports ___
from SQL.config import engine, base
from SQL.config import Dev as dev
from SQL.config import User as user

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
	
	def __init__(self, org_num, navn, tlf):
		self.org_num = org_num
		self.navn = navn
		self.tlf = tlf

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
	
	def __init__(self, org_num, navn, tlf):
		self.org_num = org_num
		self.navn = navn
		self.tlf = tlf 

class Google(base):
	__tablename__ = "Google"
	org_num = Column(Integer, unique = True, index = True, primary_key = True)
	name = Column(String, index = True)
	# loc = Column(postgresql.JSON, index = True)
	loc = Column(String, index = True)
	
	def __init__(self, org_num, name, loc):
		self.org_num = org_num
		self.name = name	
		self.loc = loc 

class InputTable(base):
	__tablename__ = "input_table"
	organisasjonsnummer = Column(Integer, unique = True, index = True, primary_key = True)
	navn = Column(String, index = True)
	forretningsadresse = Column(postgresql.JSON, index = True)
	# postadresse = Column(String, index = True, nullable = True) #! maybe wrong parameter
	adresse_short = Column(String, index=True)
	postboks = Column(String, index=True)

	def __init__(self, organisasjonsnummer, navn, forretningsadresse, adresse_short, postboks, ) -> None:#postadresse) -> None:
		self.organisasjonsnummer = organisasjonsnummer
		self.navn = navn
		# self.postadresse = postadresse
		self.forretningsadresse = forretningsadresse
		self.adresse_short = adresse_short
		self.postboks = postboks 

# TODO: [x] implement Phone numbers and add to Call List.
class CallList(base):
	engine = dev.engine
	base = dev.base
	__tablename__ = 'call_list'
	__table_args__ = {'extend_existing': True}

	org_num = Column(Integer, unique=True, index=True, primary_key=True)
	navn = Column(String, index=True)
	tlf = Column(String, index=True)
	google_profil = Column(String, index=True)
	eier_bekreftet = Column(Boolean(), index=True)
	komplett_profil = Column(Boolean(), index=True)
	ringe_status = Column(Boolean(), index=True)
	link_til_profil = Column(String, index=True)
  
	def __init__(self, org_num, navn, google_profil, eier_bekreftet, komplett_profil, ringe_status, link_til_profil, tlf) -> None:
		self.org_num = org_num
		self.navn = navn
		self.tlf = tlf
		self.google_profil = google_profil
		self.eier_bekreftet = eier_bekreftet
		self.komplett_profil = komplett_profil
		self.ringe_status = ringe_status
		self.link_til_profil = link_til_profil 
		# self.liste_id = ringe_status


#> TEMP WHILE TESTING
class CallListTest(base):
	engine = dev.engine
	base = dev.base
	__tablename__ = 'call_list_test'
	__table_args__ = {'extend_existing': True}

	org_num = Column(Integer, unique=True, index=True, primary_key=True)
	navn = Column(String, index=True)
	google_profil = Column(String, index=True)
	eier_bekreftet = Column(Boolean(), index=True)
	komplett_profil = Column(Boolean(), index=True)
	ringe_status = Column(Boolean(), index=True)
	link_til_profil = Column(String, index=True)
  
	def __init__(self, org_num, navn, google_profil, eier_bekreftet, komplett_profil, ringe_status, link_til_profil) -> None:
		self.org_num = org_num
		self.navn = navn
		self.google_profil = google_profil
		self.eier_bekreftet = eier_bekreftet
		self.komplett_profil = komplett_profil
		self.ringe_status = ringe_status
		self.link_til_profil = link_til_profil 




base.metadata.create_all(engine)



