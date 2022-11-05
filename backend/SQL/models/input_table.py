from sqlalchemy import  create_engine, Column, String, Integer, Boolean
from SQL.config import settings
from core.base import Base

class InputTable(Base):
	__tablename__ = "input_table"
	org_num = Column(Integer, unique = True, index = True, primary_key = True)
	navn = Column(String, index = True)
	postadresse = Column(String, index = True, nullable = True) #! maybe wrong parameter
	forretningsadresse = Column(String, index = True)
