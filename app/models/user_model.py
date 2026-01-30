from datetime import datetime
from typing import Optional, List, Dict


class UserModel:
    def __init__(
        self,
        email: str,
        password: str,
        username: Optional[str] = None,
        name: Optional[str] = None,
        avatar: Optional[str] = "https://placehold.co/200x200",
        phone_number: Optional[str] = None,
        date_of_birth: Optional[str] = None,
        gender: Optional[str] = None,
        roles: List[str] = ["user"],
        status: str = "active",
        preferences: Dict = {},
        social_auth: Dict = {},
        address: Dict = {},
        metadata: Dict = {},
        created_at: datetime = None,
        updated_at: datetime = None,
        last_login_at: datetime = None
    ):
        self.email = email
        self.username = username
        self.password = password

        self.name = name
        self.avatar = avatar
        self.phoneNumber = phone_number
        self.dateOfBirth = date_of_birth
        self.gender = gender

        self.roles = roles
        self.status = status

        self.preferences = preferences
        self.socialAuth = social_auth
        self.address = address
        self.metadata = metadata

        self.createdAt = created_at or datetime.utcnow()
        self.updatedAt = updated_at or datetime.utcnow()
        self.lastLoginAt = last_login_at

    def to_dict(self):
        return {
            "email": self.email,
            "username": self.username,
            "password": self.password,

            "name": self.name,
            "avatar": self.avatar,
            "phoneNumber": self.phoneNumber,
            "dateOfBirth": self.dateOfBirth,
            "gender": self.gender,

            "roles": self.roles,
            "status": self.status,

            "preferences": self.preferences,
            "socialAuth": self.socialAuth,
            "address": self.address,
            "metadata": self.metadata,

            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt,
            "lastLoginAt": self.lastLoginAt
        }