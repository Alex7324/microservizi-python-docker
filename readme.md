# Modern Microservices Architecture 🚀

This repository contains a proof-of-concept for a modern, containerized microservices architecture. It demonstrates how to decouple application logic into independent, scalable services that communicate over a virtual network.

## 🏗 System Architecture

The ecosystem is composed of 4 independent containers:

1. **Frontend (Streamlit):** An interactive web dashboard that acts as the user-facing entry point.
2. **Users API (FastAPI):** A stateful REST API responsible for handling user data and interacting directly with the database.
3. **Orders API (FastAPI):** A stateless REST API that demonstrates service-to-service communication by querying the Users API over the internal Docker network.
4. **Database (PostgreSQL):** A persistent relational database equipped with Docker Volumes to prevent data loss upon container destruction.

## 🛠 Tech Stack

- **Backend:** Python 3.10, FastAPI, Uvicorn, Requests
- **Frontend:** Streamlit
- **Database:** PostgreSQL, Psycopg2
- **DevOps:** Docker, Docker Compose

## 🚀 How to Run locally

Make sure you have Docker and Docker Compose installed on your machine.

1. Clone this repository:
   ```bash
   git clone <your-repository-url>
   ```

2. Navigate to the root directory and spin up the cluster:
   ```bash
   docker-compose up --build
   ```

3. Access the services:
   - **Web Dashboard:** `http://localhost:8501`
   - **Users API Swagger Docs:** `http://localhost:8001/docs`
   - **Orders API Swagger Docs:** `http://localhost:8002/docs`

## 🧠 Core Concepts Demonstrated
- Monolith to Microservices decoupling.
- Containerization and Virtual Networking (Docker Compose).
- Stateful vs Stateless application design.
- Persistent Data Storage (Docker Volumes).
- Graceful Degradation in service-to-service HTTP communication.