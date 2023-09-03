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

'''
sqlalchemy.exc.OperationalError: (psycopg2.OperationalError) could not translate host name "postgres" to address: Unknown host
'''

class Settings:
    def __init__(self):
        ''' sets settings-state to admin-settings if self.caller == Dev, else it keeps default settings (user-settings )'''
        self.POSTGRES_SERVER = "localhost"
        self.POSTGRES_PORT = os.environ["POSTGRES_PORT"]
        self.POSTGRES_DB = os.environ["POSTGRES_DB"] #(OR) self.POSTGRES_DB = "ProSpector_Dev"
        self.SECRET_KEY = os.environ["SECRET_KEY"]
        self.USE_SQLITE_DB = os.environ["USE_SQLITE_DB"]
        self.POSTGRES_USER = os.environ["POSTGRES_USER"] #(OR) self.POSTGRES_USER = "postgres" (OR) "mediavest"
        self.POSTGRES_PASSWORD = os.environ["POSTGRES_PASSWORD"]
        # TODO [ ]: os.environ["POSTGRES_PASSWORD"] should really not display password, make a encrypted password and make a decrypter
        #      TODO We might already have this implementation in the user the backend i think, implement it here also.  
        
        if self.caller == "Dev":
            self.POSTGRES_USER = "postgres"
            self.POSTGRES_PASSWORD = os.environ["POSTGRES_DEV_PASSWORD"]
        
        self.DATABASE_URL = f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    @property
    def caller(self):
        return sys._getframe(1).f_locals["self"].__class__.__name__

class Dev(Settings):
    def __init__(self) -> None:
        super().__init__()
    
    @property
    @staticmethod
    def engine(self) -> Engine:
        self.__init__()
        return create_engine(self.DATABASE_URL)
    
    @property
    def base(self) -> DeclarativeMeta:
        return declarative_base()
    
    @property
    def display_settings(self) -> None:
        print(
            "\n", "caller: ", self.caller,
    	    "\n",
            "\n", "POSTGRES_SERVER: ",self.POSTGRES_SERVER, 
            "\n", "POSTGRES_PORT: ",self.POSTGRES_PORT, 
            "\n", "POSTGRES_DB: ",self.POSTGRES_DB, 
            "\n", "SECRET_KEY: ",self.SECRET_KEY, 
            "\n", "USE_SQLITE_DB: ",self.USE_SQLITE_DB, 
            "\n", "POSTGRES_USER: ",self.POSTGRES_USER, 
            "\n","\n", "DATABASE_URL: ", self.DATABASE_URL, 
        )

class User(Settings):
    def __init__(self) -> None:
        super().__init__()
    
    @property
    def engine(self) -> Engine:
        return create_engine(self.DATABASE_URL)
    
    @property
    def base(self) -> DeclarativeMeta:
        return declarative_base()
    
    @property
    def display_settings(self) -> None:
        print(
            "\n", "caller: ", self.caller,
    	    "\n",
            "\n", "POSTGRES_SERVER: ",self.POSTGRES_SERVER, 
            "\n", "POSTGRES_PORT: ",self.POSTGRES_PORT, 
            "\n", "POSTGRES_DB: ",self.POSTGRES_DB, 
            "\n", "SECRET_KEY: ",self.SECRET_KEY, 
            "\n", "USE_SQLITE_DB: ",self.USE_SQLITE_DB, 
            "\n", "POSTGRES_USER: ",self.POSTGRES_USER, 
            "\n","\n", "DATABASE_URL: ", self.DATABASE_URL, 
        )
        

Dev = Dev()
User = User()






# class DevSettings:
#     def __init__(self) -> None:
#         self.POSTGRES_USER = "mediavest"	#TEMP while testing (env variables seems to be wrong)
#         # self.POSTGRES_USER = "postgres"	#TEMP while testing (env variables seems to be wrong)
#         # self.POSTGRES_USER = os.environ["POSTGRES_USER"] # TEMPORARLY DISABLED WHILE TESTING
#         # TEMP
#         ''' ___ Postgres ___ '''
#         self.POSTGRES_SERVER = "localhost"
#         self.POSTGRES_PORT = os.environ["POSTGRES_PORT"]
#         self.POSTGRES_DB = os.environ["POSTGRES_DB"] #(OR) self.POSTGRES_DB = "ProSpector_Dev"
#         self.SECRET_KEY = os.environ["SECRET_KEY"]
#         self.USE_SQLITE_DB = os.environ["USE_SQLITE_DB"]
#         self.POSTGRES_USER = os.environ["POSTGRES_USER"] #(OR) self.POSTGRES_USER = "postgres" (OR) "mediavest"
#         try:
#             self.POSTGRES_DEV_PASSWORD = os.environ["POSTGRES_DEV_PASSWORD"]
#         except:
#             print("Could not connect to Postgres, edit password in: ProSpector\backend\dev_backend\SQL\config.py")
#             """self.POSTGRES_DEV_PASSWORD ="Mitt personlige passord"""
#         # self.POSTGRES_SERVER = "localhost"
#         # self.POSTGRES_PORT = os.environ["POSTGRES_PORT"]
#         # # self.POSTGRES_DB = os.environ["POSTGRES_DB"]
#         # self.POSTGRES_DB = "ProSpector_Dev"
#         # self.SECRET_KEY = os.environ["SECRET_KEY"]
#         # self.USE_SQLITE_DB = os.environ["USE_SQLITE_DB"]
#         # self.DATABASE_URL = f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_DEV_PASSWORD}@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        
#         print(
#             "\n", "POSTGRES_SERVER: ",self.POSTGRES_SERVER, 
#             "\n", "POSTGRES_PORT: ",self.POSTGRES_PORT, 
#             "\n", "POSTGRES_DB: ",self.POSTGRES_DB, 
#             "\n", "SECRET_KEY: ",self.SECRET_KEY, 
#             "\n", "USE_SQLITE_DB: ",self.USE_SQLITE_DB, 
#             "\n", "POSTGRES_USER: ",self.POSTGRES_USER, 
#         )


