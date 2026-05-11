import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from fastapi.testclient import TestClient
from src.app.api import app

client = TestClient(app)


def test_basic_health_exists():
    response = client.get("/health")
    assert response.status_code == 200
