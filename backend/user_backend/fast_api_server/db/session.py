from typing import Generator

from core.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# psycopg (v3) driver; SQLAlchemy 2.1 needs it named for postgresql URLs
SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL.replace("postgresql://", "postgresql+psycopg://", 1)
engine = create_engine(SQLALCHEMY_DATABASE_URL)


SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