#         # ''' ___ EMAIL ___ '''
#         # self.MAIL_FROM = os.environ["MAIL_FROM"]
#         # self.MAIL_PORT = os.environ["MAIL_PORT"]
#         # self.MAIL_SERVER = os.environ["MAIL_SERVER"]
#         # self.MAIL_FROM_NAME = os.environ["MAIL_SERVER"]
#         # self.MAIL_USERNAME = os.environ["MAIL_USERNAME"]
#         # self.MAIL_PASSWORD = os.environ["MAIL_PASSWORD"]
#         # # self.MAIL_TSL = os.environ["MAIL_TSL"]
#         # # self.MAIL_SSL = os.environ["MAIL_SSL"]
#         # self.MAIL_TSL = os.environ["MAIL_TSL"]
#         # self.MAIL_SSL = os.environ["MAIL_SSL"]
#         # self.USE_CREDENTIALS = os.environ["USE_CREDENTIALS"]	

#         # ''' ___ TWILIO ___ '''
#         # self.TWILIO_ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
#         # self.TWILIO_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
#         # self.VERIFY_SID = 'VA0af259d1f90eef02d4cfe86f45e64b8f'	

# class Dev(DevSettings):
#     def __init__(self) -> None:
#         super().__init__()
    
#     @property
#     def engine(self) -> Engine:
#         return create_engine(self.DATABASE_URL)
    
#     @property
#     def base(self) -> DeclarativeMeta:
#         return declarative_base()
        
#     '''	settings = DevSettings()
#         # settings.DATABASE_URL = 'postgresql://[postgres]/Orikkel1991@localhost:5432/ProSpector_Dev'
#         def getEngine(self) -> Engine:
#             return create_engine(settings.DATABASE_URL)

#         def getBase(self) -> DeclarativeMeta:
#             return declarative_base()
            
#         engine = create_engine(settings.DATABASE_URL)
#         base = declarative_base()
#     '''
# class Settings:   
#     def __init__(self, admin=False) -> None:
#         ''' gets admin-settings if admin=True, else gets user-settings '''
#         ''' ___ Postgres ___ '''
#         self.POSTGRES_SERVER = "localhost"
#         self.POSTGRES_PORT = os.environ["POSTGRES_PORT"]
#         self.POSTGRES_DB = os.environ["POSTGRES_DB"] #(OR) self.POSTGRES_DB = "ProSpector_Dev"
#         self.SECRET_KEY = os.environ["SECRET_KEY"]
#         self.USE_SQLITE_DB = os.environ["USE_SQLITE_DB"]
#         self.POSTGRES_USER = os.environ["POSTGRES_USER"] #(OR) self.POSTGRES_USER = "postgres" (OR) "mediavest"
    
#         if admin:
#         # ________________________________________ ADMIN SETTINGS ________________________________________
#         	''' ___ Postgres ___ '''
#         	self.POSTGRES_SERVER = "localhost"
#         	self.POSTGRES_PORT = os.environ["POSTGRES_PORT"]
#         	self.POSTGRES_DB = os.environ["POSTGRES_DB"] #(OR) self.POSTGRES_DB = "ProSpector_Dev"
#         	self.SECRET_KEY = os.environ["SECRET_KEY"]
#         	self.USE_SQLITE_DB = os.environ["USE_SQLITE_DB"]
#         	self.POSTGRES_USER = os.environ["POSTGRES_USER"] #(OR) self.POSTGRES_USER = "postgres" (OR) "mediavest"















