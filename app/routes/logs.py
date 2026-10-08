from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database import get_db
from app.models import Log
from app.schemas import LogResponse


router = APIRouter(
    prefix="/logs",
    tags=["Logs"]
)


@router.get("/", response_model=list[LogResponse])
def get_logs(db: Session = Depends(get_db)):

    logs = (
        db.query(Log)
        .order_by(Log.timestamp.desc())
        .all()
    )

    return logs


@router.get("/stats")
def get_log_stats(db: Session = Depends(get_db)):

    total = db.query(Log).count()

    info = db.query(Log).filter(Log.level == "INFO").count()
    warning = db.query(Log).filter(Log.level == "WARNING").count()
    error = db.query(Log).filter(Log.level == "ERROR").count()
    critical = db.query(Log).filter(Log.level == "CRITICAL").count()

    return {
        "total": total,
        "INFO": info,
        "WARNING": warning,
        "ERROR": error,
        "CRITICAL": critical
    }