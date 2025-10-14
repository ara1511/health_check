# app/routes/generate_token.py
from fastapi import APIRouter
import redis
import os
import uuid

router = APIRouter()

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

@router.post("/generate-token")
def generate_token():
    """
    Genera un token aleatorio y lo guarda en Redis con expiración de 1 hora.
    """
    token = str(uuid.uuid4())
    redis_client.setex(f"token:{token}", 3600, "active")  # expira en 3600 segundos (1h)
    return {"token": token}