from fastapi import APIRouter, Depends, Request
from app.middlewares.auth_middleware import auth_middleware
from app.utils.response import success_response
from app.schemas.user_schema import UpdateProfileDTO

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


@router.put("/me")
def update_profile(
    request: Request,
    payload: UpdateProfileDTO,
    _: None = Depends(auth_middleware)
):
    user_id = request.state.user_id

    update_data = {
        k: v for k, v in payload.dict().items()
        if v is not None
    }

    if not update_data:
        raise HTTPException(
            status_code=400,
            detail="Nothing to update"
        )

    user_collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": update_data}
    )

    user = user_collection.find_one({"_id": ObjectId(user_id)})

    user["id"] = str(user["_id"])
    del user["_id"]
    user.pop("password", None)

    return success_response(
        message="Profile updated successfully",
        data={"user": user}
    )

@router.patch("/me")
def update_profile(
    request: Request,
    payload: UpdateProfileDTO,
    _: None = Depends(auth_middleware)
):
    user_id = request.state.user_id

    update_data = {
        k: v for k, v in payload.dict().items()
        if v is not None
    }

    if not update_data:
        raise HTTPException(
            status_code=400,
            detail="Nothing to update"
        )

    user_collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": update_data}
    )

    user = user_collection.find_one({"_id": ObjectId(user_id)})

    user["id"] = str(user["_id"])
    del user["_id"]
    user.pop("password", None)

    return success_response(
        message="Profile updated successfully",
        data={"user": user}
    )