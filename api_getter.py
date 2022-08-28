from sqlalchemy.orm import Session

import api_model, validation_schema


def getRowsBetween(db: Session, start: int, limit: int):
    return db.query(api_model.CallList).offset(start).limit(limit).all()

