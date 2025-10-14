# app/middleware/validate_token.py
from fastapi import Request, HTTPException
import redis
import os

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

def validate_token(request: Request):
    """
    Valida que el header Authorization contenga un Bearer token
    y que ese token exista en Redis como 'token:<valor>'.
    """
    auth_header = request.headers.get("Authorization")
    
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid or missing token")
    
    token_value = auth_header.split(" ")[1]
    
    if not redis_client.exists(f"token:{token_value}"):
        raise HTTPException(status_code=401, detail="Invalid or missing token")
    
    return token_value