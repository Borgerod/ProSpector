from fastapi import Depends
from fastapi import APIRouter
from sqlalchemy.orm import Session


''' Local Imports '''
from schemas.users import UserCreate
from schemas.users import ShowUser
from db.session import get_db
from db.repository.users import create_new_user, delete_user_by_phone_number
from apis.version1.send_sms import Verification

router = APIRouter()

@router.post("/", response_model = ShowUser)
async def create_user(user:UserCreate, db: Session = Depends(get_db)):
    ''' NOTE:
        - did recieve verification sms
        - TypeError: object NoneType can't be used in 'await' expression:
            await send_sms_async(sms_to = user.telefon_nummer)
                "await Verification().requestVerification(phone_number = sms_to)" 
    '''
    send_otp_code_async(phone_number = user.telefon_nummer)
    user = create_new_user(user = user, db = db)
    return user 


@router.get("/verification/phone/send_code") #link trenger email fra Frontend
async def send_otp_code_async(phone_number = None):
    verify_sid = Verification().requestVerification(phone_number = phone_number)
    return verify_sid


@router.get("/verification/phone/recieve_code") #link trenger email fra Frontend
async def recieve_otp_code_async(verify_sid = None,  phone_number = None, otp_code:str = None, db: Session = Depends(get_db)):
    
    if await Verification().checkVerificationCode(verify_sid, otp_code, phone_number):
        return Verification().verify_sid
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





