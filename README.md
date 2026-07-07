
# CI/CD Learning project...

A simple full-stack web application developed as part of a CI/CD learning project. The application demonstrates how a frontend, backend, and database can work together using Docker containers. It also serves as a foundation for learning Docker Hub, GitHub Actions, Continuous Integration, and Continuous Deployment.

---

## Project Overview

This project consists of three main services:

- **Frontend:** HTML, CSS, and JavaScript served by Nginx.
- **Backend:** Flask REST API written in Python.
- **Database:** PostgreSQL used to store application data.

All services are connected using Docker Compose, allowing the entire application to be started with a single command.

---

## Features

- Add new items through a simple web interface.
- Display all stored items.
- Delete existing items.
- Data is stored permanently using a Docker volume.
- REST API for communication between the frontend and backend.
- Nginx reverse proxy for serving the frontend and routing API requests.

---

## Project Structure

```text
cicd-learning/
│
├── frontend/
│   └── index.html
│
├── Dockerfile
├── Dockerfile.nginx
├── docker-compose.yml
├── backend_app.py
├── requirements.txt
├── README.md
└── QUICK_START.md
```

---

## Technologies Used

- HTML
- CSS
- JavaScript
- Python
- Flask
- PostgreSQL
- Docker
- Docker Compose
- Nginx
- Git
- GitHub
- Docker Hub

---

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/T-Barch/cicd-learning.git
```

### 2. Move into the project folder

```bash
cd cicd-learning
```

### 3. Start all containers

```bash
docker compose up --build
```

### 4. Open the application

Frontend:

```
http://localhost
```

API:

```
http://localhost/api/items
```

Health Check:

```
http://localhost/health
```

---

## Docker Services

The application consists of three Docker containers.

| Service | Description |
|----------|-------------|
| Frontend | Nginx serves the user interface |
| Backend | Flask REST API |
| Database | PostgreSQL database |

---

## Docker Hub Images

Backend Image

```
barch2002/cicd-learning-backend:latest
```

Frontend Image

```
barch2002/cicd-learning-frontend:latest
```

---

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/api/items` | Retrieve all items |
| POST | `/api/items` | Add a new item |
| GET | `/api/items/<id>` | Retrieve a single item |
| DELETE | `/api/items/<id>` | Delete an item |
| GET | `/health` | Check backend health |

---

## Learning Objectives

This project was created to practice:

- Docker containerization
- Multi-container applications
- Docker Compose
- Docker networking
- Docker volumes
- REST API development
- Docker Hub image publishing
- Git and GitHub workflows
- CI/CD concepts

---

## Future Improvements

Some planned improvements include:

- Edit existing items
- User authentication
- Better frontend design
- Automated testing
- GitHub Actions CI pipeline
- Automatic deployment to the cloud
- Monitoring with Prometheus and Grafana

---

## Author

**Yitayal Minale**

This project was developed as part of a Full-Stack CI/CD training program to gain hands-on experience with containerization, version control, and modern DevOps practices.
