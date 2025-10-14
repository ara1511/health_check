# app/routes/get_responses.py
from fastapi import APIRouter, Depends, Request
import redis
import json
import os
import uuid
from app.middleware.validate_token import validate_token


router = APIRouter()

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

@router.get("/get-responses", dependencies=[Depends(validate_token)])
def get_responses():
    """
    Devuelve todos los logs guardados en Redis.
    Requiere un token válido en el header: Authorization: Bearer <token>
    """
    keys = redis_client.keys("health:*") + redis_client.keys("ping:*")
    logs = []
    for key in keys:
        data_str = redis_client.get(key)
        if data_str:
            try:
                data = json.loads(data_str)
                if "id" not in data:
                    data["id"] = str(uuid.uuid4())
                logs.append(data)
            except json.JSONDecodeError:
                continue
    logs.sort(key=lambda x: x.get("timestamp", ""), reverse=True)
    return {"total": len(logs), "logs": logs}