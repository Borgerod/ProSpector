def test_current_call_list_assigns_a_list(logged_in, call_list):
    response = logged_in.get("/currentcallList")
    assert response.status_code == 200, response.text
    assert {row["org_num"] for row in response.json()} == {111, 222}


def test_ringe_status_toggles(logged_in, call_list, db):
    from db.models.call_list import CallList
    logged_in.get("/currentcallList")  # assigns list 1
    response = logged_in.put("/callList/ringe_status", params = {"org_num": 111})
    assert response.status_code == 200, response.text
    assert db.get(CallList, 111).ringe_status is True
