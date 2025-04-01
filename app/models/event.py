from pydantic import BaseModel
from datetime import datetime
from typing import Dict, Any


class Event(BaseModel):
    event_type: str
    data: Dict[str, Any]
    timestamp: datetime = datetime.utcnow()
    user_id: str
