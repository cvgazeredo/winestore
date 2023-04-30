from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from model import Base


class Item(Base):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True)
    quantity = Column(Integer, default=0)
    product_id = Column(Integer, ForeignKey("product.id"))
    product = relationship("Product", back_populates="item")
    order_id = Column(Integer, ForeignKey("orders.id"))
    order = relationship("Order", back_populates="items")

    def __init__(self, product, order):
        self.product = product
        self.order = order
        self.quantity = 0

    def increment_quantity(self):
        self.quantity = self.quantity + 1
