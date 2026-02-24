import os
import sys

import pytest
from fastapi.testclient import TestClient

# project root dynamically add karna
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SRC_PATH = os.path.join(BASE_DIR, "src")
sys.path.insert(0, SRC_PATH)


@pytest.fixture(scope="session")
def client() -> TestClient:
    # Import inside function (ruff happy rahega)
    from git_day_practice.api import app

    os.environ.setdefault("API_KEY", "test-key")
    os.environ.setdefault("APP_NAME", "Test API")
    os.environ.setdefault("ENVIRONMENT", "test")
    os.environ.setdefault("DEBUG", "false")

    return TestClient(app)
