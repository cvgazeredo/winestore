from logger import logger

from flask import redirect
from flask_cors import CORS
from flask_openapi3 import OpenAPI, Info, Tag
from sqlalchemy.exc import IntegrityError

from model import Session, Order, Item, Product, User
from schemas import *


info = Info(title="Project 01", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

home_tag = Tag(name="Documentation", description="Select doc: Swagger, Redoc")
tag_list_products = Tag(name="Products", description="List of Products")
tag_user = Tag(name="User", description="Register user")
tag_order = Tag(name="Order", description="Finish order and buy products")
tag_cart = Tag(name="Shopping Cart", description="Add and remove items of shopping cart")


@app.get('/', tags=[home_tag])
def home():
    return redirect('/openapi')


@app.get('/products', tags=[tag_list_products],
         responses={
             "200": ProductSchema,
             "500": ErrorSchema
         })
def get_products():
    logger.debug(f"Collecting all products")
    session = Session()
    products = session.query(Product).all()

    if not products:
        return {"products": []}, 200
    else:
        logger.debug(f"%d types were found" % len(products))

        return list_products(products), 200


@app.post('/order/add', tags=[tag_cart],
          responses={
              "200": ItemSchema,
              "409": ErrorSchema
          })
def add_product_to_cart(form: ItemOrderSchema):
    product_id = form.product_id
    order_id = form.order_id

    # Start session:
    session = Session()

    item = session.query(Item).filter(Item.product_id == product_id, Item.order_id == order_id).first()
    order = session.query(Order).filter(Order.id == order_id).first()
    if not item:
        added_product = session.query(Product).filter(Product.id == product_id).first()
        item = Item(product=added_product, order=order)

    if order.status:
        error_message = "Pedido finalizado. Impossível adicionar item ao carrinho."
        logger.warning("Erro ao adicionar item ao carrinho. Pedido finalizado")

        return {"message": error_message}, 409

    item.increment_quantity()

    # Insert into item:
    session.add(item)
    session.commit()

    item.order.recalculate_total()
    session.add(item.order)
    session.commit()

    return list_order(order), 200


@app.post('/order/buy', tags=[tag_order])
def buy_order(form: OrderBuySchema):

    order_id = form.order_id
    user_id = form.user_id
    print(order_id)
    print(user_id)

    session = Session()
    order = session.query(Order).filter(Order.id == order_id).first()

    if order.status:
        error_message = "Este pedido já foi finalizado!"
        return {"message": error_message}, 409

    order.user_id = user_id
    order.status = True
    session.commit()

    return list_order(order), 200


@app.delete('/order/delete', tags=[tag_cart])
def delete_item(query: ItemSearchSchema):
    item_id = query.item_id

    logger.debug("Deleting item ")
    session = Session()

    item = session.query(Item).filter(Item.id == item_id).first()
    order = item.order

    if item.quantity == 1:
       # Delete item from order
        session.delete(item)

    else:
        # Decrease quantity
        item.quantity = item.quantity - 1
        print(item.quantity)

    session.commit()

    order.recalculate_total()

    orders = list_order(order)

    session.close()
    return orders, 200


@app.post('/user/create', tags=[tag_user])
def create_user(form: CreateUserSchema):

    name = form.name
    address = form.address

    session = Session()
    new_order = Order()
    session.add(new_order)
    session.commit()
    print(new_order.id)

    new_user = User(name=name, address=address)
    session.add(new_user)
    session.commit()

    print(new_user.id)

    return {"user_id": new_user.id,
            "order_id": new_order.id}

