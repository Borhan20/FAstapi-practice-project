from sqlalchemy.orm import Session
from db.models.course import Course
from pydantic_schemas.course import CourseCreate
from db import models
from pydantic_schemas import course
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select


# def get_user(db: Session, user_id: int):
#     return db.query(User).filter(User.id == user_id).first()

async def get_course(db: AsyncSession, course_id: int): 
    query = select(Course).where(Course.id == course_id)
    result = await db.execute(query)
    return result.scalar_one_or_none()

def get_course_by_name(db: Session, name: str): 
    return db.query(Course).filter(Course.name == name).first()


# def get_user_by_email(db: Session, email: str):
#     return db.query(User).filter(User.email == email).first()


def get_courses(db: Session, skip: int = 0, limit: int = 100):
    print("in utils")
    courses =  db.query(Course).offset(skip).limit(limit).all()
    print("out from utils")
    return courses

def get_courses_by_user(user_id: int, db: Session, skip: int = 0, limit: int =100): 
    courses = db.query(Course).filter(Course.user_id == user_id).offset(skip).limit(limit).all()
    return courses

def create_courses(db: Session, course: CourseCreate):
    db_course = Course(name = course.name, user_id = course.user_id)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course