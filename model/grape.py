from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from model import Base
from model.product import product_grapes


class Grape(Base):
    __tablename__ = "grape"

    id = Column(Integer, primary_key=True)
    name = Column(String(40), unique=True)
    products = relationship("Product", secondary=product_grapes, back_populates="grapes")

    def __init__(self, id, name):
        self.id = id
        self.name = name

