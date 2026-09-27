import os
import sys
from pathlib import Path

import psycopg
import pytest
from dotenv import dotenv_values

# backend/.env is the only config source; its values override machine-wide
# env vars, and the database is a throwaway one.
BACKEND = Path(__file__).resolve().parents[2]
os.environ.update({k: v for k, v in dotenv_values(BACKEND / ".env").items() if v is not None})
os.environ["POSTGRES_DB"] = "prospector_test"
sys.path.insert(0, str(BACKEND / "user_backend" / "fast_api_server"))
sys.path.insert(0, str(BACKEND / "dev_backend"))

with psycopg.connect(host = os.environ["POSTGRES_SERVER"], port = os.environ["POSTGRES_PORT"],
                     user = os.environ["POSTGRES_USER"], password = os.environ["POSTGRES_PASSWORD"],
                     dbname = "postgres", autocommit = True) as conn:
    if not conn.execute("SELECT 1 FROM pg_database WHERE datname = 'prospector_test'").fetchone():
        conn.execute("CREATE DATABASE prospector_test")

from db.base import Base  # noqa: E402
from db.session import engine  # noqa: E402


@pytest.fixture
def db_engine():
    Base.metadata.drop_all(bind = engine)
    Base.metadata.create_all(bind = engine)
    return engine
