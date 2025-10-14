# tests/test_health_perf.py
import os
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Usa la misma API key que en tu .env o docker-compose.yml
API_KEY = "tu-clave-secreta-aqui"

RUN_PERF = os.getenv("RUN_PERF_TESTS", "false").lower() == "true"

@pytest.mark.skipif(not RUN_PERF, reason="Performance tests disabled. Set RUN_PERF_TESTS=true to enable.")
def test_health_response_time_under_100ms():
    resp = client.get("/health")
    elapsed = resp.elapsed.total_seconds()
    assert elapsed < 0.1, f"Response took {elapsed:.3f}s which is >= 0.1s"

# Nuevo test para /health_perf
def test_health_perf_requires_valid_api_key():
    # Sin cabecera → 422
    resp = client.get("/health_perf")
    assert resp.status_code == 422

    # Con cabecera inválida → 401
    resp = client.get("/health_perf", headers={"x-api-key": "clave-incorrecta"})
    assert resp.status_code == 401

    # Con cabecera válida → 200
    resp = client.get("/health_perf", headers={"x-api-key": API_KEY})
    assert resp.status_code == 200
    assert resp.json()["performance"] == "good"