from sqlalchemy.orm import Session
from db.models.user import User
from pydantic_schemas.user import UserCreate, UsersWithCourses
from db import models
from pydantic_schemas import user
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select


# def get_user(db: Session, user_id: int):
#     return db.query(User).filter(User.id == user_id).first()



async def get_user(db: AsyncSession, user_id: int): 
    query = select(User).where(User.id == user_id)
    result = await db.execute(query)
    return result.scalar_one_or_none()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    print("in utils")
    users =  db.query(User).offset(skip).limit(limit).all()
    print("out from utils")
    return users

def get_users_courses(db: Session, skip: int = 0, limit: int = 100):
    print("in utils")
    users =  db.query(User).offset(skip).limit(limit).all()
    print("out from utils")
    return users

def create_user(db: Session, user: UserCreate):
    db_user = User(email=user.email, role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user