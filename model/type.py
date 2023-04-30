from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from model import Base


class Type(Base):
    __tablename__ = "type"

    id = Column(Integer, primary_key=True)
    name = Column(String(40), unique=True)
    products = relationship("Product", back_populates="type")

    def __init__(self, id, name):
        self.id = id
        self.name = name

