from fastapi import FastAPI,  Depends

from fastapi_mail import FastMail, MessageSchema,ConnectionConfig
from sqlalchemy.orm import Session
from mangum import Mangum 


''' Local Imports '''
from core.config import settings
from db.base import Base
from db.session import get_db, engine
from db.repository.users import changePassword
from db.repository.call_list import getOverview, getCurrentCallList, getRowsBetween, updateCallListStatus, renewList
from db.utils import check_db_disconnected, check_db_connected
from apis.version1.route_login import get_current_user_from_token
from apis.version1.send_email import send_email_async
from apis.utils import OAuth2PasswordBearerWithCookie
from apis.base import api_router

TOKEN_URL = "/login/token"

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
handler = Mangum(app)

@app.on_event("startup")
async def app_startup():
    await check_db_connected()

@app.on_event("shutdown")
async def app_shutdown():
    await check_db_disconnected()

@app.get("/callList")
def get_limited_call_list(skip: int = 0, limit: int = 40, db: Session = Depends(get_db)):    
    return getRowsBetween(db, skip, limit)

@app.get("/currentcallList")
def get_call_list(token: str = Depends(OAuth2PasswordBearerWithCookie(TOKEN_URL)), db: Session = Depends(get_db)):
    user = get_current_user_from_token(token, db)
    return getCurrentCallList(db, user)

@app.get("/overView")
def get_overview(token: str = Depends(OAuth2PasswordBearerWithCookie(TOKEN_URL)), db: Session = Depends(get_db)):
    user = get_current_user_from_token(token, db)
    overview = getOverview(db, user)
    return overview

@app.get("/ShowUser")
def get_user( token: str = Depends(OAuth2PasswordBearerWithCookie(TOKEN_URL)), db: Session = Depends(get_db)):
    user = get_current_user_from_token(token, db)
    return user

@app.put("/callList/ringe_status")
async def update_item(org_num: int, db: Session = Depends(get_db)):
    return updateCallListStatus(db, org_num)

@app.get("/RenewList")
async def renew_list(token: str = Depends(OAuth2PasswordBearerWithCookie(TOKEN_URL)), db: Session = Depends(get_db)):
    user = get_current_user_from_token(token, db)
    return renewList(db, user)

@app.get("/ResetPassword/Authentication")
async def send_email_asynchronous(email_to = None, verify_num = None):
    await send_email_async(email_to, verify_num)
    return 'Success'

@app.put("/ResetPassword")
async def post_email_auth():
    is_auth = True
    return is_auth

@app.get('/ResetPassword')
async def put_change_password(new_password = None, email = None, db: Session = Depends(get_db)):
    if email == None:
        try: 
            user = get_user( token = Depends(OAuth2PasswordBearerWithCookie(TOKEN_URL)), db = db)
            email = user.email    
        except:
            print("ResetPassword ERROR")
    return changePassword(new_password, email, db)
