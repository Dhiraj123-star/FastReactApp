
# ⚡ FastReactApp

A modern fullstack application that seamlessly connects a **React** frontend with a **FastAPI** backend, containerized using **Docker** and orchestrated with **Docker Compose**.

---

## 🌐 Functionality Overview

- 🧠 **API-Driven Architecture**  
  The React frontend fetches data from a FastAPI backend using clean RESTful endpoints.

- ✨ **Full CRUD API Support**  
  Supports Create, Read, Update, and Delete operations on a list of items via FastAPI.

- 🚫 **Input Validation**  
  Backend prevents blank entries for item names using robust Pydantic validation.

- 🚀 **Live Interaction**  
  On page load, the frontend sends a request to the backend and dynamically displays the response.

- 🔄 **Asynchronous Communication**  
  Powered by the `fetch` API to handle backend communication without page reloads.

- 🧠 **Redis Caching for Performance**  
  GET requests for all items are now cached in **Redis**, improving speed and reducing database load.  
  Cache is invalidated on POST, PUT, and DELETE operations.

- 🐳 **Fully Containerized Setup**  
  All services (frontend + backend + Redis) run inside isolated Docker containers for consistency and ease of deployment.

- 🔐 **Environment Variables Support**  
  Secure secrets management using `.env` files and `python-dotenv`.

- 🔗 **Seamless Integration**  
  Built to ensure smooth interaction across services using CORS-enabled communication.

---

## ✅ How It Works

1. The user visits the web app.
2. The React frontend sends HTTP requests to the FastAPI backend.
3. The backend responds with messages or performs CRUD actions.
4. Redis caches the item list on reads and invalidates it on writes.
5. The frontend dynamically displays the data.

---

## 📦 Tech Stack

- 🧬 Backend: [FastAPI](https://fastapi.tiangolo.com/)
- ⚛️ Frontend: [React](https://reactjs.org/)
- 🐳 DevOps: Docker & Docker Compose
- 🗃️ Database: SQLite
- ⚡ Cache: Redis
- 🔐 Secrets: Python Dotenv

---

## 🛠️ Endpoints Overview

| Method | Endpoint        | Description             |
|--------|-----------------|-------------------------|
| GET    | `/items/`       | List all items (cached) |
| POST   | `/items/`       | Add new item            |
| PUT    | `/items/{id}`   | Update item by ID       |
| DELETE | `/items/{id}`   | Delete item by ID       |

---

## 🚀 Running Locally

```bash
docker compose up --build
````

Visit: [http://localhost:3000](http://localhost:3000)

---

Made with ❤️ using React, FastAPI, Redis & Docker.


