from pydantic import BaseModel, EmailStr
from typing import Optional
from backend.app.schemas.enums import UserRole

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    name: str
    role: UserRole = UserRole.STAFF

class UserResponse(BaseModel):
    id: str
    username: str
    email: str
    name: str
    role: UserRole
    is_active: bool

class LoginRequest(BaseModel):
    username: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserResponse
