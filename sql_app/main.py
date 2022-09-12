# from fastapi import Depends, FastAPI, HTTPException
# from sqlalchemy.orm import Session

# from sql_app import crud, models, schemas
# from sql_app.database import SessionLocal, engine, Base

# '''
#     activation command:
#         uvicorn sql_app.main:app
#         uvicorn sql_app.main:app --reload

#     close command:
#         ctrl+c
# '''

# Base.metadata.create_all(bind=engine)

# app = FastAPI()

# # Dependency
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @app.get("/callList/")
# def get_callList(skip: int = 0, limit: int = 100, token: str = None, db: Session = Depends(get_db)):
#     if token != "493802fjn9v24mucrf9+8q23u4jr98x+43":
#         return "Error"

#     users = crud.getRowsBetween(db, skip, limit)
#     return users

# # response_model=list[validation_schema.CallListBase]

# @app.post("/users/{user_id}/items/", response_model=schemas.Item)
# def create_item_for_user(
#     user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
# ):
#     return crud.create_user_item(db=db, item=item, user_id=user_id)












from fastapi import Depends, FastAPI, HTTPException
from sql_app import crud
from sql_app.core.config import Settings
from sql_app.apis.general_pages.route_homepage import general_pages_router
from sql_app.db.base import Base      # now import Base from db.base not db.base_class
from sql_app.db.session import SessionLocal, engine, get_db
from sql_app.apis.base import api_router #new

# from core.config import Settings
# from apis.general_pages.route_homepage import general_pages_router
# from db.base import Base      # now import Base from db.base not db.base_class
# from db.session import engine
# from apis.base import api_router #new


def include_router(app):   
	app.include_router(api_router) #modified

def start_application():
	app = FastAPI(title=Settings.PROJECT_NAME,version=Settings.PROJECT_VERSION)
	include_router(app)
	return app 

def create_tables():
	print("create_tables")
	Base.metadata.create_all(bind=engine)

app = start_application()

# @app.get("/callList/")
# def get_callList(skip: int = 0, limit: int = 100, token: str = None, db: SessionLocal = Depends(get_db)):
#     # if token != "493802fjn9v24mucrf9+8q23u4jr98x+43":
#     #     return "Error"

#     call_list = crud.getRowsBetween(db, skip, limit)
#     return call_list




'''
make virtual enviourment:
    python -m venv env

activate env:
    .\env\Scripts\activate

initialise git:
    git init


set execuytionPolicy:
	Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted

'''