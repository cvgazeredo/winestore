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
from model.user import User
from seed import seed_database

db_path = "database/"
if not os.path.exists(db_path):
    os.makedirs(db_path)

url = URL.create(
    drivername="postgresql",
    username=os.getenv('DB_USERNAME'),
    password=os.getenv('DB_PASSWORD'),
    host="localhost",
    database= os.getenv('DB_NAME'),
    port=os.getenv('DB_PORT')
)

print(url)

engine = create_engine(url)

Session = sessionmaker(bind=engine)

Base.metadata.drop_all(engine)

Base.metadata.create_all(engine)

seed_database(url)



