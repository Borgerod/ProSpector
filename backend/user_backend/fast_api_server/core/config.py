''' Nessasary for importing config ''' 
import sys; sys.path.insert(0, '.')
from virtual_env.config import Config


class Settings:
    ''' A little bit redundant but im keeping it regardless
    '''
    config = Config.getPostgresConfig # Get Appropriate config variables 
    PROJECT_NAME: str = "ProSpector"
    USE_SQLITE_DB: str = config["USE_SQLITE_DB"]
    POSTGRES_USER = "postgres" #(OR) POSTGRES_USER: str = config["POSTGRES_USER"] 
    POSTGRES_PASSWORD = config["POSTGRES_PASSWORD"]
    POSTGRES_SERVER: str = config["POSTGRES_SERVER"] #(OR), "localhost",
    POSTGRES_PORT: str = config["POSTGRES_PORT"] #(OR), 5432, ''' default postgres port is 5432 '''
    POSTGRES_DB: str = config["POSTGRES_DB"]  #(OR), "tdd",
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 480  # in mins (8 hours)

settings = Settings()
