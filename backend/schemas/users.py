from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime



class UserBase(BaseModel):
    email: EmailStr
    username: str
    name: str
    surname: str



class UserCreate(UserBase):
    password1: str = Field(..., min_length=4)
    password2: str = Field(..., min_length=4)


class UserResponse(UserBase):
    id: int
    created_at: datetime
    is_active: bool = True

    class Config:
        from_atributes = True


class UserInDB(UserResponse):
    hashed_password: str



class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None