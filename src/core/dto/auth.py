from uuid import UUID
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserToDBBase(UserBase):
    username: str
    email: EmailStr


class User(UserToDBBase):
    is_active: bool = True
    is_admin: bool = False
    is_manager: bool = False
    is_customer: bool = True


class UserInDB(UserToDBBase):
    password_hash: str


class FullUser(UserInDB):
    id: UUID


class UserId(BaseModel):
    user_id: UUID
