import os
from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from dotenv import load_dotenv

from app.routes.auth import router as auth_router
from app.routes.user import router as user_router

from app.middlewares.error_handler import (
    http_exception_handler,
    general_exception_handler
)

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

app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(Exception, general_exception_handler)

# 🔥 API VERSIONING
app.include_router(
    auth_router,
    prefix="/api/v1"
)

app.include_router(
    user_router,
    prefix="/api/v1"
)


@app.get("/")
def read_root():
    return {
        "success": True,
        "message": "Server is running",
        "data": {
            "env": "production" if isProduction else "development"
        },
        "error": None
    }