from sqlalchemy.orm import Session

import models, schemas


def getRowsBetween(db: Session, start: int, limit: int):
    return db.query(models.CallList).offset(start).limit(limit).all()

