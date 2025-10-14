# main.py
from fastapi import FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.routes.health import router as health_router
from app.routes.ping import router as ping_router
from app.routes.get_responses import router as responses_router
from app.routes.clear_responses import router as clear_responses_router
from app.routes.generate_token import router as generate_token_router
from datetime import datetime
import os
from dotenv import load_dotenv
import redis
import logging

# Cargar variables de entorno
if os.path.exists(".env.local"):
    load_dotenv(".env.local")
else:
    load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("main")

@asynccontextmanager
async def lifespan(app: FastAPI):
    REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
    try:
        client = redis.Redis(
            host=REDIS_HOST,
            port=REDIS_PORT,
            socket_connect_timeout=3,
            socket_timeout=3,
            decode_responses=False
        )
        client.ping()
        logger.info(f"✅ Redis está corriendo en {REDIS_HOST}:{REDIS_PORT}")
    except Exception as e:
        logger.warning(f"⚠️ Redis NO está disponible en {REDIS_HOST}:{REDIS_PORT} - {str(e)}")
    
    yield

    logger.info("Aplicación apagándose...")

app = FastAPI(lifespan=lifespan)


# Configuración de CORS (antes de incluir routers)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["x-api-key", "Content-Type", "Authorization"],  # 👈 Agregamos "Authorization"
)

# Routers (todos juntos al final)
@app.get("/")
def read_root():
    return {"message": "Bienvenido a mi servicio 🚀"}

app.include_router(health_router)
app.include_router(ping_router)
app.include_router(responses_router)
app.include_router(clear_responses_router)
app.include_router(generate_token_router)

@app.get("/health_perf")
def health_perf(x_api_key: str = Header(...)):
    api_key = os.getenv("API_KEY", "no-api-key")
    if x_api_key != api_key:
        raise HTTPException(status_code=401, detail="API key inválida")
    return {
        "performance": "good",
        "timestamp": datetime.now().strftime("%Y-%m-%d"),
        "message": "El servicio está funcionando correctamente"
    }