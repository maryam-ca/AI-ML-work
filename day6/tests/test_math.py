def test_divide_success(client):
    payload = {"a": 10, "b": 2}
    r = client.post("/math/divide", json=payload)

    assert r.status_code == 200
    assert r.json()["result"] == 5


def test_divide_by_zero(client):
    payload = {"a": 10, "b": 0}
    r = client.post("/math/divide", json=payload)

    assert r.status_code == 400
