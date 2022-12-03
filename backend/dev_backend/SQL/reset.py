from sqlalchemy.orm import sessionmaker

''' ___ local imports ___ '''
import SQL.db as db


def getSession():
    return sessionmaker(bind = db.engine)()


class Reset:
    
    def brreg(self):
        session = getSession()
        # TODO: [ ] Make BrregTable
        session.query(db.BrregTable).delete()
        session.commit()

    def inputTable(self):
        session = getSession()
        session.query(db.InputTable).delete()
        session.commit()

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
        session.query(db._1881).delete()
        session.commit()
    
    def Industry1881(self):
        session = getSession()
        session.query(db.Industry1881).delete()
        session.commit()

    def industryGulesider(self):
        session = getSession()
        session.query(db.IndustryGulesider).delete()
        session.commit()

    def IndustryProff(self):
        session = getSession()
        session.query(db.IndustryProff).delete()
        session.commit()