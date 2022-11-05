from sqlalchemy import  create_engine, Column, String, Integer, Boolean
from SQL.config import settings
from core.base import Base

class BrregTable(Base):
	''' NOTE: #todo [ ] burde kanskje bytte om navnene for consistancy!! 
	'''
	__tablename__ = "brreg_table"
	organisasjonsnummer = Column(Integer, unique = True, index = True, primary_key = True)
	navn = Column(String, index = True)
	konkurs = Column(Boolean(), index = True)
	underAvvikling = Column(Boolean(), index = True)
	underTvangsavviklingEllerTvangsopplosning = Column(Boolean(), index = True)
	postadresse = Column(String, index = True, nullable = True) #! maybe wrong parameter
	forretningsadresse = Column(String, index = True)
