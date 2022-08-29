from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from sql_app import crud, models, schemas
from sql_app.database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

# from sql_app import database
# database.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/callList/")
def get_callList(skip: int = 0, limit: int = 100, token: str = None, db: Session = Depends(get_db)):
    if token != "493802fjn9v24mucrf9+8q23u4jr98x+43":
        return "Error"

    users = crud.getRowsBetween(db, skip, limit)
    return users

# response_model=list[validation_schema.CallListBase]

# @app.post("/users/{user_id}/items/", response_model=schemas.Item)
# def create_item_for_user(
#     user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
# ):
#     return crud.create_user_item(db=db, item=item, user_id=user_id)




