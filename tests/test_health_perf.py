# tests/test_health_perf.py
import os
import sys
from unittest.mock import patch

# 👇 MOCKEA redis.Redis ANTES de importar cualquier cosa de la app
with patch("redis.Redis") as mock_redis_class:
    # Simula un cliente de Redis funcional
    mock_instance = mock_redis_class.return_value
    mock_instance.set.return_value = True
    mock_instance.expire.return_value = True
    mock_instance.ping.return_value = True

    # Ahora sí importa la app (después del mock)
    from fastapi.testclient import TestClient
    from app.main import app

# Cargar variables de entorno si es necesario
if os.path.exists(".env.local"):
    from dotenv import load_dotenv
    load_dotenv(".env.local")

client = TestClient(app)
API_KEY = os.getenv("API_KEY", "no-api-key")
RUN_PERF = os.getenv("RUN_PERF_TESTS", "false").lower() == "true"

@pytest.mark.skipif(not RUN_PERF, reason="Performance tests disabled. Set RUN_PERF_TESTS=true to enable.")
def test_health_response_time_under_100ms():
    resp = client.get("/health")
    elapsed = resp.elapsed.total_seconds()
    assert elapsed < 0.1, f"Response took {elapsed:.3f}s which is >= 0.1s"

def test_health_perf_requires_valid_api_key():
    resp = client.get("/health_perf")
    assert resp.status_code == 422

    resp = client.get("/health_perf", headers={"x-api-key": "clave-incorrecta"})
    assert resp.status_code == 401

    resp = client.get("/health_perf", headers={"x-api-key": API_KEY})
    assert resp.status_code == 200
    assert resp.json()["performance"] == "good"