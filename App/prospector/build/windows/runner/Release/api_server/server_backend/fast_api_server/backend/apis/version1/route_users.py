from fastapi import Depends
from fastapi import APIRouter
from sqlalchemy.orm import Session
from apis.version1.send_sms import Verification

''' Local Imports '''
from schemas.users import UserCreate
from schemas.users import ShowUser
from db.session import get_db
from db.repository.users import create_new_user, delete_user_by_phone_number

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

#> test NEW user creation route ++ phone verification
@router.post("/", response_model = ShowUser)
async def create_user(user:UserCreate, db: Session = Depends(get_db)):
    ''' NOTE:
        - did recieve verification sms
        - TypeError: object NoneType can't be used in 'await' expression:
            await send_sms_async(sms_to = user.telefon_nummer)
                "await Verification().requestVerification(phone_number = sms_to)" 
    '''
    send_sms_async(sms_to = user.telefon_nummer)
    user = create_new_user(user = user, db = db)
    return user 

def send_sms_async(sms_to:str):
    Verification().requestVerification(phone_number = sms_to)

@router.get("/verification/phone/recieve_code") #link trenger email fra Frontend
async def recieve_otp_code_async(phone_number = None, otp_code:str = None, db: Session = Depends(get_db)):
    
    if await Verification().checkVerificationCode(otp_code, phone_number):
        return True #Phone number was verified, redirecting to "account created"
    else:
        await delete_user(phone_number, db = db) 
        return False, "Incorrect verification code, Account removed from db, please try again" #Error, Phone number NOT verified, redirecting to "message: error, account not created"

async def delete_user(phone_number, db: Session):
    delete_user_by_phone_number(phone_number, db)
