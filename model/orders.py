from typing import Union
from datetime import datetime

from sqlalchemy import Column, Integer, Float, DateTime, Boolean
from sqlalchemy.orm import relationship

from model import Base, Item


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    total = Column(Float, default=0)
    created_at = Column(DateTime, default=datetime.now())
    items = relationship("Item", back_populates="order")
    status = Column(Boolean, default=False)

    def __init__(self, created_at: Union[DateTime, None] = None):

        if created_at:
            self.created_at = created_at

    def recalculate_total(self):
        self.total = 0
        for item in self.items:
            self.total = self.total + item.product.price * item.quantity

