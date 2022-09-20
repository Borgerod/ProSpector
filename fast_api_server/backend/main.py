from apis.base import api_router
from apis.utils import OAuth2PasswordBearerWithCookie
from apis.version1.route_login import get_current_user_from_token
from apis.version1.send_email import send_email_async

# from db.db.repository.call_list import getOverview
# from db.db.repository.call_list import getRowsBetween

from db.repository.call_list import getOverview, getCurrentCallList, getRowsBetween, updateCallListStatus, renewList
from db.repository.users import changePassword
# from db.repository.call_list import getRowsBetween

# from db.session import SessionLocal, get_db
from core.config import settings
from db.base import Base
from db.session import engine
from db.utils import check_db_connected
from db.utils import check_db_disconnected
from fastapi import FastAPI, Depends
# from webapps.base import api_router as web_app_router
from sqlalchemy.orm import Session
from db.session import get_db
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from fastapi import FastAPI, BackgroundTasks, UploadFile, File, Form
from starlette.responses import JSONResponse
from starlette.requests import Request
from fastapi_mail import FastMail, MessageSchema,ConnectionConfig
from pydantic import BaseModel, EmailStr
from typing import List

def include_router(app):
    app.include_router(api_router)
    # app.include_router(web_app_router)

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

@app.get("/RenewList")
async def renew_list(token: str = Depends(OAuth2PasswordBearerWithCookie(tokenUrl = "/login/token")), db: Session = Depends(get_db)):
    user = get_current_user_from_token(token, db)
    return renewList(db, user)

@app.get("/ResetPassword/Authentication")
async def send_email_asynchronous(email_to = None, verify_num = None):
    await send_email_async(email_to, verify_num)
    return 'Success'

@app.put("/ResetPassword")
async def post_email_auth():
    isAuth = True
    return isAuth

@app.get('/ResetPassword')
async def put_change_password(new_password = None, email = None, db: Session = Depends(get_db)):
    if email == None:
        try: 
            user = get_user( token=Depends(OAuth2PasswordBearerWithCookie(tokenUrl = "/login/token")), db=db)
            email = user.email    
        except:
            print("ResetPassword ERROR")
    return changePassword(new_password, email, db)


# @app.get("/ResetPassword")
# async def renew_list(email: str, db: Session):

    # return renewList(db, user)

# async def send_email_asynchronous(email = None, Session = Depends(get_db)):
    # user_emial = get_user_email(email, db)
    # if user_emial:
    #     subject, body = get_authentication_email()
    #     await send_email_async('Email Authentication',user_email=email)
    #     return 'Success'
    # else: 
    #     return 'Failiure'




# @app.get("/ResetPassword/AuthenticationBool")
# async def check_email_auth():
#     return isEmailAuthenticated()

# def isEmailAuthenticated():
#     isAuth = True
#     return isAuth


# def moredi():
#     callStatus = db.query(CallList).filter_by(org_num = org_num).first()
#     if callStatus.ringe_status:
#          callStatus.ringe_status = False
#     else:
#         callStatus.ringe_status = True
#     db.commit()

# class CallList(Base):
#     __tablename__ = "call_list"
#     org_num = Column(Integer, unique=True, index=True, primary_key=True)
#     navn = Column(String, index=True)
#     google_profil = Column(String, index=True)
#     eier_bekreftet = Column(Boolean(), index=True)
#     komplett_profil = Column(Boolean(), index=True)
#     ringe_status = Column(Boolean(), index=True)
#     liste_id = Column(Integer, index=True)



# class emailAuth(Base):
#     isAuth = False




# @app.post("/email")
# async def simple_send() -> JSONResponse:
#     # return await send_email_async()
#     await send_email_async('Hello World','someemail@gmail.com',
#         {'title': 'Hello World'})
#     return 'Success'



# @app.get('/email')
# async def send_email_asynchronous():
#     await send_email_async('Hello World', 'borgerod@hotmail.com')
#     return 'Success'

    # return await changePassword(new_password, email, db)


'''
aleksander@hotmail.com
Passord123
'''