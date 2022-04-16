from peewee import *
# Models go here

#db connection

db = SqliteDatabase('app.db')

class BaseModel(Model):
    class Meta:
        database = db


#user
class user(BaseModel):
    name = CharField()
    address = CharField()
    billing_information = CharField()

#producten
class producten(BaseModel):
    name = CharField()
    description = CharField()
    price_per_unit = FloatField()
    ammount = IntegerField()
    user = ForeignKeyField(user, backref='producten')

#stock
class in_stock(BaseModel):
    name = CharField()
    description = CharField()
    price_per_unit = FloatField()
    stock = IntegerField()

#tags
class Tags(BaseModel):
    name = CharField()
    description =  CharField()

#connect tag to the stock
class Tag_for_stock(BaseModel):
    stock = ForeignKeyField(in_stock ,backref='tags_connection')
    tag = ForeignKeyField(Tags ,backref='tags_connection')

#connect tag to the products
class Tag_for_products(BaseModel):
    product = ForeignKeyField(producten ,backref='tags_connection')
    tag = ForeignKeyField(Tags ,backref='tags_connection')


#transaction
class transaction(BaseModel):
    name = CharField
    ammount = IntegerField()
    price_of_each_product = FloatField()
    date = DateField()
    product_sold = ForeignKeyField(in_stock)
