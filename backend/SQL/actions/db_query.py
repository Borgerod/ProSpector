import json
import pandas as pd
import SQL.db as db
from SQL.add_row import getSession
from sqlalchemy import  create_engine, Column, String, Integer, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from SQL.config import settings
from models.input_table import InputTable
from models.brreg_table import BrregTable
from core.session import get_db

#! REMOVE THIS
session = getSession()
engine = create_engine(settings.DATABASE_URL)

def getCallList():
	''' simple get function for call_list
	'''
	return pd.read_sql_table(
		'call_list',
		con = engine
		)

def getCallListTest():
	''' simple get function for call_list_test
	'''
	return pd.read_sql_table(
		'call_list_test',
		con = engine
		)

class Table:
	def __init__(self, tablename) -> None:
		self.tablename = tablename

	async def getTableFromName(self, tablename, _row):
		match await tablename:
			case ['input_table']:
				return await db.InputTable(_row)

			case ['brreg_table']:
				return await db.BrregTable(_row) 

			# case ['1881_output_table']:
			# 	return await db.I88ITable(_row) 

			# case ['gulesider_output_table']:
			# 	return await db.GulesiderOutputTable(_row) 	

			# case ['gulesider_table']:
			# 	return await db.GulesiderTable(_row) 

			# case ['proff_output_table']:
			# 	return await db.ProffTable(_row) 
			
			case ['call_list']:
				return await db.CallList(_row) 

			# case ['google_input_table']:
			# 	return await db.CallList(_row) 

			case ['update_tracker']:
				return await db.UpdateTracker(_row) 

	async def addRowToTable(self, _row, session):
		row = await self.getTableFromName(self.tablename, _row)
		await session.add(row)
		await session.commit()

	async def getRowByOrgNum(self, org_num: str, session) -> json: #i think its json
		return await session.query(self.tablename).filter(self.tablename.org_num == org_num).first()
	
	
	def addRowToDb(self, row, session) -> str:
		'''
			will [a] try to add row to db, 
			  or [b] replace row if "a" was unsuccsessfull.
		'''
		try:
			session.add(row)
			session.commit()
		except:
			session.rollback()
			session.query(db.CallListTest).filter_by(org_num = self.org_num).delete()

