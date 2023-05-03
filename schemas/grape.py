from typing import List

from pydantic import BaseModel

from model import Grape


class GrapeSchema(BaseModel):
    id: int
    name: str


class ListGrapesSchema(BaseModel):
    grapes: List[GrapeSchema]

