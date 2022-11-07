import os
import sys
from typing import Generator
from dotenv import load_dotenv
from sqlalchemy import create_engine
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from fastapi_mail import ConnectionConfig, FastMail  # See NOTE
sys.path.insert(0, '.') #? Not sure if needed

from sqlalchemy.engine.base import Engine  #for annotation
from sqlalchemy.orm.decl_api import DeclarativeMeta #for annotation


''' NOTE fastapi_mail:
	some small (harmless) errors originates fastapi_mail;
		No module named 'aioredis'
		No module named 'httpx'
'''


class DevSettings:
	def __init__(self) -> None:
		# self.POSTGRES_USER = "mediavest"	#TEMP while testing (env variables seems to be wrong)
		self.POSTGRES_USER = "postgres"	#TEMP while testing (env variables seems to be wrong)
		# self.POSTGRES_USER = os.environ["POSTGRES_USER"] # TEMPORARLY DISABLED WHILE TESTING
		# TEMP
		try:
			self.POSTGRES_DEV_PASSWORD = os.environ["POSTGRES_DEV_PASSWORD"]
		except:
			self.POSTGRES_DEV_PASSWORD ="Orikkel1991"

		self.POSTGRES_SERVER = "localhost"
		self.POSTGRES_PORT = os.environ["POSTGRES_PORT"]
		# self.POSTGRES_DB = os.environ["POSTGRES_DB"]
		self.POSTGRES_DB = "ProSpector_Dev"
		self.SECRET_KEY = os.environ["SECRET_KEY"]
		self.USE_SQLITE_DB = os.environ["USE_SQLITE_DB"]
		self.DATABASE_URL = f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_DEV_PASSWORD}@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

		self.MAIL_FROM = os.environ["MAIL_FROM"]
		self.MAIL_PORT = os.environ["MAIL_PORT"]
		self.MAIL_SERVER = os.environ["MAIL_SERVER"]
		self.MAIL_FROM_NAME = os.environ["MAIL_SERVER"]
		self.MAIL_USERNAME = os.environ["MAIL_USERNAME"]
		self.MAIL_PASSWORD = os.environ["MAIL_PASSWORD"]
		# self.MAIL_TSL = os.environ["MAIL_TSL"]
		# self.MAIL_SSL = os.environ["MAIL_SSL"]
		self.MAIL_TSL = os.environ["MAIL_TSL"]
		self.MAIL_SSL = os.environ["MAIL_SSL"]
		self.USE_CREDENTIALS = os.environ["USE_CREDENTIALS"]	
		self.TWILIO_ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
		self.TWILIO_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
		self.VERIFY_SID = 'VA0af259d1f90eef02d4cfe86f45e64b8f'	

class Dev:
	settings = DevSettings()

	def getEngine(self) -> Engine:
		return create_engine(settings.DATABASE_URL)

	def getBase(self) -> DeclarativeMeta:
		return declarative_base()
		
	engine = create_engine(settings.DATABASE_URL)
	base = declarative_base()




class Settings:   
	def __init__(self) -> None:
		# self.POSTGRES_USER = "mediavest"	#TEMP while testing (env variables seems to be wrong)
		self.POSTGRES_USER = "postgres"	#TEMP while testing (env variables seems to be wrong)
		# self.POSTGRES_USER = os.environ["POSTGRES_USER"] # TEMPORARLY DISABLED WHILE TESTING
		self.POSTGRES_PASSWORD = os.environ["POSTGRES_PASSWORD"]
		self.POSTGRES_SERVER = os.environ["POSTGRES_SERVER"]
		self.POSTGRES_PORT = os.environ["POSTGRES_PORT"]
		# self.POSTGRES_DB = os.environ["POSTGRES_DB"]
		self.POSTGRES_DB = "ProSpector_Dev"
		self.SECRET_KEY = os.environ["SECRET_KEY"]
		self.USE_SQLITE_DB = os.environ["USE_SQLITE_DB"]
		self.DATABASE_URL = f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

		self.MAIL_FROM = os.environ["MAIL_FROM"]
		self.MAIL_PORT = os.environ["MAIL_PORT"]
		self.MAIL_SERVER = os.environ["MAIL_SERVER"]
		self.MAIL_FROM_NAME = os.environ["MAIL_SERVER"]
		self.MAIL_USERNAME = os.environ["MAIL_USERNAME"]
		self.MAIL_PASSWORD = os.environ["MAIL_PASSWORD"]
		# self.MAIL_TSL = os.environ["MAIL_TSL"]
		# self.MAIL_SSL = os.environ["MAIL_SSL"]
		self.MAIL_TSL = os.environ["MAIL_TSL"]
		self.MAIL_SSL = os.environ["MAIL_SSL"]
		self.USE_CREDENTIALS = os.environ["USE_CREDENTIALS"]	
		self.TWILIO_ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
		self.TWILIO_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
		self.VERIFY_SID = 'VA0af259d1f90eef02d4cfe86f45e64b8f'

	@property
	def getMailConnection(self) -> FastMail:
		'''
		returns a connection to FastMail, -> fm = FastMail(conf)

		NOTE: mail config is a bit weird; 
		sometimes it asks for MAIL_STARTTLS & MAIL_SSL_TLS, 
		other times it asks for MAIL_TLS & MAIL_SSL.
		Instead of fixing it, i will just handle it, bite me. 
		'''
		try:
			conf = ConnectionConfig(
					MAIL_USERNAME = self.MAIL_USERNAME,
					MAIL_PASSWORD = self.MAIL_PASSWORD,
					MAIL_FROM = self.MAIL_FROM,
					MAIL_PORT = self.MAIL_PORT,
					MAIL_SERVER = self.MAIL_SERVER,
					MAIL_FROM_NAME = self.MAIL_FROM_NAME,
					MAIL_STARTTLS = True, #! sometimes fastapi_mail requires this, sometimes the other 
					MAIL_SSL_TLS = False, #! sometimes fastapi_mail requires this, sometimes the other 
					USE_CREDENTIALS = True,
					VALIDATE_CERTS = True
				)
		except:
			conf = ConnectionConfig(
				MAIL_USERNAME = self.MAIL_USERNAME,
				MAIL_PASSWORD = self.MAIL_PASSWORD,
				MAIL_FROM = self.MAIL_FROM,
				MAIL_PORT = self.MAIL_PORT,
				MAIL_SERVER = self.MAIL_SERVER,
				MAIL_FROM_NAME = self.MAIL_FROM_NAME,
				MAIL_TLS = True,  #* sometimes fastapi_mail requires this, sometimes the other 
				MAIL_SSL = False, #* sometimes fastapi_mail requires this, sometimes the other 
				USE_CREDENTIALS = True,
				VALIDATE_CERTS = True
			)
		return FastMail(conf) # fm 
	
	
	# TEMPORARLY DISABLED WHILE TESTING (MIGHT BE REMOVED)
	# @property
	# def getPostgresConnection(self) -> Generator: # <-TEMP
	# 	'''
	# 	returns a connection to Postgres Server, -> db 
	# 	'''
	# 	engine = create_engine(self.DATABASE_URL)
	# 	SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)
	# 	try:
	# 		db = SessionLocal()
	# 		yield db
	# 	finally:
	# 		db.close()

	# @property
	# def getBase(self) -> declarative_base:
	# 	return declarative_base()

load_dotenv()
settings = Settings()

def getEngine() -> Engine:
	return create_engine(settings.DATABASE_URL)

def getBase() -> DeclarativeMeta:
	return declarative_base()


engine = create_engine(settings.DATABASE_URL)
base = declarative_base()
