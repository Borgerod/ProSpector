import os
from dotenv import load_dotenv

class Config:
	def __init__(self) -> None:
		self.POSTGRES_USER = os.environ["POSTGRES_USER"]
		self.POSTGRES_PASSWORD = os.environ["POSTGRES_PASSWORD"]
		self.POSTGRES_SERVER = os.environ["POSTGRES_SERVER"]
		self.POSTGRES_PORT = os.environ["POSTGRES_PORT"]
		self.POSTGRES_DB = os.environ["POSTGRES_DB"]
		self.SECRET_KEY = os.environ["SECRET_KEY"]
		self.USE_SQLITE_DB = os.environ["USE_SQLITE_DB"]
	
		self.MAIL_FROM = os.environ["MAIL_FROM"]
		self.MAIL_PORT = os.environ["MAIL_PORT"]
		self.MAIL_SERVER = os.environ["MAIL_SERVER"]
		self.MAIL_FROM_NAME = os.environ["MAIL_SERVER"]
		self.MAIL_USERNAME = os.environ["MAIL_USERNAME"]
		self.MAIL_PASSWORD = os.environ["MAIL_PASSWORD"]
		self.MAIL_TSL = os.environ["MAIL_TSL"]
		self.MAIL_SSL = os.environ["MAIL_SSL"]
		self.USE_CREDENTIALS = os.environ["USE_CREDENTIALS"]
	
		self.account_sid = os.environ['TWILIO_ACCOUNT_SID']
		self.auth_token = os.environ['TWILIO_AUTH_TOKEN']
		self.verify_sid = 'VA0af259d1f90eef02d4cfe86f45e64b8f'

	@property
	def getFullConfig(self):
		return self.__dict__

	@property
	def getPhoneConfig(self):
		return {
		"account_sid" : self.account_sid,
		"auth_token" : self.auth_token,
		"verify_sid" : self.verify_sid,
		}

	@property
	def getEmailConfig(self):
		return {
		"MAIL_FROM" : self.MAIL_FROM,
		"MAIL_PORT" : self.MAIL_PORT,
		"MAIL_SERVER" : self.MAIL_SERVER,
		"MAIL_FROM_NAME" : self.MAIL_FROM_NAME ,
		"MAIL_USERNAME" : self.MAIL_USERNAME ,
		"MAIL_PASSWORD" : self.MAIL_PASSWORD ,
		"MAIL_TSL" : self.MAIL_TSL ,
		"MAIL_SSL" : self.MAIL_SSL,
		"USE_CREDENTIALS" : self.USE_CREDENTIALS,
		}

	@property
	def getPostgresConfig(self):
		return {
		"POSTGRES_USER" : self.POSTGRES_USER,
		"POSTGRES_PASSWORD" : self.POSTGRES_PASSWORD ,
		"POSTGRES_SERVER" : self.POSTGRES_SERVER ,
		"POSTGRES_PORT" : self.POSTGRES_PORT ,
		"POSTGRES_DB" : self.POSTGRES_DB ,
		"SECRET_KEY" : self.SECRET_KEY,
		"USE_SQLITE_DB" : self.USE_SQLITE_DB,
		}
	
load_dotenv()
Config = Config()
# print(Config.getPhoneConfig)
# print(Config.getEmailConfig)
# print(Config.getPostgresConfig)




# if __name__ == "__main__":
# 	load_dotenv()
# 	Config = Config()


