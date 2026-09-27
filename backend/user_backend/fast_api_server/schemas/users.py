from phonenumbers import PhoneNumber
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import field_validator
from core.hashing import MAX_PASSWORD_BYTES
# from pydantic import PhoneNumber

class UserCreate(BaseModel):
    brukername: str
    epost: EmailStr
    passord: str
    organisasjon: str
    telefon_nummer: str

    @field_validator("passord")
    @classmethod
    def passord_fits_bcrypt(cls, value: str) -> str:
        if len(value.encode()) > MAX_PASSWORD_BYTES:
            raise ValueError(f"passord is longer than {MAX_PASSWORD_BYTES} bytes")
        return value

class ShowUser(BaseModel):
    username: str
    email: EmailStr
    is_active: bool
    org: str

    class Config:  # to convert non dict obj to json
        orm_mode = True
  