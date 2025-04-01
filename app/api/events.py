from fastapi import APIRouter, HTTPException
from ..models.event import Event
from ..db.mongodb import db

router = APIRouter(prefix="/api/events", tags=["events"])


@router.post("/")
async def create_event(event: Event):
    # Verify event type exists
    event_type = await db.db.event_types.find_one(
        {"name": event.event_type, "active": True}
    )

    if not event_type:
        raise HTTPException(status_code=400, detail="Invalid event type")

    result = await db.db.events.insert_one(event.dict())
    return {"id": str(result.inserted_id)}


@router.get("/")
async def get_events():
    events = await db.db.events.find().to_list(None)
    return events
