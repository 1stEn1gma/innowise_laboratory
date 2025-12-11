from typing import Optional, List

from pydantic import BaseModel
from sqlalchemy import null


class BookBase(BaseModel):
    title: str
    author: str


class BookCreate(BookBase):
    year: int | None = null()


class Book(BookBase):
    id: int
    year: Optional[int]


class BaseResponse(BaseModel):
    status: int
    data: None
    details: None


class ResponseForBooks(BaseResponse):
    data: List[Book]
