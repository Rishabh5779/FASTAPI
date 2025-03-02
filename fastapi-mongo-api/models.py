
# models.py
from pydantic import BaseModel

class Book(BaseModel):
    name: str
    img: str
    summary: str