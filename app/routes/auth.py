from fastapi import APIRouter, HTTPException
from passlib.context import CryptContext
from datetime import datetime

from app.schemas.user_schema import UserRegister, UserLogin
from app.models.user_model import UserModel
from app.config.db import user_collection
from app.utils.jwt import create_access_token
from app.utils.response import success_response


router = APIRouter(prefix="/auth", tags=["Auth"])

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/register")
def register(user: UserRegister):

    existing_user = user_collection.find_one(
        {"email": user.email}
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="User already exists"
        )

    hashed_password = pwd_context.hash(user.password)

    new_user = UserModel(
        email=user.email,
        password=hashed_password,
        name=user.name
    )

    result = user_collection.insert_one(new_user.to_dict())

    return success_response(
        message="User registered successfully",
        code=201,
        data={
            "user": {
                "id": str(result.inserted_id),
                "name": user.name,
                "email": user.email
            }
        }
    )

@router.post("/login")
def login(user: UserLogin):

    db_user = user_collection.find_one(
        {"email": user.email}
    )

    if not db_user:
        raise HTTPException(400, "Invalid email or password")

    if not pwd_context.verify(user.password, db_user["password"]):
        raise HTTPException(400, "Invalid email or password")

    user_collection.update_one(
        {"_id": db_user["_id"]},
        {"$set": {"lastLoginAt": datetime.utcnow()}}
    )

    access_token = create_access_token({
        "id": str(db_user["_id"]),
        "name": db_user["name"],
        "email": db_user["email"]
    })

    return success_response(
        message="Login successful",
        data={
            "user": {
                "id": str(db_user["_id"]),
                "name": db_user["name"],
                "email": db_user["email"]
            },
            "access_token": access_token
        }
    )