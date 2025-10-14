# tests/test_health.py
from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import patch
import json

client = TestClient(app)

@patch("app.routes.health.redis_client")
def test_health_status_ok(mock_redis):
    # Simula que Redis funciona (sin errores)
    mock_redis.set.return_value = True
    mock_redis.expire.return_value = True

    resp = client.get("/health")
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "ok"
    assert "timestamp" in data

    # Verifica que se llamó a Redis con los datos correctos
    mock_redis.set.assert_called_once()
    mock_redis.expire.assert_called_once()