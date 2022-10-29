from fastapi import Depends, Request
from fastapi import APIRouter
from psycopg2 import IntegrityError
from sqlalchemy.orm import Session



''' Local Imports '''
from schemas.users import UserCreate
from schemas.users import ShowUser
from db.session import get_db
from db.repository.users import create_new_user, delete_user_by_phone_number
from apis.version1.send_sms import Verification
router = APIRouter()

#! OLD user creation route
# @router.post("/", response_model = ShowUser)
# def create_user(user: UserCreate, db: Session = Depends(get_db)):
#     print(user)
#     user = create_new_user(user=user, db=db)
#     return user

'''
#> IDÉ
    (litt hack)
    create user som vanlig (inkl. tlf nummer) i tillegg til at den kjører send_verification_sms 
    men i stedenfor å bli redirektet til "account created",
    bir du istedenfor redirektet til "insert verification code"
    den venter på du skal skrive inn verification, og trykke på "OK" som;
    kjører en api call på "recieve_otp_code_async()" som vil sjekke og sette is_valid:
    is_valid==True: ingenting skjer, du blir redirektet til "account created"
        
    is_valid==False: [ALT 1] sender en feilmelding og sletter konto fra db, pop tilbake til signup page, hvor skjemaet er fortsatt fyllt ut (forhåpentligvis).
                     [ALT 2] sender en feilmelding og vil ikke sette is_active=True, og is_active vil være nødvendig for å kunne logge inn.
                     [ALT 3] sender en feilmelding som ber deg skrive inn på nytt.
'''

# #> ________________ TEST ________________
# @router.post("/", response_model = ShowUser)
# async def create_user(user:UserCreate, db: Session = Depends(get_db)):
#     try:
#         user = create_new_user(user = user, db = db)
#         return user 
#     except IntegrityError as e:
#         raise UnicornException(response_model=e)


# # #> _____________TEST _________________________________________________________________________________
# from fastapi.responses import JSONResponse

# class UnicornException(Exception):
#     def __init__(self, name: str):
#         self.name = name


# # @router.exception_handler(UnicornException)
# @router.exception_handler(UnicornException)
# async def unicorn_exception_handler(request: Request, exc: UnicornException):
#     return JSONResponse(
#         status_code=418,
#         content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
#     )

# # #> ___________________________________________________________________________________________________









''' test NEW user creation route ++ phone verification
'''
@router.post("/", response_model = ShowUser)
async def create_user(user:UserCreate, db: Session = Depends(get_db)):
    ''' NOTE:
        - did recieve verification sms
        - TypeError: object NoneType can't be used in 'await' expression:
            await send_sms_async(sms_to = user.telefon_nummer)
                "await Verification().requestVerification(phone_number = sms_to)" 
    '''
    # send_sms_async(sms_to = user.telefon_nummer)
    user = create_new_user(user = user, db = db)
    return user 


# send_otp_code_async(phone_number)
@router.get("/verification/phone/send_code") #link trenger email fra Frontend
async def send_otp_code_async(phone_number = None):
    Verification().requestVerification(phone_number = phone_number)
    return True
#     if await Verification().checkVerificationCode(otp_code, phone_number):
#         return True #Phone number was verified, redirecting to "account created"
#     else:
#         await delete_user(phone_number, db = db) 
#         return False, "Incorrect verification code, Account removed from db, please try again" #Error, Phone number NOT verified, redirecting to "message: error, account not created"

# def send_sms_async(sms_to:str):
    

@router.get("/verification/phone/recieve_code") #link trenger email fra Frontend
async def recieve_otp_code_async(phone_number = None, otp_code:str = None, db: Session = Depends(get_db)):
    
    if await Verification().checkVerificationCode(otp_code, phone_number):
        return True #Phone number was verified, redirecting to "account created"
    else:
        await delete_user(phone_number, db = db) 
        return False, "Incorrect verification code, Account removed from db, please try again" #Error, Phone number NOT verified, redirecting to "message: error, account not created"

async def delete_user(phone_number, db: Session):
    delete_user_by_phone_number(phone_number, db)

@router.get("/verification/search_for_user_in_db") #link trenger email fra Frontend
async def search_for_user_in_db(phone_number = None, otp_code:str = None, db: Session = Depends(get_db)):
    '''
    usage: used by APP to check if user data, e.g.: username, email, phone number already exsist in the system.  
    '''

    print()





