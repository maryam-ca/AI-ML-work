def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_config_no_secret(client):
    response = client.get("/config")
    assert response.status_code == 200
    assert "api_key" not in response.json()


def test_secure_without_key(client):
    response = client.get("/secure-data")
    assert response.status_code == 401


def test_secure_with_key(client):
    response = client.get(
        "/secure-data",
        headers={"X-API-Key": "supersecret123"},
    )
    assert response.status_code == 200
