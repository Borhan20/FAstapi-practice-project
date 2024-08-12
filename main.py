from fastapi import FastAPI,Path,Query
from pydantic import BaseModel
from typing import Optional,List

from api import users, courses, sections

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

app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)




