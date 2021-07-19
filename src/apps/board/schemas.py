  
from datetime import datetime
from typing import List

from pydantic.main import BaseModel


class CreateCategory(BaseModel):
    name: str


class OutCategory(BaseModel):
    id: int
    name: str


class CreateToolKit(BaseModel):
    name: str


class OutToolkit(BaseModel):
    id: int
    name: str


class CreateProject(BaseModel):
    name: str
    description: str
    category: int
    toolkit: int
    team: List[int]


class OutProject(BaseModel):
    id: int
    name: str
    description: str
    create_date: datetime
    category: OutCategory
    toolkit: OutToolkit
