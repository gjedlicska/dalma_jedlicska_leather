from app.main import app
from fastapi.testclient import TestClient

app.routes

def test_homepage():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
