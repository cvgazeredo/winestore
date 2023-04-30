from datetime import datetime
from typing import List

from pydantic import BaseModel

from model import Order
from schemas import ItemSchema


class OrderSchema(BaseModel):
    id: int
    total: float
    status: bool
    created_at: datetime
    items: List[ItemSchema]

class CreateOrderSchema(BaseModel):
    id: int
    item: ItemSchema

class ListOrdersSchema(BaseModel):
    orders: List[OrderSchema]


class ItemOrderSchema(BaseModel):
    id: int

class OrderBuySchema(BaseModel):
    id: int


def list_order(order: OrderSchema):
    order = {
        "id": order.id,
        "status": order.status,
        "order_total": order.total,
        "created_at": order.created_at,
        "items": [
            {
                "id": item.id,
                "quantity": item.quantity,
                "product_id": item.product.id,
                "product_label": item.product.label,
                "price": item.product.price,
            } for item in order.items ]
    }
    return {"order": order}


def list_orders(orders: List[Order]):
    result = []
    for order in orders:
        for item in order.items:
            total = (item.product.price * item.quantity)
            print(total)
        result.append({
            "id": order.id,
            "status": order.status,
            "order_total": order.total,
            "created_at": order.created_at,
            "items": [
                {
                    "id": item.id,
                    "quantity": item.quantity,
                    "product_id": item.product_id,
                    "product_label": item.product.label,
                    "price": item.product.price,
                    "total_for_item": (item.quantity * item.product.price)
                } for item in order.items
            ]
        })

    return {"orders": result}
