from fastapi import FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.routes.health import router as health_router
from datetime import datetime  
import os
from dotenv import load_dotenv

load_dotenv()  # Carga las variables del archivo .env

app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # O especifica los dominios permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["x-api-key", "Content-Type"],  # Permite la cabecera personalizada
)

@app.get("/")
def read_root():
    return {"message": "Bienvenido a mi servicio 🚀"}

app.include_router(health_router)

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



