# Nessasary for importing config 
import sys; sys.path.insert(0, '.')
from virtual_env.config import Config


class Settings:
    ''' A little bit redundant but im keeping it regardless
    '''
    config = Config.getPostgresConfig # Get Appropriate config variables 
    
    PROJECT_NAME: str = "ProSpector"
    PROJECT_VERSION: str = "1.0.0" #todo REMOVE THIS (could replace with func that finds real version)

    USE_SQLITE_DB: str = config["USE_SQLITE_DB"]
    POSTGRES_USER: str = config["POSTGRES_USER"]
    POSTGRES_PASSWORD = config["POSTGRES_PASSWORD"]
    # POSTGRES_USER: str = "postgres" #> TEMP
    # POSTGRES_USER: str = "mediavest" #> TEMP
    # POSTGRES_PASSWORD = "Orikkel1991" #> TEMP
    # POSTGRES_PASSWORD = "F%K6L51KXGXs" #> TEMP

    
    POSTGRES_SERVER: str = config["POSTGRES_SERVER"]#, "localhost",
    POSTGRES_PORT: str = config["POSTGRES_PORT"]#, 5432,
      # default postgres port is 5432
    POSTGRES_DB: str = config["POSTGRES_DB"]#, "tdd",
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

    SECRET_KEY: str = config["SECRET_KEY"]
    ALGORITHM = "HS256"
    # ACCESS_TOKEN_EXPIRE_MINUTES = 30  # in mins
    ACCESS_TOKEN_EXPIRE_MINUTES = 480  # in mins (8 hours)

    TEST_USER_EMAIL = "test@example.com"


settings = Settings()






# import os
# from pathlib import Path
# from dotenv import load_dotenv

# env_path = Path(".") / ".env"
# load_dotenv(dotenv_path = env_path)


# class Settings:
#     PROJECT_NAME: str = "ProSpector"
#     PROJECT_VERSION: str = "1.0.0"

#     USE_SQLITE_DB: str = os.getenv("USE_SQLITE_DB")
#     POSTGRES_USER: str = os.getenv("POSTGRES_USER")
#     POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
#     POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
#     POSTGRES_PORT: str = os.getenv(
#         "POSTGRES_PORT", 5432
#     )  # default postgres port is 5432
#     POSTGRES_DB: str = os.getenv("POSTGRES_DB", "tdd")
#     DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

#     SECRET_KEY: str = os.getenv("SECRET_KEY")
#     ALGORITHM = "HS256"
#     # ACCESS_TOKEN_EXPIRE_MINUTES = 30  # in mins
#     ACCESS_TOKEN_EXPIRE_MINUTES = 480  # in mins

#     TEST_USER_EMAIL = "test@example.com"


# settings = Settings()
