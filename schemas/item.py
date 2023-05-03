from typing import List

from pydantic import BaseModel

from model import Item
from schemas import ProductSchema


class ItemSchema(BaseModel):
    id: int
    quantity: int = 0
    product: ProductSchema = "Vinho X"


class ItemSearchSchema(BaseModel):
    item_id: int


class ItemOrderSchema(BaseModel):
    product_id: int
    quantity: int = 0
    order_id: int

