from pydantic import BaseModel

class Book(BaseModel):
    id: int
    author: str
    country: str
    imageLink: str
    language: str
    link: str
    pages: int
    title: str
    year: int

class BookUpdateModel(BaseModel):
    author: str
    country: str
    imageLink: str
    language: str
    link: str
    pages: int
   