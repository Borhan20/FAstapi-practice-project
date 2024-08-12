import fastapi
from fastapi import Path, Query
from pydantic import BaseModel
from typing import Optional,List

router = fastapi.APIRouter()

courses = []


class Course(BaseModel): 
    name: str
    is_active: bool 


@router.get("/course", response_model= List[Course])
async def get_courses():
    return courses


@router.post("/courses")
async def crete_courses(course: Course):
    courses.append(course)
    return {"message": "Course Created"}

@router.get("/courses/{id}")
async def get_course(
    id: int = Path(...,description="The ID of the user want to retrive", ge=2),
    q: str = Query(None    , max_length= 5)
    ):
    return {"course":  courses[id], "query": q}

@router.delete("/courses/{id}")
async def delete_course(
    id: int = Path(...,description="The ID of the user want to retrive", ge=2),
):
    return {"message": "deleted successfully"}
