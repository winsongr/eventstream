from fastapi import APIRouter, HTTPException
from ..models.event_type import EventType
from ..db.mongodb import db

router = APIRouter(prefix="/api/event-types", tags=["event_types"])


@router.post("/")
async def create_event_type(event_type: EventType):
    result = await db.db.event_types.insert_one(event_type.dict())
    return {"id": str(result.inserted_id)}


@router.get("/")
async def get_event_types():
    event_types = await db.db.event_types.find({"active": True}).to_list(None)
    return event_types
