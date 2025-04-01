from fastapi import FastAPI
import uvicorn

app = FastAPI(
    title="EventStream",
    description="EventStream is a MicroCDP",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
