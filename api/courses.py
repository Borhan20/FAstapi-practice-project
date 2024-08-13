import fastapi
from fastapi import Path, Query
from api.utils.course import get_course, create_courses, get_courses,get_course_by_name
from pydantic_schemas.course import Course, CourseCreate
from typing import Optional,List
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from fastapi import HTTPException, WebSocketException

from db.db_setup import get_async_db, get_db

router = fastapi.APIRouter()

@router.get("/courses", response_model= List[Course])
async def read_courses(skip: int =0, limit: int = 100, db: Session = Depends(get_db)):
    print("start")
    users = get_courses(db = db, skip=skip, limit=limit)
    print(users)
    return users


@router.post("/courses", response_model=Course, status_code= 201)
async def crete_new_course(course: CourseCreate, db: Session = Depends(get_db)): 
    db_user = get_course_by_name(db=db, name = course.name)  
    if db_user: 
        raise HTTPException(status_code=400, detail="course already exists")
    return create_courses(db=db, course=course)

# @router.get("/users/{user_id}", response_model=User, status_code= 200)
# async def get_user_by_id(user_id: int ,db: Session = Depends(get_db) ):
#     db_user = get_user(db=db, user_id=user_id)
#     if db_user is None: 
#         raise HTTPException(status_code=404, detail="user not found")
#     return db_user

@router.get("/courses/{course_id}", response_model=Course, status_code= 200)
async def get_user_by_id(course_id: int ,db: AsyncSession = Depends(get_async_db) ):
    db_user = await get_course(db=db, user_id=course_id)
    if db_user is None: 
        raise HTTPException(status_code=404, detail="user not found")
    return db_user
