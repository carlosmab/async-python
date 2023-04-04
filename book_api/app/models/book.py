from typing import List
from pydantic import BaseModel

class BookBase(BaseModel):
    title: str
    author_id: int
    year: int
    description: str

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int

    class Config:
        orm_mode = True