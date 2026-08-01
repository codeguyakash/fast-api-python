from pydantic import BaseModel, EmailStr
from typing import Optional


class UserRegister(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UpdateProfileDTO(BaseModel):
    name: Optional[str] = None
    username: Optional[str] = None
    phoneNumber: Optional[str] = None
    avatar: Optional[str] = None
    gender: Optional[str] = None
    dateOfBirth: Optional[str] = None
    address: Optional[dict] = None
    preferences: Optional[dict] = None
    role: Optional[str] = None