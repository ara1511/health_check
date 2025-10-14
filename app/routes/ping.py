# app/routes/ping.py

from fastapi import APIRouter, Request
from datetime import datetime
import json
import redis
import os

router = APIRouter()

# Configuración de Redis (igual que en health.py)
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
redis_client = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    decode_responses=True,
    socket_connect_timeout=5,
    socket_timeout=5,
    
)

@router.get("/ping")
async def ping(request: Request):
    """
    Endpoint que registra cada ping en Redis con datos relevantes.
    """
    client_ip = request.client.host if request.client else "unknown"
    timestamp = datetime.now().isoformat()
    
    log_data = {
        "ip": client_ip,
        "timestamp": timestamp,
        "user_agent": request.headers.get("user-agent", "unknown"),
        "endpoint": "/ping"
    }

    # Guardar en Redis: clave = ping:<timestamp>, valor = JSON
    key = f"ping:{timestamp.replace(':', '-')}"  # evitar : en clave
    redis_client.set(key, json.dumps(log_data))
    redis_client.expire(key, 3600)  # expira en 1 hora

    return {
        "status": "pong",
        "logged": True,
        "timestamp": timestamp
    }