from datetime import datetime

from pydantic import BaseModel


class LogResponse(BaseModel):
    id: int
    level: str
    message: str
    source: str | None = None
    timestamp: datetime

    class Config:
        from_attributes = True