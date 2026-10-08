# Real-Time Log Monitoring System

A Python-based real-time log monitoring system that generates application logs, detects log events, stores them in PostgreSQL, exposes REST APIs through FastAPI, and displays live logs through a WebSocket-powered dashboard.

## Features

- Real-time application log generation
- Automatic log monitoring
- INFO, WARNING, ERROR and CRITICAL log detection
- PostgreSQL log storage
- REST API using FastAPI
- Log statistics API
- WebSocket-based real-time updates
- Live monitoring dashboard
- Swagger/OpenAPI documentation
- Automated API tests using Pytest

## Tech Stack

- Python
- FastAPI
- Uvicorn
- SQLAlchemy
- PostgreSQL
- Pydantic
- WebSockets
- Pandas
- Pytest
- HTML
- CSS
- JavaScript

## Project Architecture

```text
Application
    ↓
Log Generator
    ↓
application.log
    ↓
Log Monitor
    ↓
PostgreSQL
    ↓
FastAPI
    ↓
REST API / WebSocket+
    ↓
Live DashboardProject Structure
real-time-log-monitoring-system/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   │
│   ├── routes/
│   │   └── logs.py
│   │
│   └── services/
│       ├── log_generator.py
│       └── log_monitor.py
│
├── dashboard/
│   └── index.html
│
├── logs/
│
├── tests/
│   ├── __init__.py
│   └── test_api.py
│
├── .gitignore
├── requirements.txt
└── README.md

Setup
1. Clone the repository
git clone https://github.com/DevKumarBhatt/real-time-log-monitoring-system.git
cd real-time-log-monitoring-system
2. Create virtual environment
python -m venv venv
3. Activate virtual environment

Windows PowerShell:

.\venv\Scripts\Activate.ps1
4. Install dependencies
pip install -r requirements.txt
Environment Variables

Create a .env file:

DATABASE_URL=postgresql+psycopg2://postgres:YOUR_PASSWORD@localhost:5432/logmonitor_db

Replace YOUR_PASSWORD with your PostgreSQL password.

Running the Project
Start FastAPI
uvicorn app.main:app --reload

API:

http://127.0.0.1:8000

Swagger documentation:

http://127.0.0.1:8000/docs
Start Log Generator

Open another terminal:

python -m app.services.log_generator
Start Log Monitor

Open another terminal:

python -m app.services.log_monitor
Dashboard

Open:

http://127.0.0.1:8000/dashboard

The dashboard provides:

Total log count
INFO count
WARNING count
ERROR count
CRITICAL count
Live log stream
WebSocket connection status
API Endpoints
Method	Endpoint	Description
GET	/	API status
GET	/health	Health check
GET	/logs/	Retrieve logs
GET	/logs/stats	Log statistics
WebSocket	/ws/logs	Real-time log stream
GET	/dashboard	Monitoring dashboard
Testing

Run:

python -m pytest -v

Current test result:

4 passed

Tests cover:

Root endpoint
Health endpoint
Logs endpoint
Statistics endpoint
Future Improvements
Email and Slack alerts
Log filtering and search
Date/time based analytics
Error-rate monitoring
Authentication and authorization
Docker deployment
Redis/Celery integration
Advanced log analytics
Production deployment
Author

Dev Kumar Bhatt

GitHub: https://github.com/DevKumarBhatt