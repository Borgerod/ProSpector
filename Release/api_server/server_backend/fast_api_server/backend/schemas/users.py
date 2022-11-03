from pydantic import BaseModel
from pydantic import EmailStr

class UserCreate(BaseModel):
    brukernavn: str
    epost: EmailStr
    passord: str
    organisasjon: str

class ShowUser(BaseModel):
    username: str
    email: EmailStr
    is_active: bool
    org: str

    class Config:  # to convert non dict obj to json
        orm_mode = True
  