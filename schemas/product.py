from typing import List

from pydantic import BaseModel

from model import Product
from schemas import TypeSchema, CountrySchema, GrapeSchema


class ProductSchema(BaseModel):
    id: int
    label: str
    photo: str
    price: float
    type: TypeSchema
    country: CountrySchema
    grapes: List[GrapeSchema]


class ProductIdSchema(BaseModel):
    id: str



class ListProductsSchema(BaseModel):
    products: List[ProductSchema]


def list_products(products: List[Product]):
    result = []
    for product in products:
        result.append({
            "id": product.id,
            "label": product.label,
            "photo": product.photo,
            "price": product.price,
            "type": {
                "id": product.type.id,
                "name": product.type.name
            },
            "country": {
                "id": product.country.id,
                "name": product.country.name
            },
            "grapes": [
                {
                    "id": grape.id,
                    "name": grape.name
                } for grape in product.grapes
            ]
        })

    return {"products": result}
