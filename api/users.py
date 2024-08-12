import fastapi
from fastapi import Path, Query
from pydantic import BaseModel
from typing import Optional,List

router = fastapi.APIRouter()

users = []

class User(BaseModel): 
    email: str 
    is_active: bool 
    bio: Optional[str] = None

class User(BaseModel): 
    email: str
    is_active: bool 
    bio: Optional[str] = None


@router.get("/users", response_model= List[User])
async def get_users():
    return users


@router.post("/users")
async def crete_users(user: User):
    users.append(user)
    return {"message": "User created"}

@router.get("/users/{id}")
async def get_user(
    id: int = Path(...,description="The ID of the user want to retrive", ge=2),
    q: str = Query(None    , max_length= 5)
    ):
    return {"user":  users[id], "query": q}
