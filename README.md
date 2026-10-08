# 🔎 Real-Time Log Monitoring System

A Python-based real-time log monitoring system that generates application
logs, detects log events, stores them in PostgreSQL, exposes REST APIs
through FastAPI, and displays live logs through a WebSocket-powered dashboard.

---

## 🚀 Key Features

- 🔄 Real-time application log generation
- 👀 Automatic log monitoring
- 🚦 INFO, WARNING, ERROR and CRITICAL log detection
- 🗄️ PostgreSQL log storage
- ⚡ FastAPI REST APIs
- 📡 WebSocket-based real-time updates
- 📊 Live monitoring dashboard
- 📈 Log statistics API
- 📚 Swagger / OpenAPI documentation
- 🧪 Automated API testing with Pytest

---

## 🏗️ System Architecture

```text
                ┌──────────────────────┐
                │    Log Generator     │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │   application.log    │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │     Log Monitor      │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │     PostgreSQL       │
                │     logmonitor_db    │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │       FastAPI        │
                │      REST API        │
                └──────────┬───────────┘
                           │
                ┌──────────┴───────────┐
                ▼                      ▼
        ┌───────────────┐      ┌───────────────┐
        │   Dashboard   │      │ API Clients   │
        │  WebSocket    │      │   / Swagger   │
        └───────────────┘      └───────────────┘
🛠️ Tech Stack
Technology	Purpose
Python	Core application
FastAPI	REST API
PostgreSQL	Log storage
WebSocket	Real-time updates
Pytest	API testing
HTML / CSS / JavaScript	Dashboard
Swagger / OpenAPI	API documentation
📂 Project Structure
real-time-log-monitoring-system/
│
├── app/
│   ├── main.py
│   ├── routes/
│   ├── schemas.py
│   └── ...
│
├── dashboard/
│   └── ...
│
├── tests/
│   └── ...
│
├── log_generator.py
├── log_monitor.py
├── requirements.txt
├── .gitignore
└── README.md
⚙️ How It Works
1. Generate Logs

The log generator continuously creates application logs.

2. Monitor Logs

The monitoring service detects newly generated log entries.

3. Store Logs

Detected logs are processed and stored in PostgreSQL.

4. Expose API

FastAPI provides REST endpoints for accessing the stored logs and
statistics.

5. Real-Time Dashboard

WebSocket communication allows the dashboard to receive live log updates.

▶️ Getting Started
Clone the repository
git clone https://github.com/DevKumarBhatt/real-time-log-monitoring-system.git
Go to the project directory
cd real-time-log-monitoring-system
Create virtual environment
python -m venv venv
Activate virtual environment

Windows:

venv\Scripts\activate
Install dependencies
pip install -r requirements.txt
Configure PostgreSQL

Create the required PostgreSQL database and configure the database
connection used by the application.

Run the application
uvicorn app.main:app --reload
📚 API Documentation

After starting the FastAPI server, API documentation is available through
Swagger/OpenAPI.

http://127.0.0.1:8000/docs
🧪 Testing

The project includes automated API tests using Pytest.

Run:

pytest
📊 Dashboard

The project includes a live monitoring dashboard that displays
application log activity and real-time updates.

🔮 Future Improvements
🔐 API authentication and authorization
🚨 Email / notification alerts for critical errors
🐳 Docker deployment
☁️ Cloud deployment
📊 Advanced log analytics
🔍 Log search and filtering
👥 Multi-user monitoring
📈 Historical log visualizations
👨‍💻 Author
Dev Kumar Bhatt

Python Developer | Data Analyst | Backend Developer

GitHub:
https://github.com/DevKumarBhatt

LinkedIn:
https://linkedin.com/in/dev-kumar-bhatt-b74540347
