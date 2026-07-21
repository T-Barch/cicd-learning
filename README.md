# Full-Stack Application Deployment & Infrastructure Task

## Project Objective
The objective of this project was to design, containerize, and deploy a full-stack web application with persistent storage and internal reverse proxying. The core task focused on establishing a multi-service architecture (Frontend, Backend API, and Database) that functions seamlessly both in local development environments and live cloud infrastructure.

---

## Key Accomplishments & Milestones

* **Multi-Container Orchestration:** Configured Docker Compose to orchestrate isolated frontend, backend, and PostgreSQL database containers on a shared virtual bridge network.
* **Reverse Proxy Routing:** Implemented Nginx as a unified entry point, serving frontend assets and securely proxying API requests (`/api/` and `/health`) to the backend without exposing raw internal backend ports.
* **Production Cloud Deployment:** Successfully deployed the multi-container environment to Railway, implementing private internal DNS networking (`cicd-learning.railway.internal`) for inter-service communication.
* **Database Resilience & Health Checks:** Configured dependency-aware startup sequences using Docker health checks and secured persistent volume storage for database operations.
* **Container Registry & Delivery:** Set up container image builds and publishing pipelines using Docker Hub registries (`barch2002/cicd-learning-frontend` and `barch2002/cicd-learning-backend`).

---

## System Architecture
 
[ User Request ]
       │
       ▼
┌───────────────────────────────┐
│  Nginx Proxy & Frontend       │
└──────────────┬────────────────┘
               │ (Internal Proxy Routing)
               ▼
┌───────────────────────────────┐
│  Flask REST API (Backend)     │
└──────────────┬────────────────┘
               │ (Database Queries)
               ▼
┌───────────────────────────────┐
│PostgreSQL (Persistent Storage)│
└───────────────────────────────┘