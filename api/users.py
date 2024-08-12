import fastapi
from fastapi import Path, Query
from api.utils.users import get_users, create_user, get_user,get_user_by_email
from pydantic_schemas.user import User, UserCreate
from typing import Optional,List
from sqlalchemy.orm import Session
from fastapi import Depends

from db.db_setup import get_db

router = fastapi.APIRouter()



@router.get("/users", response_model= List[User])
async def read_users(skip: int =0, limit: int = 100, db: Session = Depends(get_db)):
    print("start")
    users = get_users(db, skip=skip, limit=limit)
    print(users)
    return users


# @router.post("/users")
# async def crete_new_users(user: User):
#     users.append(user)
#     return {"message": "User created"}

# @router.get("/users/{id}")
# async def get_user(
#     id: int = Path(...,description="The ID of the user want to retrive", ge=2),
#     q: str = Query(None    , max_length= 5)
#     ):
#     return {"user":  users[id], "query": q}
