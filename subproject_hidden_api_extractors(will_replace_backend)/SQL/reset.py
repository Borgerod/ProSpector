from sqlalchemy.orm import sessionmaker
from sqlalchemy import exc
# ___ local imports ___
import SQL.db as db


def getSession():
    return sessionmaker(bind = db.engine)()


class Reset:
    
    def proff(self):
        session = getSession()
        session.query(db.Proff).delete()
        session.commit()
    
    def gulesider(self):
        session = getSession()
        session.query(db.Gulesider).delete()
        session.commit()
    
    def _1881(self):
        session = getSession()
        # session.query(db.).delete()
        session.commit()
    
    def Industry1881(self):
        session = getSession()
        session.query(db.Industry1881).delete()
        session.commit()