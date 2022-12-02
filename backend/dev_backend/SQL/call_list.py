# from tutorial: https://www.youtube.com/watch?v=NuDSWGOcvtg&ab_channel=DATAnnosaurus
# TODO: Test removing this file 

from sqlalchemy import  create_engine, Column, String, Integer, Boolean
from SQL.config import settings
from core.base import Base

from sqlalchemy.orm import sessionmaker

'''
Has two Models based on argument; testmode (bool):
	- CallList
	- CallListTest
'''

class CallList(Base):
	__tablename__ = 'call_list'
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
		# self.liste_id = ringe_status


class CallListTest(Base):
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

# base.metadata.create_all(engine)