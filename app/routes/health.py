from fastapi import APIRouter
from datetime import datetime
import pytz 

router = APIRouter()

@router.get("/health", tags=["health"])
async def health_check():
    """
    Health endpoint minimal: no auth, no DB deps.
    Retorna status ok y timestamp local ISO8601.
    """
    local_tz = pytz.timezone("America/Argentina/Buenos_Aires")
    local_time = datetime.now(local_tz)
    return {
        "status": "ok",
        "timestamp": local_time.isoformat()
    }
