from fastapi import APIRouter, HTTPException
from passlib.context import CryptContext
from datetime import datetime

from app.schemas.user_schema import UserRegister, UserLogin
from app.models.user_model import UserModel
from app.config.db import user_collection


router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# ---------------- REGISTER ----------------
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

    password = pwd_context.hash(user.password)

    new_user = UserModel(
        email=user.email,
        password=password,
        name=user.name
    )

    user_collection.insert_one(new_user.to_dict())

    return {
        "message": "User registered successfully"
    }


# ---------------- LOGIN ----------------
@router.post("/login")
def login(user: UserLogin):

    db_user = user_collection.find_one(
        {"email": user.email}
    )

    if not db_user:
        raise HTTPException(
            status_code=400,
            detail="Invalid email or password"
        )

    if not pwd_context.verify(user.password, db_user["password"]):
        raise HTTPException(
            status_code=400,
            detail="Invalid email or password"
        )

    user_collection.update_one(
        {"_id": db_user["_id"]},
        {"$set": {"lastLoginAt": datetime.utcnow()}}
    )

    return {
        "message": "Login successful",
        "email": db_user["email"]
    }