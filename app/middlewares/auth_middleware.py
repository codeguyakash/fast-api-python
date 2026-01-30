from fastapi import Depends, Request, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.utils.jwt import verify_access_token

security = HTTPBearer()

async def auth_middleware(
    request: Request,
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    token = credentials.credentials   # ✅ only token

    payload = verify_access_token(token)

    request.state.user_id = payload["id"]
    request.state.user = payload

    # return payload