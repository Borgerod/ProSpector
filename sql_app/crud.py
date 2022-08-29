from sqlalchemy.orm import Session

from sql_app import models, schemas


def getRowsBetween(db: Session, start: int, limit: int):
    return db.query(models.CallList).offset(start).limit(limit).all()

