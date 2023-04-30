import os
from sqlalchemy import URL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model.base import Base
from model.country import Country
from model.grape import Grape
from model.item import Item
from model.orders import Order
from model.product import Product
from model.type import Type


db_path = "database/"
if not os.path.exists(db_path):
    os.makedirs(db_path)

url = URL.create(
    drivername="postgresql",
    username="postgres",
    password="12345",
    host="localhost",
    database="winestore",
    port=5432
)
print(url)

engine = create_engine(url)

Session = sessionmaker(bind=engine)

Base.metadata.create_all(engine)