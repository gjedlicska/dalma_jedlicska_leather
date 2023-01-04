from fastapi.testclient import TestClient

from app.main import app

app.routes


def test_homepage():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
