from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import relationship

from model import Base


class Country(Base):
    __tablename__ = "country"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    products = relationship("Product", back_populates="country")

    def __init__(self, id, name):
        self.id = id
        self.name = name

