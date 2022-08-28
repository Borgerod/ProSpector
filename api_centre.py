# from django.db import models 





''' TODO __________________________
	- [ ] generate api keys on AWS
	- [ ] store api keys on a PG table (if AWS doesnt handle it by itself)
	- [ ] create verification code for API keys to gatekeep API-calls (if AWS doesnt handle it by itself)
	- [ ] create functions for API-actions
'''
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import payload
from postgres import parseConfig


dbname, host, user, password = parseConfig()

SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{user}:{password}@{host}:5432/{dbname}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
