# Quick Start Guide: Full-Stack CI/CD App
**For: Say's INSA Internship Prep**

---

## **Step 1: Install Docker (5 mins)**

### Windows/Mac:
1. Go to: https://www.docker.com/products/docker-desktop
2. Download Docker Desktop for your OS
3. Install and restart computer
4. Verify: Open terminal/PowerShell and run:
```bash
docker --version
```
Should show: `Docker version 24.x.x` (version number)

### Linux (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install docker.io docker-compose
sudo usermod -aG docker $USER
newgrp docker
```

---

## **Step 2: Create Project Directory (2 mins)**

```bash
# Create folder
mkdir cicd-learning
cd cicd-learning

# Download all files from outputs folder into this directory
# You should have:
# ├── backend_app.py
# ├── requirements.txt
# ├── Dockerfile
# ├── docker-compose.yml
# ├── frontend/
# │   ├── index.html
# │   └── style.css
```

Or copy this structure:
```bash
mkdir frontend
# Put index.html and style.css in frontend/ folder
```

---

## **Step 3: Run Your First Stack (5 mins)**

```bash
# In the cicd-learning directory:
docker compose up
```

**What you should see:**
```
frontend  | Configuration successfully loaded
backend   | * Running on http://0.0.0.0:5000
database  | database system is ready to accept connections
```

---

## **Step 4: Test It Works (3 mins)**

Open your browser and go to:
```
http://localhost
```

You should see:
- ✅ Title: "🚀 CI/CD Learning App"
- ✅ Green "✅ Backend is healthy" message
- ✅ Items list (empty at first)
- ✅ Input field to add items

**Try it:**
1. Type "Learn Docker" in the input box
2. Click "Add"
3. Item should appear in the list
4. Data persists because of the database!

---

## **Step 5: Test Data Persistence (Important!)**

This proves the volume works:

```bash
# Terminal 1: Stop containers (Ctrl+C)
# Then:

docker compose down

# Wait 5 seconds, then:

docker compose up
```

Go to http://localhost again.

**Your item is still there!** ✅

Data persisted across container restart. This is the **core concept of Week 1**.

---

## **Step 6: Understand What You Built**

### **3 Services Running:**

1. **Frontend (Nginx)**
   - Port: 80 (http://localhost)
   - Serves: HTML + CSS + JavaScript
   - Calls: Backend API

2. **Backend (Flask Python)**
   - Port: 5000 (http://localhost:5000)
   - API endpoints:
     - `GET /health` → health check
     - `GET /api/items` → list all items
     - `POST /api/items` → create item
     - `DELETE /api/items/<id>` → delete item
     - `GET /metrics` → Prometheus metrics (Week 5)

3. **Database (PostgreSQL)**
   - Port: 5432
   - Username: `app_user`
   - Password: `secure_password_123`
   - Database: `app_database`
   - Stores: All items created via API

### **Communication Flow:**
```
Browser → Nginx (Frontend)
         ↓
        [Docker Network Bridge]
         ↓
      Flask Backend
         ↓
        [Docker Network Bridge]
         ↓
      PostgreSQL Database
```

All three services talk via **Docker's internal bridge network** (automatic).

---

## **Useful Commands**

```bash
# See running containers
docker ps

# See logs from specific service
docker logs -f cicd-learning-backend-1

# Stop all containers (without deleting)
docker compose stop

# Start them again
docker compose start

# Remove everything (volume data persists)
docker compose down

# Remove everything INCLUDING data (⚠️ be careful)
docker compose down -v

# Build fresh (if you change code)
docker compose up --build

# Open shell in running container
docker exec -it cicd-learning-backend-1 bash

# See volume contents
docker volume ls
docker volume inspect cicd-learning_backend_data
```

---

## **What to Do Next**

### **Today/Tomorrow:**
- ✅ Get it running locally
- ✅ Add/delete items to understand the flow
- ✅ Stop and restart to test persistence
- ✅ Read the code in `backend_app.py` (Flask basics)

### **This Week (Week 1):**
- Learn what each file does
- Modify `backend_app.py` to add a new endpoint
- Rebuild: `docker compose up --build`
- Test the new endpoint

### **Next Week (Week 2):**
- Push to Docker Hub
- Follow CICD_Study_Roadmap.md

---

## **Debugging Tips**

**App won't start?**
```bash
# Check logs
docker compose logs

# Check if ports are already in use
netstat -an | grep 80
netstat -an | grep 5000
netstat -an | grep 5432
```

**Can't connect to backend?**
```bash
# Test inside frontend container
docker exec -it cicd-learning-frontend-1 bash
curl http://backend:5000/health
```

**Database connection issues?**
```bash
# Connect directly
docker exec -it cicd-learning-database-1 psql -U app_user -d app_database
```

---

## **Remember**

This 3-tier stack is exactly what you'll use for:
- Week 1: Get it running ✅ (you are here)
- Week 2: Push to Docker Hub
- Week 3: Add GitHub Actions CI/CD
- Week 4: Deploy to Render
- Week 5: Add monitoring (Prometheus + Grafana)

By Week 5, you'll have a **production-ready full stack** that's:
- Containerized ✅
- Automated ✅
- Monitored ✅
- Deployed live ✅

---

## **Questions?**

If stuck:
1. Check the logs: `docker compose logs`
2. Re-read this guide (especially Debugging Tips)
3. Refer to CICD_Study_Roadmap.md

**You've got this. 🚀**
