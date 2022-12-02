from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import sessionmaker
from sqlalchemy import exc
import pandas as pd 
import numpy as np 


# ___ local imports ___
import SQL.db as db


def getSession() -> None:
	# Create new Session
	Session = sessionmaker(bind = db.engine)
	# session = Session()
	return Session()
# # Create new Session
# Session = sessionmaker(bind = db.engine)
# session = Session()

# class Insert:

class ErrorCounter:
	def __init__(self) -> None:
		self.org_num = 0000
		self.tlf = 0000
		self.navn = 0000

	def getCount(self, item):
		if item =='org_num':
			return 404+self.org_num
		if item =='tlf':
			return 404+self.tlf
		if item =='navn':
			return 404+self.navn

	def increase(self, item):
		if item =='org_num':
			self.org_num += 1
		if item =='tlf':
			self.tlf += 1
		if item =='navn':
			self.navn += 1
	@property 
	def resetCounters(self):
		self.org_num = 0000
		self.tlf = 0000
		self.navn = 0000

	# @property    
	# def getOrgNum(self):
	# 	return self.org_num

class Insert:
	ErrorCounter = ErrorCounter()

	def __init__(self) -> None:
		self.session = self.getSession()		

	def getSession(self) -> None:
		return sessionmaker(bind = db.engine)()

	def tryCommit(self, row:db) -> None:
		self.session.add(row) 
		try:
			self.session.commit()
		except exc.IntegrityError:
			self.session.rollback()  
	
	def tryGetData(self, item) -> int or str:
		try:
			match item:
				case 'org_num':
					return self.data['organisationNumber']
				case 'navn':
					return self.data['name']
				case 'tlf':
					return self.data['phones'][0]['number']   
		except KeyError:
			ErrorCounter.increase(item)
			return ErrorCounter.getCount(item)
			
	def toGulesider(self, data:list) -> None:
		'''
		takes a list of data from page, splits it, then inserts it into db
		'''
		self.data = data
		row = db.Gulesider(
			org_num = self.tryGetData('org_num'),
			navn = self.tryGetData('navn'),
			tlf = self.tryGetData('tlf'),
			is_premium = data['hitType'] == 'premium',
		)
		self.tryCommit(row)

	def toCategories(self, data:str) -> None:
		'''
		takes a list of data from page, splits it, then inserts it into db
		'''
		row = db.Categories(
			data,
		)
		self.tryCommit(row)

	def to1881Industries(self, data:str) -> None:
		'''
		takes a list of data from page, splits it, then inserts it into db
		'''
		row = db.Industry1881(
			data,
		)
		self.tryCommit(row)

	def toProffIndustries(self, data:str) -> None:
		'''
		takes data from page, splits it, then inserts it into db
		'''
		row = db.IndustryProff(
			data,
		)
		self.tryCommit(row)

	def toProff(self, org_num, navn, tlf) -> None:
			'''
			takes a list of data from page, splits it, then inserts it into db
			'''
			row = db.Proff(
				org_num,
				navn,
				tlf
			)
			self.tryCommit(row)
		  
	def to1881(self, org_num, navn, tlf) -> None:
		'''
		takes a list of data from page, splits it, then inserts it into db
		'''
		row = db._1881(
			org_num,
			navn,
			tlf
		)
		self.tryCommit(row)

	def toGoogle(self, array:np.ndarray) -> None:
		'''
		inserts generated list and inserts it into googleInputTable
		'''
		
		for data in array:
			row = db.Google(
			data[0], #org_num   
			data[1], #name
			data[2], #loc        
			)
			self.tryCommit(row)
		#     session.add(row) 
		# try:
		#     session.commit()
		# except exc.IntegrityError:
		#     session.rollback()  
	
	def toInputTable(self, array:np.ndarray) -> None:
		# df:pd.DataFrame[int, str, JSON] ) -> None:
		# org_num:int, navn:str, forretningsadresse:JSON
		'''
		#TODO: make description
		'''
		row = db.InputTable(
			array[0], # organisasjonsnummer
			array[1], # navn
			array[2], # forretningsadresse
		)
		self.tryCommit(row) 

	def toCallList(self, data:np.ndarray ) -> None:
	# def toCallList( self, org_num:int, navn:str, tlf:str,
					# google_profil:str, eier_bekreftet:bool, komplett_profil:bool, 
					# ringe_status:bool, link_til_profil:str,
					# ) -> None:
		'''
		Used by google.py inserts output into AWS db
		'''
		row = db.CallList(
			data['org_num'],
			data['navn'],
			data['tlf'],
			data['google_profil'],
			data['eier_bekreftet'],
			data['komplett_profil'],
			data['ringe_status'],
			data['link_til_profil'],
		)
		self.tryCommit(row)





