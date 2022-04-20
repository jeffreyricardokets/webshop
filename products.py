from models import *

def update_stock(product_id, new_quantity):
    try:
        product  = Products.get(Products.product_id == product_id)
        product.product_stock = new_quantity
        product.save()
    except:
        print('Error there is something wrong')



#update_stock(2,100)
    