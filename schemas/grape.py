from typing import List

from pydantic import BaseModel

from model import Grape


class GrapeSchema(BaseModel):
    id: int
    name: str


class ListGrapesSchema(BaseModel):
    grapes: List[GrapeSchema]


def list_grapes(grapes: List[Grape]):
    result = []
    for grape in grapes:
        result.append({
            "id": grape.id,
            "name": grape.name
        })

    return {"grapes": result}


