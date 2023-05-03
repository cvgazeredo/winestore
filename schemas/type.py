from typing import List

from pydantic import BaseModel

from model import Type



class TypeSchema(BaseModel):
    id: int
    name: str


