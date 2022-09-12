from typing import Optional
from pydantic import BaseModel,EmailStr


class CallListBase(BaseModel):
    org_num: int | None = None
    navn: str | None = None
    google_profil: bool | None = None
    eier_erklært: bool | None = None
    komplett_profil: bool | None = None

class Token(BaseModel):
    access_token: str
    token_type: str


#properties required during user creation
class UserCreate(BaseModel):
    username: str
    email : EmailStr
    password : str