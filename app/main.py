import os
from fastapi import FastAPI
from dotenv import load_dotenv

from app.routes.auth import router

load_dotenv()

ENV = os.getenv("ENV")
isProduction = ENV == "production"

app = FastAPI(
    title="FastAPI Auth Service",
    version="1.0.1",
    docs_url=None if isProduction else "/docs",
    redoc_url=None if isProduction else "/redoc",
    openapi_url=None if isProduction else "/openapi.json"
)




# 👇 API versioning (industry standard)
app.include_router(
    router,
    prefix="/api/v1"
)


@app.get("/")
def read_root():
    return {
        "message": "Server is running",
        "env": "production" if isProduction else "development",
        "status": "success",
        "status_code": 200
    }