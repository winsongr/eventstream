from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class EventType(BaseModel):
    name: str
    description: Optional[str]
    schema: dict
    created_at: datetime = datetime.utcnow()
    active: bool = True
