from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .db.mongodb import db
from .api import events, event_types
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="CDP Platform")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount admin UI static files
app.mount("/admin", StaticFiles(directory="admin", html=True), name="admin")

# Include routers
app.include_router(events.router)
app.include_router(event_types.router)


@app.on_event("startup")
async def startup():
    await db.connect_to_database()


@app.on_event("shutdown")
async def shutdown():
    await db.close_database_connection()
