import pytest
from day7_app.api import app
from fastapi.testclient import TestClient


@pytest.fixture
def client():
    return TestClient(app)
