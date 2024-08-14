from pydantic import BaseModel
from datetime import datetime
from typing import List
from .commonbase import CourseRequestBase,UserResponseBase

# class UserBase(BaseModel):
#     id: int
#     email: str
#     role: int

#     class Config:
#         orm_mode = True

# class CourseBase(BaseModel):
#     name: str
#     user_id: int

class CourseCreate(CourseRequestBase):
    pass

class Course(CourseRequestBase):
    id : int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class CourseWithStudents(Course):
    created_by : UserResponseBase

    class Config:
        orm_mode = True
