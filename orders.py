from os import remove
from models import *
import datetime

#purchase a product for the user
def purchase_product(product_id, buyer_id, quantity):
    buyer = Users.get(Users.user_id == buyer_id)
    product = Products.get(Products.product_id == product_id)
    
    if product.product_stock >= quantity:
        product.product_stock = product.product_stock - quantity
        product.save()        
        Orders.create(order_product = product, product_ammount = quantity,
        product_price = product.product_price_per_unit,
        total_ammount = product.product_price_per_unit * quantity,
        order_date = datetime.datetime.now(),
        user = buyer)
    else:
        print('not enough in stock')

#add a product for the user
def purchase_product(product_id, buyer_id, quantity):
    buyer = Users.get(Users.user_id == buyer_id)
    product = Products.get(Products.product_id == product_id)
    
    if product.product_stock >= quantity:
        product.product_stock = product.product_stock - quantity
        product.save()        
        Orders.create(order_product = product, product_ammount = quantity,
        product_price = 0,
        total_ammount = product.product_price_per_unit * quantity,
        order_date = datetime.datetime.now(),
        user = buyer)
    else:
        print('not enough in stock')

def delete_order(order_id):
    item_to_delete = Orders.get(Orders.order_id == order_id)
    item_to_delete.delete_instance()
    return 

#remove order from user
def remove_product(product_id,user_id, remove_row = False):
    query = Orders.select().where(Orders.order_product_id == product_id).join(Users).where(Users.user_id == user_id)
    if query.exists():
        for item in query:
            object = Orders.get(Orders.order_id == item.order_id)
            if remove_row:
                delete_order(item.order_id)
            elif object.product_ammount <= 0:
                delete_order(item.order_id)
                remove_product(product_id,user_id)
            elif object.product_ammount == 1: 
                delete_order(item.order_id)
            elif object.product_ammount > 1:
                object.product_ammount = item.product_ammount - 1
                object.save()
            return
    else:
        print('No record found')

def print_order_list():
    query = Orders.select()
    for item in query:
        print(item)
            

#print_order_list()
#remove_product(2,1,True)

#purchase_product(2, 1, 1)
