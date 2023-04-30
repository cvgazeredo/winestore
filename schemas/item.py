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


class ListItemsSchema(BaseModel):
    items: List[ItemSchema]



def list_item(item: Item):
    return {
        "id": item.id,
        "quantity": item.quantity,
        "product": {
                "id": item.product_id,
                "label": item.product.label,
                "price": item.product.price
        }
    }


def list_items(items: List[Item]):

    result = []
    for item in items:
        result.append({
            "id": item.id,
            "quantity": item.quantity,
            "product": {
                "id": item.product_id,
                "label": item.product.label,
                "price": item.product.price
            }
        })

    return {"items": result}
