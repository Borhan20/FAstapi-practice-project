import fastapi
from fastapi import Path, Query
from api.utils.users import get_users, create_user, get_user,get_user_by_email,get_users_courses
from api.utils.course import get_courses_by_user
from pydantic_schemas.user import User, UserCreate, UsersWithCourses
from typing import Optional,List
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from fastapi import HTTPException, WebSocketException
from pydantic_schemas.course import Course
from db import models

from db.db_setup import get_db, get_async_db

router = fastapi.APIRouter()



@router.get("/users/courses", response_model= List[UsersWithCourses])
async def read_users_courses(skip: int =0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users_courses(db=db, skip=skip, limit=limit)
    return users

@router.get("/users", response_model= List[User])
async def read_users(skip: int =0, limit: int = 100, db: Session = Depends(get_db)):
    print("start")
    users = get_users(db = db, skip=skip, limit=limit)
    print(users)
    return users


@router.post("/users", response_model=User, status_code= 201)
async def crete_new_users(user: UserCreate, db: Session = Depends(get_db)): 
    db_user = get_user_by_email(db=db, email = user.email)  
    if db_user: 
        raise HTTPException(status_code=400, detail="user already exists")
    return create_user(db=db, user=user)

# @router.get("/users/{user_id}", response_model=User, status_code= 200)
# async def get_user_by_id(user_id: int ,db: Session = Depends(get_db) ):
#     db_user = get_user(db=db, user_id=user_id)
#     if db_user is None: 
#         raise HTTPException(status_code=404, detail="user not found")
#     return db_user

@router.get("/users/{user_id}", response_model=User, status_code= 200)
async def get_user_by_id(user_id: int ,db: AsyncSession = Depends(get_async_db) ):
    db_user = await get_user(db=db, user_id=user_id)
    if db_user is None: 
        raise HTTPException(status_code=404, detail="user not found")
    return db_user

@router.get("/users/{user_id}/courses", response_model=List[Course], status_code=200)
async def read_courses_by_user(user_id: int, skip: int =0, limit: int = 100, db: Session = Depends(get_db)): 
    courses = get_courses_by_user(user_id = user_id,db=db, skip=skip, limit=limit)
    print(courses)
    return courses
