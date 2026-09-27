def request_code(client, fake_email, email):
    response = client.get("/ResetPassword/Authentication", params = {"email_to": email})
    assert response.status_code == 200
    return fake_email[-1][1] if fake_email else None


def reset(client, email, code, new_password = "new-password"):
    return client.put("/ResetPassword", json = {"email": email, "verify_num": code, "new_password": new_password})


def login(client, email, password):
    return client.post("/login/token", data = {"username": email, "password": password})


def test_code_is_made_by_server_and_emailed(client, user, fake_email):
    code = request_code(client, fake_email, user["epost"])
    assert len(code) == 6 and code.isdigit()


def test_unknown_email_gets_same_answer_and_no_mail(client, fake_email):
    assert request_code(client, fake_email, "nobody@example.com") is None


def test_reset_with_valid_code(client, user, fake_email):
    code = request_code(client, fake_email, user["epost"])
    assert reset(client, user["epost"], code).status_code == 200
    assert login(client, user["epost"], "new-password").status_code == 200


def test_code_works_only_once(client, user, fake_email):
    code = request_code(client, fake_email, user["epost"])
    reset(client, user["epost"], code)
    assert reset(client, user["epost"], code, "third-password").status_code == 400


def test_reset_without_valid_code_is_refused(client, user, fake_email):
    request_code(client, fake_email, user["epost"])
    assert reset(client, user["epost"], "000000x").status_code == 400
    assert login(client, user["epost"], user["passord"]).status_code == 200


def test_too_many_wrong_codes_kill_the_code(client, user, fake_email):
    code = request_code(client, fake_email, user["epost"])
    for _ in range(5):
        reset(client, user["epost"], "wrong")
    assert reset(client, user["epost"], code).status_code == 400


def test_old_unauthenticated_reset_is_gone(client, user):
    response = client.get("/ResetPassword", params = {"new_password": "hacked", "email": user["epost"]})
    assert response.status_code == 405
    assert login(client, user["epost"], "hacked").status_code == 401
