# 🚀 mi-servicio

**Health-Check Service** desarrollado con **FastAPI** para monitorear el estado y rendimiento del servicio de manera rápida y segura.

---

## 📌 Endpoints disponibles

| Método | Ruta            | Descripción |
|--------|----------------|------------|
| `GET`  | `/`             | Mensaje de bienvenida. |
| `GET`  | `/health`       | Retorna el estado del servicio:<br>```json { "status": "ok", "timestamp": "..." } ``` |
| `GET`  | `/health_perf`  | Retorna el rendimiento del servicio:<br>```json { "performance": "good" } ```<br>**Requiere cabecera `x-api-key`.** |

### 🔑 Ejemplo de cabecera para `/health_perf`

```http
x-api-key: tu_api_key_aqui
⚡ Instalación y ejecución local

Clonar el repositorio:

git clone https://tu-repositorio.git
cd mi-servicio


Activar entorno virtual:

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate


Instalar dependencias:

pip install -r requirements.txt


Ejecutar el servicio:

uvicorn app.main:app --reload


El servicio estará disponible en: http://127.0.0.1:8000/

🌿 Variables de entorno

Crea un archivo .env en la raíz del proyecto con:

API_KEY=tu_api_key_aqui

🧪 Pruebas

Ejecutar tests con pytest:

pytest

💻 Ejemplo de uso con curl
curl -H "x-api-key: tu_api_key_aqui" http://127.0.0.1:8000/health_perf


Respuesta esperada:

{
  "performance": "good",
  "timestamp": "2025-09-24",
  "message": "El servicio está funcionando correctamente"
}

🛠 Tecnologías utilizadas

Python 3.11+

FastAPI

Uvicorn

python-dotenv

pytest# health_check
