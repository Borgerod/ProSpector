from pydantic import BaseModel


class CallListBase(BaseModel):
    org_num: int | None = None
    navn: str | None = None
    google_profil: bool | None = None
    eier_erklært: bool | None = None
    komplett_profil: bool | None = None

