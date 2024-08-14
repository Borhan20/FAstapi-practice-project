from pydantic import BaseModel
from datetime import datetime
from typing import List

class UserRequestBase(BaseModel):
    email: str
    role: int

class CourseRequestBase(BaseModel):
    name: str
    user_id: int


class CourseResponseBase(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class UserResponseBase(BaseModel):
    id: int
    email: str
    role: int

    class Config:
        orm_mode = True

