from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    username: str
    date_of_birth: str

class UserCreate(UserBase):
    password: str  # only during signup

class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True