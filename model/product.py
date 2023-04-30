from sqlalchemy import Table, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from model import Base

product_grapes = Table(
    "product_grapes",
    Base.metadata,
    Column("product_id", ForeignKey("product.id")),
    Column("grape_id", ForeignKey("grape.id")),
)


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True)
    label = Column(String(100), unique=True)
    photo = Column(String(4000))
    price = Column(Float)
    type_id = Column(Integer, ForeignKey("type.id"))
    type = relationship("Type", back_populates="products")
    country_id = Column(Integer, ForeignKey("country.id"))
    country = relationship("Country", back_populates="products")
    grapes = relationship("Grape", secondary=product_grapes, back_populates="products")
    item = relationship("Item")

    def __init__(self, id, label, photo, price, type, country, grapes):
        self.id = id
        self.label = label
        self.photo = photo
        self.price = price
        self.type = type
        self.country = country
        self.grapes = grapes

