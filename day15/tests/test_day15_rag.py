from app.api import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_rag_success():
    response = client.post(
        "/rag",
        json={"question": "What does Qdrant do?", "limit": 3},
    )
    assert response.status_code == 200
    body = response.json()
    assert "question" in body
    assert "answer" in body
    assert "sources" in body


def test_empty_question():
    response = client.post(
        "/rag",
        json={"question": "", "limit": 3},
    )
    assert response.status_code == 422
