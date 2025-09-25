import re
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_status_ok():
    resp = client.get("/health")
    assert resp.status_code == 200
    data = resp.json()
    assert "status" in data
    assert data["status"] == "ok"
    assert "timestamp" in data
    assert re.match(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}", data["timestamp"])
