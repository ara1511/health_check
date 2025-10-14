# 🚀 Mi-Servicio

<div align="center">

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge\&logo=fastapi\&logoColor=white)
![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge\&logo=python\&logoColor=ffdd54)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge\&logo=docker\&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=for-the-badge\&logo=redis\&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

**Health-Check & Logging Service** desarrollado con **FastAPI**, que registra cada solicitud en **Redis** y expone métricas en tiempo real con sistema de tokens JWT.

</div>

---

## 🌟 Características

* ✅ **Health check** con timestamp y zona horaria (`/health`)
* ✅ **Ping endpoint** para monitoreo simple (`/ping`)
* ✅ **Rendimiento protegido** con API Key (`/health_perf`)
* ✅ **Registro automático** en Redis de cada solicitud (IP, user-agent, timestamp, endpoint)
* ✅ **Endpoint de auditoría**: `/get-responses` devuelve todos los logs almacenados
* 🆕 **Sistema de tokens**: Generación y validación con middleware (`/generate-token`)
* 🆕 **Limpieza de logs**: Endpoint para borrar todos los registros (`/clear-responses`)
* 🆕 **Middleware de autenticación** con Bearer tokens
* 🆕 **Interfaz HTML** de pruebas incluida (`test.html`)
* ✅ **CORS configurado** con soporte para headers personalizados
* ✅ Soporte para **Docker** y **desarrollo local**
* ✅ Tests automatizados con **pytest**

---

## 📌 Endpoints Disponibles

| Método   | Ruta               | Descripción                                | Requiere API Key | Requiere Token |
| :------: | :----------------- | :----------------------------------------- | :--------------: | :------------: |
|  `GET`   | `/`                | 🏠 Mensaje de bienvenida                   |         ❌        |       ❌       |
|  `GET`   | `/health`          | 💓 Estado del servicio + registro en Redis |         ❌        |       ❌       |
|  `GET`   | `/ping`            | 🏓 Respuesta "pong" + registro en Redis    |         ❌        |       ❌       |
|  `GET`   | `/health_perf`     | ⚡ Métricas de rendimiento                  |         ✅        |       ❌       |
|  `GET`   | `/get-responses`   | 📊 Lista de logs guardados en Redis        |         ❌        |       ❌       |
|  `POST`  | `/generate-token`  | 🔐 Genera token JWT con expiración 1h      |         ❌        |       ❌       |
| `DELETE` | `/clear-responses` | 🗑️ Elimina todos los logs de Redis          |         ❌        |       ❌       |

---

### 🏠 **GET** `/`

```json
{ "message": "Bienvenido a mi servicio 🚀" }
```

### 💓 **GET** `/health`

Registra en Redis y devuelve:

```json
{
  "status": "ok",
  "timestamp": "2025-10-08T21:30:00.123456-03:00"
}
```

### 🏓 **GET** `/ping`

Registra en Redis y devuelve:

```json
{
  "status": "pong",
  "logged": true,
  "timestamp": "2025-10-08T21:30:05.789012"
}
```

### ⚡ **GET** `/health_perf`

🔑 Requiere cabecera `x-api-key`:

```
GET /health_perf
x-api-key: tu_api_key_aqui
```

```json
{
  "performance": "good",
  "timestamp": "2025-10-08",
  "message": "El servicio está funcionando correctamente"
}
```

### 📊 **GET** `/get-responses`

Devuelve todos los logs almacenados en Redis:

```json
{
  "total": 2,
  "logs": [
    {
      "ip": "127.0.0.1",
      "user_agent": "curl/8.4.0",
      "timestamp": "2025-10-08T21:30:05.789012",
      "endpoint": "/ping",
      "id": "a1b2c3d4-..."
    },
    {
      "ip": "127.0.0.1",
      "user_agent": "Mozilla/5.0...",
      "timestamp": "2025-10-08T21:30:00.123456-03:00",
      "endpoint": "/health",
      "id": "e5f6g7h8-..."
    }
  ]
}
```

### 🔐 **POST** `/generate-token`

Genera un token JWT que expira en 1 hora y lo almacena en Redis:

```json
{
  "token": "a1b2c3d4-e5f6-7890-1234-567890abcdef"
}
```

### 🗑️ **DELETE** `/clear-responses`

Elimina todos los logs almacenados en Redis (claves `health:*` y `ping:*`):

```json
{
  "message": "All responses have been cleared successfully"
}
```

---

## 🐳 Ejecución con Docker (Recomendado)

### 1️⃣ Construir e iniciar

```bash
docker-compose up --build
```

