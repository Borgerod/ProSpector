from phonenumbers import PhoneNumber
from pydantic import BaseModel
from pydantic import EmailStr
# from pydantic import PhoneNumber

class UserCreate(BaseModel):
    brukername: str
    epost: EmailStr
    passord: str
    organisasjon: str
    telefon_nummer: str

class ShowUser(BaseModel):
    username: str
    email: EmailStr
    is_active: bool
    org: str

    class Config:  # to convert non dict obj to json
        orm_mode = True
  