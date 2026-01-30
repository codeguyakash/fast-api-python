from fastapi import APIRouter, Depends, Request
from app.middlewares.auth_middleware import auth_middleware
from app.utils.response import success_response

from app.models.user_model import UserModel

router = APIRouter(prefix="/user", tags=["User"])


from bson import ObjectId
from app.config.db import user_collection

@router.get("/me")
def profile(request: Request, _: None = Depends(auth_middleware)):
    user_id = request.state.user_id

    user = user_collection.find_one({"_id": ObjectId(user_id)})

    if user:
        user["id"] = str(user["_id"])
        del user["_id"]
        if "password" in user:
            del user["password"]

    return success_response(
        message="Profile fetched successfully",
        data={
            "user": user
        }
    )