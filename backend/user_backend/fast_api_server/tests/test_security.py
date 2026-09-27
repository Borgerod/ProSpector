from tests.conftest import NEW_USER


def test_show_user_hides_password_hash(logged_in):
    body = logged_in.get("/ShowUser").json()
    assert body["email"] == NEW_USER["epost"]
    assert "hashed_password" not in body


def test_call_list_needs_login(client, call_list):
    assert client.get("/callList").status_code == 401
    assert client.put("/callList/ringe_status", params = {"org_num": 111}).status_code == 401


def test_ringe_status_only_for_own_list(logged_in, call_list, db):
    from db.models.call_list import CallList
    db.add(CallList(org_num = 333, name = "Other list", ringe_status = False, liste_id = 2))
    db.commit()
    logged_in.get("/currentcallList")  # assigns list 1
    assert logged_in.put("/callList/ringe_status", params = {"org_num": 333}).status_code == 404


def test_unverified_user_cannot_log_in(client, fake_sms):
    client.post("/users/", json = NEW_USER)
    response = client.post("/login/token", data = {"username": NEW_USER["epost"], "password": NEW_USER["passord"]})
    assert response.status_code == 401


def test_wrong_code_does_not_delete_verified_user(client, user, fake_sms):
    client.get("/users/verification/phone/recieve_code",
               params = {"verify_sid": "VA_test", "phone_number": user["telefon_nummer"], "otp_code": "999999"})
    response = client.post("/login/token", data = {"username": user["epost"], "password": user["passord"]})
    assert response.status_code == 200
