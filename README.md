# 🚀 Mi-Servicio

<div align="center">

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Status](https://img.shields.io/badge/status-active-brightgreen?style=for-the-badge)

**Health-Check Service** desarrollado con **FastAPI** para monitorear el estado y rendimiento del servicio de manera rápida y segura.

</div>

---

## 📌 Endpoints Disponibles

<div align="center">

| Método | Ruta            | Descripción |
|:------:|:----------------|:------------|
| `GET`  | `/`             | 🏠 Mensaje de bienvenida |
| `GET`  | `/health`       | 💓 Estado del servicio |
| `GET`  | `/health_perf`  | ⚡ Rendimiento del servicio |

</div>

### 🏠 **GET** `/`
Retorna un mensaje de bienvenida.

### 💓 **GET** `/health`
Retorna el estado del servicio:
```json
{ 
  "status": "ok", 
  "timestamp": "..." 
}
```

### ⚡ **GET** `/health_perf`
Retorna el rendimiento del servicio:
```json
{ 
  "performance": "good" 
}
```
> **🔑 Requiere cabecera `x-api-key`**

#### Ejemplo de cabecera para `/health_perf`
```http
x-api-key: tu_api_key_aqui
```

---

## ⚡ Instalación y Ejecución Local

### 1️⃣ Clonar el repositorio
```bash
git clone https://tu-repositorio.git
cd mi-servicio
```

### 2️⃣ Activar entorno virtual
```bash
# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

### 3️⃣ Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4️⃣ Ejecutar el servicio
```bash
uvicorn app.main:app --reload
```

🎉 **El servicio estará disponible en:** `http://127.0.0.1:8000/`

---

## 🌿 Variables de Entorno

Crea un archivo `.env` en la raíz del proyecto:

```env
API_KEY=tu_api_key_aqui
```

---

## 🧪 Pruebas

Ejecutar tests con pytest:

```bash
pytest
```

---

## 💻 Ejemplo de Uso con cURL

```bash
curl -H "x-api-key: tu_api_key_aqui" http://127.0.0.1:8000/health_perf
```

**Respuesta esperada:**
```json
{
  "performance": "good",
  "timestamp": "2025-09-24",
  "message": "El servicio está funcionando correctamente"
}
```

---

## 🛠 Tecnologías Utilizadas

<div align="center">

| Tecnología | Versión | Descripción |
|:----------:|:-------:|:------------|
| **Python** | 3.11+ | Lenguaje de programación |
| **FastAPI** | Latest | Framework web moderno |
| **Uvicorn** | Latest | Servidor ASGI |
| **python-dotenv** | Latest | Variables de entorno |
| **pytest** | Latest | Framework de testing |

</div>

---

<div align="center">

**⭐ Si este proyecto te resulta útil, considera darle una estrella ⭐**

Made with ❤️ using FastAPI

</div>