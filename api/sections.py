import fastapi
from fastapi import Path, Query
from pydantic import BaseModel
from typing import Optional,List

router = fastapi.APIRouter()

sections = []

class Section(BaseModel): 
    name: str 
     



@router.get("/sections", response_model= List[Section])
async def get_sections():
    return sections


@router.post("/sections")
async def crete_sections(section: Section):
    sections.append(section)
    return {"message": "Section created"}

@router.get("/sections/{id}")
async def get_section(
    id: int = Path(...,description="The ID of the user want to retrive", ge=2),
    q: str = Query(None    , max_length= 5)
    ):
    return {"user":  sections[id], "query": q}
