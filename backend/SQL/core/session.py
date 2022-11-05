from typing import Generator
# from base import Base

# from core.config import settings #todo make this 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .base import Base
from ..config import Settings

# from base import Base


SQLALCHEMY_DATABASE_URL = Settings.DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

def create_tables():
    Base.metadata.create_all(bind = engine)

def getSession():
    #new session
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = SessionLocal()
    # session = sessionmaker(bind=db.engine)
    return session