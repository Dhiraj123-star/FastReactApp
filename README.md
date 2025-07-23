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

- 🐳 **Fully Containerized Setup**  
  Both services (frontend + backend) run inside isolated Docker containers for consistency and ease of deployment.

- 🔐 **Environment Variables Support**  
  Secure secrets management using `.env` files and `python-dotenv`.

- 🔗 **Seamless Integration**  
  Built to ensure smooth interaction across services using CORS-enabled communication.

---

## ✅ How It Works

1. The user visits the web app.
2. The React frontend sends HTTP requests to the FastAPI backend.
3. The backend responds with messages or performs CRUD actions.
4. The frontend dynamically displays the data.

---

## 📦 Tech Stack

- 🧬 Backend: [FastAPI](https://fastapi.tiangolo.com/)
- ⚛️ Frontend: [React](https://reactjs.org/)
- 🐳 DevOps: Docker & Docker Compose
- 🗃️ Database: SQLite
- 🔐 Secrets: Python Dotenv

---

## 🛠️ Endpoints Overview

| Method | Endpoint        | Description             |
|--------|-----------------|-------------------------|
| GET    | `/items/`       | List all items          |
| POST   | `/items/`       | Add new item            |
| PUT    | `/items/{id}`   | Update item by ID       |
| DELETE | `/items/{id}`   | Delete item by ID       |

---

Made with ❤️ using React, FastAPI & Docker.
