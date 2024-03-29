from sqlalchemy import Column, String, Integer, Boolean
# from sqlalchemy.dialects import postgresql
from sqlalchemy.dialects.postgresql import JSON as Json

''' ___ local imports ___ '''
# from SQL.config import engine, base
from SQL.config import Dev as dev
from SQL.config import User as user

engine = dev.engine
base = dev.base

# engine =  create_engine('postgresql://[mediavest]/F%K6L51KXGXs@localhost:5432/ProSpector_Dev')
# mediavest
# F%K6L51KXGXs
# postgres
# Orikkel1991

base.metadata.create_all(engine)

class IndustryGulesider(base):
	''' Industries used by Gulesider
	'''
	__tablename__ = "gulesider_industries"
	industries = Column(String, unique = True, index = True, primary_key = True)

	def __init__(self, industries):
		self.industries = industries

class Gulesider(base):
	__tablename__ = "gulesider"
	org_num = Column(Integer, unique = True, index = True, primary_key = True)
	name = Column(String, index = True)
	tlf = Column(String, index = True)
	is_premium = Column(Boolean, index = True) 
	
	def __init__(self, org_num, name, is_premium, tlf):
		self.org_num = org_num
		self.name = name
		self.tlf = tlf
		self.is_premium = is_premium

class IndustryProff(base):
	''' Industries used by Proff
	'''
	__tablename__ = "proff_industries"
	industries = Column(String, unique = True, index = True, primary_key = True)

	def __init__(self, industries):
		self.industries = industries

class Proff(base):
	__tablename__ = "proff"
	org_num = Column(Integer, unique = True, index = True, primary_key = True)
	name = Column(String, index = True)
	
	def __init__(self, org_num, name, tlf):
		self.org_num = org_num
		self.name = name
		self.tlf = tlf

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
	name = Column(String, index = True)
	
	def __init__(self, org_num, name, tlf):
		self.org_num = org_num
		self.name = name
		self.tlf = tlf 

class Google(base):
	__tablename__ = "Google"
	org_num = Column(Integer, unique = True, index = True, primary_key = True)
	name = Column(String, index = True)
	# loc = Column(Json, index = True)
	loc = Column(String, index = True)
	
	def __init__(self, org_num, name, loc):
		self.org_num = org_num
		self.name = name	
		self.loc = loc 

class InputTable(base):
	__tablename__ = "input_table"
	org_num = Column(Integer, unique = True, index = True, primary_key = True)
	name = Column(String, index = True)
	# loc = Column(String, index = True) 
	loc = Column(Json, index = True)  #> Testing if this work (did work for Google, these should be equal)

	def __init__(self, org_num, name, loc,) -> None: #postadresse) -> None:
		self.org_num = org_num
		self.name = name
		self.loc = loc


# TODO: [x] implement Phone numbers and add to Call List.
class CallList(base):
	engine = dev.engine
	base = dev.base
	__tablename__ = 'call_list'
	__table_args__ = {'extend_existing': True}

	org_num = Column(Integer, unique=True, index=True, primary_key=True)
	name = Column(String, index=True)
	tlf = Column(String, index=True)
	google_profil = Column(String, index=True)
	eier_bekreftet = Column(Boolean(), index=True)
	komplett_profil = Column(Boolean(), index=True)
	ringe_status = Column(Boolean(), index=True)
	link_til_profil = Column(String, index=True)
  
	def __init__(self, org_num, name, google_profil, eier_bekreftet, komplett_profil, ringe_status, link_til_profil, tlf) -> None:
		self.org_num = org_num
		self.name = name
		self.tlf = tlf
		self.google_profil = google_profil
		self.eier_bekreftet = eier_bekreftet
		self.komplett_profil = komplett_profil
		self.ringe_status = ringe_status
		self.link_til_profil = link_til_profil 

#> TEMP WHILE TESTING
class CallListTest(base):
	engine = dev.engine
	base = dev.base
	__tablename__ = 'call_list_test'
	__table_args__ = {'extend_existing': True}

	org_num = Column(Integer, unique=True, index=True, primary_key=True)
	name = Column(String, index=True)
	google_profil = Column(String, index=True)
	eier_bekreftet = Column(Boolean(), index=True)
	komplett_profil = Column(Boolean(), index=True)
	ringe_status = Column(Boolean(), index=True)
	link_til_profil = Column(String, index=True)
  
	def __init__(self, org_num, name, google_profil, eier_bekreftet, komplett_profil, ringe_status, link_til_profil) -> None:
		self.org_num = org_num
		self.name = name
		self.google_profil = google_profil
		self.eier_bekreftet = eier_bekreftet
		self.komplett_profil = komplett_profil
		self.ringe_status = ringe_status
		self.link_til_profil = link_til_profil 






