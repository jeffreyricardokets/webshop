from peewee import *
# Models go here

#db connection

db = SqliteDatabase('app.db')

class BaseModel(Model):
    class Meta:
        database = db


#user
class Users(BaseModel):
    user_id = PrimaryKeyField()
    username = CharField()
    address = CharField()
    billing_information = CharField()

#Products
class Products(BaseModel):
    product_id = PrimaryKeyField()
    product_name = CharField()
    product_description = CharField()
    product_price_per_unit = FloatField()
    product_stock = IntegerField()

#Orders
class Orders(BaseModel):
    order_id = PrimaryKeyField()
    order_product = ForeignKeyField(Products)
    product_ammount = IntegerField()
    product_price = FloatField()
    total_ammount = FloatField()
    order_date = DateField()
    user = ForeignKeyField(Users, backref='producten')

#tags
class Tags(BaseModel):
    tag_name = CharField()
    tag_description =  CharField()

#connect tag to the products
class Tag_for_products(BaseModel):
    product = ForeignKeyField(Products ,backref='tags_connection')
    product_tag = ForeignKeyField(Tags ,backref='tags_connection')

