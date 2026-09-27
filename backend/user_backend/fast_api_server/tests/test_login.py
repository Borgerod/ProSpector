def test_login_sets_cookie(client, user):
    response = client.post("/login/token", data = {"username": user["epost"], "password": user["passord"]})
    assert response.status_code == 200, response.text
    assert response.json()["token_type"] == "bearer"
    assert "access_token" in response.cookies


def test_login_wrong_password(client, user):
    response = client.post("/login/token", data = {"username": user["epost"], "password": "wrong"})
    assert response.status_code == 401


def test_protected_route_needs_login(client):
    assert client.get("/currentcallList").status_code == 401
