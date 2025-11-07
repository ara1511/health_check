# app/routes/health.py
from fastapi import APIRouter, Request
from datetime import datetime
import pytz
import redis
import json
import os

router = APIRouter()

# Reutilizamos la misma conexión (o podrías inyectarla mejor con Depends, pero por simplicidad...)
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

@router.get("/health", tags=["health"])
async def health_check(request: Request):
    local_tz = pytz.timezone("America/Argentina/Buenos_Aires")
    local_time = datetime.now(local_tz)
    timestamp = local_time.isoformat()

    # Registrar en Redis
    client_ip = request.client.host if request.client else "unknown"
    log_data = {
        "ip": client_ip,
        "timestamp": timestamp,
        "user_agent": request.headers.get("user-agent", "unknown"),
        "endpoint": "/health"
    }
    key = f"health:{timestamp.replace(':', '-')}"
    redis_client.set(key, json.dumps(log_data))
    redis_client.expire(key, 3600)

    return {
        "status": "ok",
        "timestamp":  
    }