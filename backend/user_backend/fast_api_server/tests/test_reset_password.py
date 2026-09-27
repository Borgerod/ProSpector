def test_reset_email_is_sent(client, fake_email):
    response = client.get("/ResetPassword/Authentication", params = {"email_to": "tester@example.com", "verify_num": "4242"})
    assert response.status_code == 200
    assert fake_email == [("tester@example.com", "4242")]


def test_reset_password_changes_login(client, user):
    response = client.get("/ResetPassword", params = {"new_password": "new-password", "email": user["epost"]})
    assert response.status_code == 200, response.text
    login = client.post("/login/token", data = {"username": user["epost"], "password": "new-password"})
    assert login.status_code == 200
