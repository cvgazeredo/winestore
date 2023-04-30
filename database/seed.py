from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Product, Type, Country, Grape


# Define data
types = [
    Type(id=1, name='Tinto'),
    Type(id=2, name='Rosé'),
    Type(id=3, name='Branco'),
]

countries = [
    Country(id=1, name='Portugal'),
    Country(id=2, name='França'),
    Country(id=3, name='Chile'),
]

grapes = [
    Grape(id=1, name='Touriga Nacional'),
    Grape(id=2, name='Pinot Noir'),
    Grape(id=3, name='Syrah'),
    Grape(id=4, name='Sauvignon Blanc'),
    Grape(id=5, name='Touriga Franca'),
    Grape(id=6, name='Tinta Amarela'),
    Grape(id=7, name='Merlot'),
    Grape(id=8, name='Cabernet Sauvignon'),
    Grape(id=9, name='Petit Verdot'),
    Grape(id=10, name='Grenache'),
]

products = [
    Product(id=1, label='Niepoort Dão', photo='niepoort_dao.png', price=139.32, type=types[0], country=countries[0], grapes=[grapes[0]]),
    Product(id=2, label='Vallado Douro', photo='vallado_douro.png', price=157.16, type=types[1], country=countries[0], grapes=[grapes[0]]),
    Product(id=3, label='Michel Noellat Fixin', photo='michel-noellat-fixin.png', price=432.34, type=types[0], country=countries[1], grapes=[grapes[1]]),
    Product(id=4, label='Matetic Corralillo ', photo='matetic_corralillo.png', price=216.66, type=types[0], country=countries[2], grapes=[grapes[1]]),
    Product(id=5, label='Errazuriz Aconcagua', photo='errazuriz_aconcagua.png', price=180.96, type=types[2], country=countries[2], grapes=[grapes[3]]),
    Product(id=6, label='Niepoort Batuta Douro', photo='niepoort_batuta.png', price=1230.72, type=types[0], country=countries[0], grapes=[grapes[0], grapes[4], grapes[5]]),
    Product(id=7, label='Pombal do Vesuvio', photo='pombal_do_vesuvio.png', price=333.96, type=types[0], country=countries[0], grapes=[grapes[5]]),
    Product(id=8, label='Fleur des Pedésclaux', photo='fleur_des_pesdesclaux.png', price=372.24, type=types[0], country=countries[1], grapes=[grapes[6], grapes[7], grapes[9]]),
    Product(id=9, label='Estandon Heritage', photo='estandon_heritage.png', price=189.46, type=types[1], country=countries[1], grapes=[grapes[2], grapes[8], grapes[2]]),
]


# Create a database connection and session
engine = create_engine('postgresql://postgres:12345@localhost/winestore')
Session = sessionmaker(bind=engine)
session = Session()

# Add the data to the database and commit the changes
for product in products:
    session.add(product)

for type in types:
    session.add(type)

for country in countries:
    session.add(country)

for grape in grapes:
    session.add(grape)

session.commit()

print('Data seeded successfully!')