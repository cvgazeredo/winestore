from typing import List

from pydantic import BaseModel

from model import Type



class TypeSchema(BaseModel):
    id: int
    name: str


class ListTypesSchema(BaseModel):
    types: List[TypeSchema]


def list_types(types: List[Type]):

    result = []
    for type in types:
        result.append({
            "id": type.id,
            "name": type.name,
            "products":  [
                {
                    "id": product.id,
                    "name": product.label
                } for product in type.products
            ]
        })

    return {"types": result}

