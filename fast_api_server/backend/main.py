''' External imports '''
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends

''' Local imports '''
from apis.version1.route_login import get_current_user_from_token
from apis.utils import OAuth2PasswordBearerWithCookie
from apis.base import api_router
from db.repository.call_list import getOverview, getCurrentCallList, getRowsBetween, updateCallListStatus
from db.utils import check_db_disconnected
from db.utils import check_db_connected
from db.session import engine
from db.session import get_db
from db.base import Base
from core.config import settings


def include_router(app):
    app.include_router(api_router)

def create_tables():
    Base.metadata.create_all(bind = engine)


def start_application():
    app = FastAPI(title = settings.PROJECT_NAME, version = settings.PROJECT_VERSION)
    include_router(app)
    create_tables()
    return app

app = start_application()


@app.on_event("startup")
async def app_startup():
    await check_db_connected()

@app.on_event("shutdown")
async def app_shutdown():
    await check_db_disconnected()

@app.get("/callList")
def get_callList(skip: int = 0, limit: int = 40, token: str = None, db: Session = Depends(get_db)):    
    return getRowsBetween(db, skip, limit)

@app.get("/currentcallList")
def get_callList(token: str = Depends(OAuth2PasswordBearerWithCookie(tokenUrl = "/login/token")), db: Session = Depends(get_db)):
    user = get_current_user_from_token(token, db)
    return getCurrentCallList(db, user)

@app.get("/overView")
def get_overview(token: str = Depends(OAuth2PasswordBearerWithCookie(tokenUrl = "/login/token")), db: Session = Depends(get_db)):
    user = get_current_user_from_token(token, db)
    overview = getOverview(db, user)
    return overview

@app.get("/ShowUser")
def get_user( token: str = Depends(OAuth2PasswordBearerWithCookie(tokenUrl = "/login/token")), db: Session = Depends(get_db)):
    user = get_current_user_from_token(token, db)
    return user

@app.put("/callList/ringe_status")
async def update_item(org_num: int, db: Session = Depends(get_db)):
    return updateCallListStatus(db, org_num)





