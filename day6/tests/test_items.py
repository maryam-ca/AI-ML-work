def test_create_item_success(client):
    payload = {"name": "Book", "price": 10.5, "in_stock": True}

    r = client.post("/items", json=payload)

    assert r.status_code == 201
    data = r.json()

    assert data["name"] == "Book"
    assert data["price"] == 10.5
    assert data["in_stock"] is True


def test_list_items(client):
    r = client.get("/items")
    assert r.status_code == 200
    assert isinstance(r.json(), list)
