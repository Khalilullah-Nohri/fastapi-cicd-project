# FastAPI CICD Task Project

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100.0-brightgreen)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-20.10-blue)](https://www.docker.com/)
[![MySQL](https://img.shields.io/badge/MySQL-8.0-orange)](https://www.mysql.com/)
[![GitHub](https://img.shields.io/badge/GitHub-Khalilullah-Nohri-181717)](https://github.com/Khalilullah-Nohri/fastapi-cicd-project)

A simple **Task Management API** built with FastAPI, MySQL, SQLAlchemy, and Docker. Includes full **CI/CD pipeline** setup with Jenkins and Docker Hub.

---

## Features

- CRUD operations for tasks (`/tasks` endpoint)
- MySQL database integration
- SQLAlchemy ORM models
- FastAPI Swagger docs: `/docs`
- Multi-stage Dockerfile for optimized image
- Docker Compose support for local development
- Ready for Jenkins CI/CD pipeline
- Unit tests with pytest

---

## Folder Structure

```bash
fastapi-cicd-project/
│   .env.example
│   docker-compose.yml
│   Dockerfile
│   README.md
│   requirements.txt
│
└───code/
    │   app.py
    │   __init__.py
    │
    ├───api/
    │       # Your route modules, e.g., users.py, items.py
    │
    ├───core/
    │       # Core configurations, settings.py, etc.
    │
    ├───crud/
    │       # CRUD operations for your models
    │
    ├───db/
    │       # Database connection, session, etc.
    │
    ├───models/
    │       # SQLAlchemy models
    │
    ├───schemas/
    │       # Pydantic schemas
    │
    └───utils/
            # Utility functions

```


- **code/api**: API routes
- **code/crud**: Database CRUD operations
- **code/db**: Database session and migrations
- **code/models**: SQLAlchemy models
- **code/schemas**: Pydantic schemas
- **code/core**: Configuration & logging

---

## Quick Start

### **Clone the repo**
```bash
git clone https://github.com/Khalilullah-Nohri/fastapi-cicd-project.git
cd fastapi-cicd-project
```
### Environment
Copy .env.example to .env and fill in real values.

```bash
cp .env.example .env
```

### Run Locally (Docker Compose)
```bash
docker compose up --build -d
```

- **Swagger docs** : http://localhost:8000/docs
- **Health check**: http://localhost:8000/



## 💡 Development Tools Used

- **IDE:** Visual Studio Code  
- **Database GUI:** SQLyog  
- **API Testing:** Postman  
- **Environment Management:** venv  
- **Version Control:** Git & GitHub  
- **Docker:** For Containerization
---

## 👨‍💻 Author

**Developed by [Khalilullah Nohri](https://www.linkedin.com/in/khalilullah-dev)**  
💻 Python & JavaScript Developer  
📩 For queries or collaboration: **nohrikhalilullah@gmail.com**  
🌐 [GitHub](https://github.com/Khalilullah-Nohri) • [LinkedIn](https://www.linkedin.com/in/khalilullah-dev) • [Docker Hub](https://hub.docker.com/u/khalilullah59) 


