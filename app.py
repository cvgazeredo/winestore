from logger import logger

from flask import redirect, jsonify
from flask_cors import CORS
from flask_openapi3 import OpenAPI, Info, Tag
from sqlalchemy.exc import IntegrityError

from model import Session, Type, Grape, Country, Order, Item, Product
from schemas import *


info = Info(title="Project 01", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

home_tag = Tag(name="Documentation", description="Select doc: Swagger, Redoc")
tag_list_type = Tag(name="Type", description="List types")
tag_list_grapes = Tag(name="Grape", description="List grapes")
tag_list_countries = Tag(name="Country", description="List countries")
tag_list_orders = Tag(name="Orders", description="List orders")
tag_list_items = Tag(name="Items", description="List items")
tag_list_products = Tag(name="Products", description="List products")


@app.get('/', tags=[home_tag])
def home():
    return redirect('/openapi')


@app.get('/products',
         tags=[tag_list_products],
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


@app.post('/order/create')
def create_order():
    print("Reached create order function")
    session = Session()
    new_order = Order()
    session.add(new_order)
    session.commit()

    return {"order_id": new_order.id}


@app.post('/products/add',
          responses={
              "200": ItemSchema,
              "409": ErrorSchema
          })
def add_product_to_cart(form: ItemOrderSchema):

    print("Reached add_product_to_cart function")
    product_id = form.product_id
    order_id = form.order_id

    # Start session:
    session = Session()

    # Access
    item = session.query(Item).filter(Item.product_id == product_id, Item.order_id == order_id).first()
    order = session.query(Order).filter(Order.id == order_id).first()
    if not item:
        added_product = session.query(Product).filter(Product.id == product_id).first()
        item = Item(product=added_product, order=order)

    if order.status:
        print(order.status)
        print("Order closed. Cannot add more items")
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

    print(list_order(order))

    return list_order(order), 200


@app.post('/order/buy')
def buy_order(form: OrderBuySchema):
    print("Buy order function reached!")
    order_id = form.id

    session = Session()
    order = session.query(Order).filter(Order.id == order_id).first()

    if order.status:
        error_message = "Este pedido já foi finalizado!"
        return {"message": error_message}, 409

    order.status = True
    session.commit()

    return list_order(order), 200


@app.delete('/item/delete')
def delete_item(query: ItemSearchSchema):
    print("Delete item function reached")
    item_id = query.item_id

    print(f"Item id: {item_id}")
    logger.debug("Deleting item ")
    session = Session()

    item = session.query(Item).filter(Item.id == item_id).first()
    order = item.order

    if item.quantity == 1:
        print("Exclude item from order - quantity < 1")
       # Delete item from order
        session.delete(item)

    else:
        print("Decrease quantity of item")
        # Decrease quantity
        item.quantity = item.quantity - 1
        print(item.quantity)

    session.commit()

    order.recalculate_total()

    orders = list_order(order)

    session.close()
    return orders, 200


























