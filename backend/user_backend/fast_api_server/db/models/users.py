from sqlalchemy import Date
from db.base_class import Base
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

class User(Base):
    id = Column(Integer, primary_key=True, nullable=False, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    org =  Column(String, nullable=False, index=True) #workplace
    phone_number = Column(String, unique=True, nullable=False, index=True)
