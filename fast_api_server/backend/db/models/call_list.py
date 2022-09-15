from sqlalchemy import Boolean, Column, Integer, String
from db.base_class import Base


class CallList(Base):
	__tablename__ = "call_list"
	org_num = Column(Integer, unique=True, index=True, primary_key=True)
	navn = Column(String, index=True)
	google_profil = Column(String, index=True)
	eier_bekreftet = Column(Boolean(), index=True)
	komplett_profil = Column(Boolean(), index=True)
	ringe_status = Column(Boolean(), index=True)
	liste_id = Column(Integer, index=True)

class CallListOverview(Base):
	__tablename__ = "call_list_overview_mediavest"
	liste_id = Column(Integer, unique=True, index=True, primary_key=True)
	liste_start = Column(Integer, unique=True, index=True)
	liste_limit = Column(Integer, unique=True, index=True)
	kunde_id = Column(String, unique=True, index=True)
	er_ledig = Column(Boolean(), default=True, index=True)
	er_ferdig = Column(Boolean(), default=False, index=True)
