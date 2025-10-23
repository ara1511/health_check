# tests/test_health_perf.py
import os
import pytest
from fastapi.testclient import TestClient
from app.main import app

# Cargar variables de entorno si es necesario (solo local)
if os.path.exists(".env.local"):
    from dotenv import load_dotenv
    load_dotenv(".env.local")

client = TestClient(app)
API_KEY = os.getenv("API_KEY", "no-api-key")

RUN_PERF = os.getenv("RUN_PERF_TESTS", "false").lower() == "true"

@pytest.mark.skipif(not RUN_PERF, reason="Performance tests disabled. Set RUN_PERF_TESTS=true to enable.")
def test_health_response_time_under_100ms(mocker):
    # 👇 Mockea la llamada a Redis para evitar conexión real
    mocker.patch("app.routes.health.redis_client.set")

    resp = client.get("/health")
    elapsed = resp.elapsed.total_seconds()
    assert elapsed < 0.1, f"Response took {elapsed:.3f}s which is >= 0.1s"

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