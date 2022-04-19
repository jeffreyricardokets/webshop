from models import *



def update_stock(product_id, new_quantity):
    try:
        #find the product in stock
        product  = Products.get(Products.product_id == product_id)
        #save the the new quantity of stock in the variable
        product.product_stock = new_quantity
        #save the variable to the database
        product.save()
    except:
        print('Error there is something wrong')



#update_stock(2,100)
    
#remove_product(76,1)
#purchase_product(1,1,1)