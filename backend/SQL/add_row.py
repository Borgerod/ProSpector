import SQL.db as db
from sqlalchemy.orm import sessionmaker

def getSession():
    #new session
    Session = sessionmaker(bind = db.engine)
    session = Session()
    return session
