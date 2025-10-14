# app/routes/clear_responses.py
from fastapi import APIRouter
import redis
import os

router = APIRouter()

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

@router.delete("/clear-responses")
def clear_responses():
    """
    Elimina todas las claves en Redis que empiezan con 'health:' o 'ping:'.
    Devuelve un mensaje de éxito.
    """
    # Buscar todas las claves
    keys = redis_client.keys("health:*") + redis_client.keys("ping:*")
    
    if keys:
        # Eliminarlas
        redis_client.delete(*keys)
        message = "All responses have been cleared successfully"
    else:
        message = "No responses to clear"

    return {"message": message}