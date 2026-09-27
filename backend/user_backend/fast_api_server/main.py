from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from apis.version1.send_email import send_email_async

''' Local Imports '''
from core.config import settings
from db.base import Base
from db.session import get_db, engine
from db.repository.users import changePassword, get_user_by_email
from db.repository.password_reset import create_reset_code, use_reset_code
from schemas.users import ShowUser, PasswordResetRequest
from db.repository.call_list import getOverview, getCurrentCallList, getRowsBetween, updateCallListStatus, renewList
from db.utils import check_db_disconnected, check_db_connected
from apis.version1.route_login import get_current_user_from_token
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

@app.on_event("startup")
async def app_startup():
    await check_db_connected()

@app.on_event("shutdown")
async def app_shutdown():
    await check_db_disconnected()

@app.get("/callList")
def get_limited_call_list(skip: int = 0, limit: int = 40, token: str = Depends(OAuth2PasswordBearerWithCookie(TOKEN_URL)), db: Session = Depends(get_db)):
    get_current_user_from_token(token, db)
    return getRowsBetween(db, skip, limit)

@app.get("/currentcallList")
def get_call_list(token: str = Depends(OAuth2PasswordBearerWithCookie(TOKEN_URL)), db: Session = Depends(get_db)):
    user = get_current_user_from_token(token, db)
    return getCurrentCallList(db, user)

@app.put("/callList/ringe_status")
async def update_item(org_num: int, token: str = Depends(OAuth2PasswordBearerWithCookie(TOKEN_URL)), db: Session = Depends(get_db)):
    user = get_current_user_from_token(token, db)
    if not updateCallListStatus(db, org_num, user):
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "org_num is not in your current call list")

@app.get("/RenewList")
async def renew_list(token: str = Depends(OAuth2PasswordBearerWithCookie(TOKEN_URL)), db: Session = Depends(get_db)):
    user = get_current_user_from_token(token, db)
    return renewList(db, user)

@app.get("/overView")
def get_overview(token: str = Depends(OAuth2PasswordBearerWithCookie(TOKEN_URL)), db: Session = Depends(get_db)):
    user = get_current_user_from_token(token, db)
    overview = getOverview(db, user)
    return overview

@app.get("/ShowUser", response_model = ShowUser)
def get_user( token: str = Depends(OAuth2PasswordBearerWithCookie(TOKEN_URL)), db: Session = Depends(get_db)):
    user = get_current_user_from_token(token, db)
    return user

@app.get("/ResetPassword/Authentication")
async def send_reset_code(email_to: str, db: Session = Depends(get_db)):
    ''' Emails a reset code, generated and checked here on the server.
        Same answer whether or not the email has an account, so it cannot be used to probe for users.
    '''
    if get_user_by_email(email_to, db):
        await send_email_async(email_to, create_reset_code(email_to, db))
    return 'Success'

@app.put("/ResetPassword")
async def reset_password(request: PasswordResetRequest, db: Session = Depends(get_db)):
    if not use_reset_code(request.email, request.verify_num, db):
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = "Invalid or expired verification code")
    return changePassword(request.new_password, request.email, db)
