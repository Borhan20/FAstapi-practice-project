from fastapi import FastAPI,Path,Query
from pydantic import BaseModel
from typing import Optional,List

app = FastAPI(
    title= "FAst API LMS",
    description= "LMS Managing Users",
    version= "0.0.1",
    contact={
        "name": "borhan",
        "email": "anamborhan.pentabd@gmail.com"
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/license/LICENSE-2.0.html"
    },
)

users = []

class User(BaseModel): 
    email: str
    is_active: bool 
    bio: Optional[str] = None


@app.get("/users", response_model= List[User])
async def get_users():
    return users


@app.post("/users")
async def crete_users(user: User):
    users.append(user)
    return {"message": "User Created"}

@app.get("/users/{id}")
async def get_user(
    id: int = Path(...,description="The ID of the user want to retrive", ge=2),
    q: str = Query(None    , max_length= 5)
    ):
    return {"user":  users[id], "query": q}


