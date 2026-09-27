from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

# backend/.env, shared with dev_backend
ENV_FILE = Path(__file__).resolve().parents[3] / ".env"


class Settings(BaseSettings):
    ''' Reads every value from env vars or backend/.env.
        A missing required value fails at startup with its name.
    '''
    model_config = SettingsConfigDict(env_file = ENV_FILE, extra = "ignore")

    PROJECT_NAME: str = "ProSpector"
    PROJECT_VERSION: str

    USE_SQLITE_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_SERVER: str
    POSTGRES_PORT: int
    POSTGRES_DB: str

    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 480  # in mins (8 hours)

    MAIL_USERNAME: str
    MAIL_PASSWORD: str
    MAIL_FROM: str
    MAIL_PORT: int
    MAIL_SERVER: str
    MAIL_FROM_NAME: str
    MAIL_STARTTLS: bool
    MAIL_SSL_TLS: bool
    USE_CREDENTIALS: bool

    TWILIO_ACCOUNT_SID: str
    TWILIO_AUTH_TOKEN: str

    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"


settings = Settings()