#         # ________________________________________ USER SETTINGS ________________________________________
#         # self.POSTGRES_USER = "mediavest"	#TEMP while testing (env variables seems to be wrong)
#         self.POSTGRES_USER = os.environ["POSTGRES_USER"] # TEMPORARLY DISABLED WHILE TESTING
#         print(f"self.POSTGRES_USER: {self.POSTGRES_USER}")
#         self.POSTGRES_USER = "postgres"	#TEMP while testing (env variables seems to be wrong)
#         # self.POSTGRES_PASSWORD = os.environ["POSTGRES_PASSWORD"]
#         self.POSTGRES_SERVER = os.environ["POSTGRES_SERVER"]
#         ''' ___ Postgres ___ '''
#         self.POSTGRES_SERVER = "localhost"
#         self.POSTGRES_PORT = os.environ["POSTGRES_PORT"]
#         # self.POSTGRES_DB = os.environ["POSTGRES_DB"]
#         self.POSTGRES_DB = "ProSpector_Dev"
#         self.SECRET_KEY = os.environ["SECRET_KEY"]
#         self.POSTGRES_DB = os.environ["POSTGRES_DB"] #(OR) self.POSTGRES_DB = "ProSpector_Dev"
#         self.USE_SQLITE_DB = os.environ["USE_SQLITE_DB"]
#         # self.DATABASE_URL = f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

#         self.POSTGRES_USER = os.environ["POSTGRES_USER"] #(OR) self.POSTGRES_USER = "postgres" (OR) "mediavest"
#         try:
#         	self.POSTGRES_DEV_PASSWORD = os.environ["POSTGRES_DEV_PASSWORD"]
#         except:
#         	print("Could not connect to Postgres, edit password in: ProSpector\backend\dev_backend\SQL\config.py")
#         	"""self.POSTGRES_DEV_PASSWORD ="Mitt personlige passord"""
#         self.DATABASE_URL = f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_DEV_PASSWORD}@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

#         ''' ___ EMAIL ___ '''
#         self.MAIL_FROM = os.environ["MAIL_FROM"]
#         self.MAIL_PORT = os.environ["MAIL_PORT"]
#         self.MAIL_SERVER = os.environ["MAIL_SERVER"]
#         self.MAIL_FROM_NAME = os.environ["MAIL_SERVER"]
#         self.MAIL_USERNAME = os.environ["MAIL_USERNAME"]
#         self.MAIL_PASSWORD = os.environ["MAIL_PASSWORD"]
#         # self.MAIL_TSL = os.environ["MAIL_TSL"]
#         # self.MAIL_SSL = os.environ["MAIL_SSL"]
#         self.MAIL_TSL = os.environ["MAIL_TSL"]
#         self.MAIL_SSL = os.environ["MAIL_SSL"]
#         self.USE_CREDENTIALS = os.environ["USE_CREDENTIALS"]	

#         ''' ___ TWILIO ___ '''
#         self.TWILIO_ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
#         self.TWILIO_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
#         self.VERIFY_SID = 'VA0af259d1f90eef02d4cfe86f45e64b8f'
#         self.VERIFY_SID = 'VA0af259d1f90eef02d4cfe86f45e64b8f'	

#     @property
#     def getMailConnection(self) -> FastMail:
#         '''
#         returns a connection to FastMail, -> fm = FastMail(conf)

#         NOTE: mail config is a bit weird; 
#         sometimes it asks for MAIL_STARTTLS & MAIL_SSL_TLS, 
#         other times it asks for MAIL_TLS & MAIL_SSL.
#         Instead of fixing it, i will just handle it, bite me. 
#         '''
#         try:
#             conf = ConnectionConfig(
#                     MAIL_USERNAME = self.MAIL_USERNAME,
#                     MAIL_PASSWORD = self.MAIL_PASSWORD,
#                     MAIL_FROM = self.MAIL_FROM,
#                     MAIL_PORT = self.MAIL_PORT,
#                     MAIL_SERVER = self.MAIL_SERVER,
#                     MAIL_FROM_NAME = self.MAIL_FROM_NAME,
#                     MAIL_STARTTLS = True, #! sometimes fastapi_mail requires this, sometimes the other 
#                     MAIL_SSL_TLS = False, #! sometimes fastapi_mail requires this, sometimes the other 
#                     USE_CREDENTIALS = True,
#                     VALIDATE_CERTS = True
#                 )
#         except:
#             conf = ConnectionConfig(
#                 MAIL_USERNAME = self.MAIL_USERNAME,
#                 MAIL_PASSWORD = self.MAIL_PASSWORD,
#                 MAIL_FROM = self.MAIL_FROM,
#                 MAIL_PORT = self.MAIL_PORT,
#                 MAIL_SERVER = self.MAIL_SERVER,
#                 MAIL_FROM_NAME = self.MAIL_FROM_NAME,
#                 MAIL_TLS = True,  #* sometimes fastapi_mail requires this, sometimes the other 
#                 MAIL_SSL = False, #* sometimes fastapi_mail requires this, sometimes the other 
#                 USE_CREDENTIALS = True,
#                 VALIDATE_CERTS = True
#             )
#         return FastMail(conf) # fm 

# class User:
    
#     @property
#     def engine(self) -> Engine:
#         return create_engine(Settings().DATABASE_URL)
    
#     @property
#     def base(self) -> DeclarativeMeta:
#         return declarative_base()
        


# # load_dotenv()
# # settings = Settings()

# # def getEngine() -> Engine:
# # 	return create_engine(settings.DATABASE_URL)

# # def getBase() -> DeclarativeMeta:
# # 	return declarative_base()

# # engine = create_engine(settings.DATABASE_URL)
# # base = declarative_base()
