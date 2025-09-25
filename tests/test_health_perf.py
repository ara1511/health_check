
import os
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

RUN_PERF = os.getenv("RUN_PERF_TESTS", "false").lower() == "true"

@pytest.mark.skipif(not RUN_PERF, reason="Performance tests disabled. Set RUN_PERF_TESTS=true to enable.")
def test_health_response_time_under_100ms():
    resp = client.get("/health")
    elapsed = resp.elapsed.total_seconds()
    assert elapsed < 0.1, f"Response took {elapsed:.3f}s which is >= 0.1s"
