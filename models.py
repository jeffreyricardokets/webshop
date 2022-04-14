from peewee import *
# Models go here

#db connection

db = SqliteDatabase('app.db')

class BaseModel(Model):
    class Meta:
        database = db

#stock
class in_stock(BaseModel):
    name = CharField()
    description = CharField()
    price_per_unit = FloatField()
    stock = IntegerField()

#producten
class producten(BaseModel):
    name = CharField()
    description = CharField()
    price_per_unit = FloatField()
    ammount = IntegerField()

#tags
class tags(BaseModel):
    name = CharField()
    description =  CharField()
    stock_id = ManyToManyField(in_stock)
    product_id = ManyToManyField(producten)

#user
class user(BaseModel):
    name = CharField()
    address = CharField()
    billing_information = CharField()
    products = ManyToManyField(producten)


#transaction
class transaction(BaseModel):
    name = CharField
    ammount = IntegerField()
    price_of_each_product = FloatField()
    date = DateField()
    product_sold = ManyToManyField(in_stock)

    
user_products = user.products.get_through_model()
tags_stock_products = tags.stock_id.get_through_model()
tags_producten = tags.product_id.get_through_model()
transaction_products = transaction.product_sold.get_through_model()