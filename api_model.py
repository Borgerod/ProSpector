from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from api_centre import Base


class CallList(Base):
    __tablename__ = "google_output_table"

    # id = Column(Integer, primary_key=True, index=True)
    org_num = Column(Integer, unique=True, index=True, primary_key=True)
    navn = Column(String, unique=False, index=True)
    google_profil = Column(Boolean, unique=False, index=True)
    eier_erklært = Column(Boolean, unique=False, index=True)
    komplett_profil = Column(Boolean, unique=False, index=True)




'''
    todo:
        kunde_id   liste_id 
'''



