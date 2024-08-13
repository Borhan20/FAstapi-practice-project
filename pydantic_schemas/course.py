from pydantic import BaseModel 
from datetime import datetime


class CourseBase(BaseModel): 
    name: str
    user_id: int


class CourseCreate(CourseBase): 
    ... 

class Course(CourseBase): 
    id: int 
    created_at: datetime
    updated_at: datetime

    class Config: 
        from_attributes = True 