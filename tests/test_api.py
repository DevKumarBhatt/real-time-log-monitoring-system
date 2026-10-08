from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert "Real-Time Log Monitoring System" in response.json()["message"]


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_logs_endpoint():
    response = client.get("/logs/")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_stats_endpoint():
    response = client.get("/logs/stats")

    assert response.status_code == 200

    data = response.json()

    assert "total" in data
    assert "INFO" in data
    assert "WARNING" in data
    assert "ERROR" in data
    assert "CRITICAL" in data