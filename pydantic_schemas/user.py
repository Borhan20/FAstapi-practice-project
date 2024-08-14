from pydantic import BaseModel
from datetime import datetime
from typing import List
from .commonbase import UserRequestBase,CourseResponseBase

# class CourseBase(BaseModel):
#     id: int
#     name: str

#     class Config:
#         orm_mode = True

# class UserBase(BaseModel):
#     email: str
#     role: int

class UserCreate(UserRequestBase):
    pass

class User(UserRequestBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class UsersWithCourses(User):
    courses: List[CourseResponseBase] = []

    class Config:
        orm_mode = True
