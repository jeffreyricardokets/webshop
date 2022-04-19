from models import *
import datetime

#purchase a product for the user
def purchase_product(product_id, buyer_id, quantity):
    #search the user that want to buy the product
    buyer = Users.get(Users.user_id == buyer_id)
    #search the product in our stock
    product = Products.get(Products.product_id == product_id)
    #check if we have enough stock
    
    if product.product_stock >= quantity:
        #remove the ammount that the user want from the stock
        product.product_stock = product.product_stock - quantity
        #save the stock
        product.save()
        
        #make a new order for the user that we can add
        order = Orders.create(order_product = product, product_ammount = quantity, product_price = product.product_price_per_unit, total_ammount = product.product_price_per_unit * quantity, order_date = datetime.datetime.now(), user = buyer)
        
    else:
        print('not enough in stock')

def delete_order(order_id):
    item_to_delete = Orders.get(Orders.order_id == order_id)
    item_to_delete.delete_instance()
    print('delete this row because stock is 0 or below ')
    return 

#remove order from user
def remove_product(product_id,user_id):
    product_is_from_user = False
    #join
    query = Orders.select().where(Orders.order_product_id == product_id).join(Users).where(Users.user_id == user_id)
    if query.exists():
        for item in query:
            object = Orders.get(Orders.order_id == item.order_id)
            if object.product_ammount <= 0:
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
remove_product(2,1)