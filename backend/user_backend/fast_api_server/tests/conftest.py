import os
from pathlib import Path

import psycopg
import pytest
from dotenv import dotenv_values

# backend/.env is the only config source for tests. Its values override
# any machine-wide env vars, and the database is a throwaway one.
ENV_FILE = Path(__file__).resolve().parents[3] / ".env"
os.environ.update({k: v for k, v in dotenv_values(ENV_FILE).items() if v is not None})
os.environ["POSTGRES_DB"] = "prospector_test"


def _admin_connection():
    return psycopg.connect(
        host = os.environ["POSTGRES_SERVER"],
        port = os.environ["POSTGRES_PORT"],
        user = os.environ["POSTGRES_USER"],
        password = os.environ["POSTGRES_PASSWORD"],
        dbname = "postgres",
        autocommit = True,
    )


with _admin_connection() as conn:
    if not conn.execute("SELECT 1 FROM pg_database WHERE datname = 'prospector_test'").fetchone():
        conn.execute("CREATE DATABASE prospector_test")


from fastapi.testclient import TestClient  # noqa: E402  (after env is set)

import main  # noqa: E402
from db.base import Base  # noqa: E402
from db.session import SessionLocal, engine  # noqa: E402
from db.models.call_list import CallList, CallListOverview  # noqa: E402


@pytest.fixture(autouse = True)
def clean_db():
    Base.metadata.drop_all(bind = engine)
    Base.metadata.create_all(bind = engine)
    yield


@pytest.fixture
def db():
    session = SessionLocal()
    yield session
    session.close()


@pytest.fixture
def client():
    with TestClient(main.app) as test_client:
        yield test_client


@pytest.fixture
def fake_sms(monkeypatch):
    ''' Replaces Twilio; live SMS sends cost money. '''
    calls = []

    class FakeVerification:
        verify_sid = "VA_test"

        def requestVerification(self, phone_number):
            calls.append(("send", phone_number))
            return self.verify_sid

        async def checkVerificationCode(self, verify_sid, otp_code, phone_number):
            calls.append(("check", phone_number, otp_code))
            return otp_code == "123456"

    from apis.version1 import route_users
    monkeypatch.setattr(route_users, "Verification", FakeVerification)
    return calls


@pytest.fixture
def fake_email(monkeypatch):
    sent = []

    async def fake_send(email_to, verify_num):
        sent.append((email_to, verify_num))

    monkeypatch.setattr(main, "send_email_async", fake_send)
    return sent


NEW_USER = {
    "brukername": "tester",
    "epost": "tester@example.com",
    "passord": "secret-password",
    "organisasjon": "ProSpector",
    "telefon_nummer": "+4799999999",
}


@pytest.fixture
def user(client, fake_sms):
    response = client.post("/users/", json = NEW_USER)
    assert response.status_code == 200, response.text
    return NEW_USER


@pytest.fixture
def logged_in(client, user):
    response = client.post("/login/token", data = {"username": user["epost"], "password": user["passord"]})
    assert response.status_code == 200, response.text
    return client


@pytest.fixture
def call_list(db):
    db.add(CallListOverview(liste_id = 1, liste_start = 0, liste_limit = 2, er_ledig = True, er_ferdig = False))
    db.add_all([
        CallList(org_num = 111, name = "Firma A", ringe_status = False, liste_id = 1),
        CallList(org_num = 222, name = "Firma B", ringe_status = False, liste_id = 1),
    ])
    db.commit()
