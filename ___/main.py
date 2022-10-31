from fastapi import FastAPI,  Depends, Request

from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from psycopg2 import IntegrityError
from requests import delete
from sqlalchemy.orm import Session

from schemas.users import ShowUser, UserCreate
from apis.version1.send_email import send_email_async

#! TEMPORARLY DISABLED EMAIL 

''' Local Imports '''
from core.config import settings
from db.base import Base
from db.session import get_db, engine
from db.repository.users import changePassword, create_new_user
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
def get_limited_call_list(skip: int = 0, limit: int = 40, db: Session = Depends(get_db)):    
    return getRowsBetween(db, skip, limit)

@app.get("/currentcallList")
def get_call_list(token: str = Depends(OAuth2PasswordBearerWithCookie(TOKEN_URL)), db: Session = Depends(get_db)):
    user = get_current_user_from_token(token, db)
    return getCurrentCallList(db, user)

@app.put("/callList/ringe_status")
async def update_item(org_num: int, db: Session = Depends(get_db)):
    return updateCallListStatus(db, org_num)

@app.get("/RenewList")
async def renew_list(token: str = Depends(OAuth2PasswordBearerWithCookie(TOKEN_URL)), db: Session = Depends(get_db)):
    user = get_current_user_from_token(token, db)
    return renewList(db, user)

@app.get("/overView")
def get_overview(token: str = Depends(OAuth2PasswordBearerWithCookie(TOKEN_URL)), db: Session = Depends(get_db)):
    user = get_current_user_from_token(token, db)
    overview = getOverview(db, user)
    return overview

@app.get("/ShowUser")
def get_user( token: str = Depends(OAuth2PasswordBearerWithCookie(TOKEN_URL)), db: Session = Depends(get_db)):
    user = get_current_user_from_token(token, db)
    return user

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


# #> _____________New API: phone_verification _____________

@app.post("/verification/phone/recieve_code")
async def recieve_otp_code_async(otp_code:str = None):
    '''
    gets otp_code from user input (in app)
    '''
    return otp_code

@app.get("/verification/phone/send_code")
async def send_otp_code_async(phone_number:str = None):
    '''
    gets otp_code from user input (in app)
    '''
    return phone_number

# @app.delete("/users/{email}")
# async def delete_user(email: str, db: Session):
#     delete_user_by_email(email, db)




# # NOTE: litt usikker på om det skal være get / put / post
# @app.get("/verification/phone/send_verification")
# async def send_sms_asynchronous(sms_to = None):
#     '''
#     send sms to user to verify phone number
#     '''
#     await send_sms_async(sms_to)
#     return 'Pending'

# @app.get("/verification/phone/send_verification")
# async def put_change_password(phone_number = None, otp_code = None, db: Session = Depends(get_db)):
#     '''
#     send sms with otp_code to user, for verifying phone number
#     '''
#     await send_sms_async(sms_to, otp_code)
#     return 'Success'


# # NOTE: litt usikker på om det skal være get / put / post
# @app.post("/verification/phone/recieve_code")
# async def recieve_otp_code_asynchronous(phone_number = None, otp_code = None):
#     '''
#     gets otp_code from user input (in app)
#     '''
#     # await recieve_otp_code_async(sms_to = None, otp_code = None)
#     is_valid = await Verification().checkVerificationCode(otp_code = None)
#     if is_valid:
#        await create_new_user_asynchronous()
#         create_user(user: UserCreate, db: Session = Depends(get_db)):


#     # return 'Success'


# @app.post("/users/user_creation")
# async def create_new_user_asynchronous():
#      create_user(user: UserCreate, db: Session = Depends(get_db)):




# # #> _____________TEST _________________________________________________________________________________
# from fastapi.responses import JSONResponse



# # @router.exception_handler(UnicornException)
# @app.exception_handler(UnicornException)
# async def unicorn_exception_handler(request: Request, exc: UnicornException):
#     return JSONResponse(
#         status_code=418,
#         content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
#     )


# ''' test NEW user creation route ++ phone verification
# '''
# @app.post("/", response_model = ShowUser)
# async def create_user(user:UserCreate, db: Session = Depends(get_db)):
#     try:
#         user = create_new_user(user = user, db = db)
#         return user 
#     except IntegrityError as e:
#         raise UnicornException(response_model=e)




# # #> ___________________________________________________________________________________________________

