import asyncio

from fastapi import FastAPI, WebSocket
from fastapi.responses import FileResponse

from app.database import Base, engine, SessionLocal
from app.models import Log
from app.routes.logs import router as logs_router


# Create database tables
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Real-Time Log Monitoring System",
    description="API for monitoring and analyzing application logs",
    version="1.0.0"
)


# Register routes
app.include_router(logs_router)


@app.get("/")
def home():
    return {
        "message": "Real-Time Log Monitoring System is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


# Dashboard
@app.get("/dashboard")
def dashboard():
    return FileResponse("dashboard/index.html")


# WebSocket for real-time logs
@app.websocket("/ws/logs")
async def websocket_logs(websocket: WebSocket):

    await websocket.accept()

    db = SessionLocal()

    try:
        latest_log = (
            db.query(Log)
            .order_by(Log.id.desc())
            .first()
        )

        last_id = latest_log.id if latest_log else 0

    finally:
        db.close()

    try:
        while True:

            db = SessionLocal()

            try:
                new_logs = (
                    db.query(Log)
                    .filter(Log.id > last_id)
                    .order_by(Log.id.asc())
                    .all()
                )

                for log in new_logs:

                    await websocket.send_json({
                        "id": log.id,
                        "level": log.level,
                        "message": log.message,
                        "source": log.source,
                        "timestamp": log.timestamp.isoformat()
                    })

                    last_id = log.id

            finally:
                db.close()

            await asyncio.sleep(1)
   
   
    except Exception:
        pass 