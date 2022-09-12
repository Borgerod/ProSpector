from sqlalchemy.orm import Session

# from sql_app import schemas
import sql_app.schemas
# import schemas
from sql_app.db.models.call_list import CallList

# from sql_app.db.models import call_list


def getRowsBetween(db: Session, start: int, limit: int):
    return db.query(CallList).offset(start).limit(limit).all()
    # return db.query(sql_app.db.models.models.CallList).offset(start).limit(limit).all()

