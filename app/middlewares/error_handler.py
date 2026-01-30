from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException

from app.utils.response import error_response


async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content=error_response(
            message=exc.detail,
            code=exc.status_code,
            error_type="HTTP_EXCEPTION"
        )
    )


async def general_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content=error_response(
            message="Internal server error",
            code=500,
            error_type="SERVER_ERROR"
        )
    )