✅ App disponible en: [http://localhost:8000](http://localhost:8000)
✅ Redis disponible en: localhost:6379

### 2️⃣ Ver logs en tiempo real

```bash
docker-compose logs -f
```

### 3️⃣ Detener

```bash
# Ctrl + C en la terminal, o:
docker-compose down
```

---

## 💻 Ejecución Local (Desarrollo con --reload)

### 1️⃣ Levantar Redis localmente

```powershell
docker run -d --name redis-local -p 6379:6379 redis:7-alpine
```

### 2️⃣ Configurar variables de entorno

Crea un archivo `.env.local`:

```env
REDIS_HOST=localhost
REDIS_PORT=6379
API_KEY=tu_api_key_aqui
```

⚠️ Agrega `.env.local` a tu `.gitignore`.

### 3️⃣ Ejecutar la app

```powershell
$env:REDIS_HOST="localhost"
uvicorn app.main:app --reload
```

---

## 🧪 Pruebas

### Instalar dependencias de testing

```bash
pip install -r requirements.txt
```

### Ejecutar tests

```bash
pytest
```

✅ Los tests usan mocks para Redis → no requieren que Redis esté corriendo.

---

## 🌿 Variables de Entorno

| Variable     | Valor por defecto | Descripción                     |
| ------------ | ----------------- | ------------------------------- |
| `REDIS_HOST` | `localhost`       | Host de Redis                   |
| `REDIS_PORT` | `6379`            | Puerto de Redis                 |
| `API_KEY`    | `no-api-key`      | Clave usada para `/health_perf` |

En Docker Compose, se usan los valores definidos en `docker-compose.yml`.

---

## 🛠 Tecnologías Utilizadas

| Tecnología        | Descripción                                |
| ----------------- | ------------------------------------------ |
| **FastAPI**       | Framework web moderno y rápido             |
| **Redis**         | Almacenamiento en memoria de logs y tokens |
| **Docker**        | Contenerización y portabilidad             |
| **pytest**        | Testing automatizado                       |
| **Uvicorn**       | Servidor ASGI para desarrollo y producción |
| **python-dotenv** | Gestión de variables de entorno            |
| **PyJWT**         | Librería para tokens JWT                   |

---

## 📦 Estructura del Proyecto

```text
mi-servicio/
├── app/
│   ├── main.py                    # 🚀 Configuración principal FastAPI
│   ├── test.html                  # 🌐 Interfaz HTML de pruebas
│   ├── middleware/
│   │   └── validate_token.py      # 🔐 Middleware de validación JWT
│   └── routes/
│       ├── __init__.py
│       ├── health.py              # 💓 Endpoint /health
│       ├── ping.py                # 🏓 Endpoint /ping
│       ├── get_responses.py       # 📊 Endpoint /get-responses
│       ├── clear_responses.py     # 🗑️ Endpoint /clear-responses
│       └── generate_token.py      # 🔐 Endpoint /generate-token
├── tests/
│   ├── conftest.py                # ⚙️ Configuración de pytest
│   ├── test_health.py             # 🧪 Tests para /health
│   └── test_health_perf.py        # 🧪 Tests para /health_perf
├── docker-compose.yml             # 🐳 Servicios: app + redis
├── Dockerfile                     # 🐳 Imagen de la aplicación
├── requirements.txt               # 📦 Dependencias Python
└── README.md                      # 📖 Este archivo
```

### 🆕 Nuevos Componentes

* **`middleware/validate_token.py`**: Middleware para validar tokens Bearer almacenados en Redis
* **`routes/generate_token.py`**: Generación de tokens UUID con expiración automática
* **`routes/clear_responses.py`**: Limpieza masiva de logs almacenados en Redis
* **`test.html`**: Interfaz web para probar endpoints con API keys y tokens

---

## 🧪 Testing y Desarrollo

### Interfaz HTML de Pruebas

El proyecto incluye un archivo `test.html` que puedes abrir en tu navegador para probar los endpoints de forma interactiva. La interfaz permite:

* ✅ Probar `/health_perf` con API key
* ✅ Generar tokens JWT
* ✅ Validar tokens con middleware
* ✅ Limpiar logs de Redis
* ✅ Ver respuestas en formato JSON

### Usando `curl` para probar

```bash
# Generar un token
curl -X POST http://localhost:8000/generate-token

# Usar el token (reemplaza YOUR_TOKEN)
curl -H "Authorization: Bearer YOUR_TOKEN" http://localhost:8000/some-protected-endpoint

# Limpiar todos los logs
curl -X DELETE http://localhost:8000/clear-responses

# Ver todos los logs
curl http://localhost:8000/get-responses
```

---

Made with ❤️ using **FastAPI + Redis + Docker + JWT**

---


