from tests.conftest import NEW_USER


def test_create_user_returns_public_fields(client, fake_sms):
    response = client.post("/users/", json = NEW_USER)
    assert response.status_code == 200, response.text
    body = response.json()
    assert body["email"] == NEW_USER["epost"]
    assert "hashed_password" not in body


def test_create_user_sends_verification_sms(client, fake_sms):
    client.post("/users/", json = NEW_USER)
    assert ("send", NEW_USER["telefon_nummer"]) in fake_sms


def test_create_user_rejects_too_long_password(client, fake_sms):
    response = client.post("/users/", json = {**NEW_USER, "passord": "x" * 73})
    assert response.status_code == 422


def test_send_code(client, fake_sms):
    response = client.get("/users/verification/phone/send_code", params = {"phone_number": "+4799999999"})
    assert response.status_code == 200
    assert response.json() == "VA_test"


def test_receive_code_correct(client, user, fake_sms):
    response = client.get("/users/verification/phone/recieve_code",
                          params = {"verify_sid": "VA_test", "phone_number": user["telefon_nummer"], "otp_code": "123456"})
    assert response.status_code == 200
    assert response.json() == "VA_test"
