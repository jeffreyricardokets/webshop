from models import *

def purchase_product(product_id, buyer_id, quantity):
    #search the user that want to buy the product
    buyer = user.get(user.id == buyer_id)
    #search the product in our stock
    stock_product = in_stock.get(in_stock.id == product_id)
    #check if we have enough stock
    if stock_product.stock >= quantity:
        #remove the ammount that the user want from the stock
        stock_product.stock = stock_product.stock - quantity
        #save the stock
        stock_product.save()
        
        #make a new product for the user that we can add
        product = producten.create(name = stock_product.name, description = stock_product.description, price_per_unit = stock_product.price_per_unit, ammount = quantity, user_id = buyer)
        #add transaction
        transaction.create(name = stock_product.name, ammount = quantity, price_of_each_product = stock_product.price_per_unit, date='2022-04-14', product_sold = stock_product)
        #make a list of all the tags we need to add
        my_list = []
        #loop over the tags_stock_product
        tags = Tag_for_stock.select().where(Tag_for_stock.stock_id == product_id)
        if tags.exists():
            for item in tags:
                my_list.append(item.tag_id)
        #remove dublicate from the list
        if my_list:
            my_list = list(dict.fromkeys(my_list))
            for item in my_list:
                tag = Tags.get(Tags.id == item)
                Tag_for_products.create(product = product, tag = tag)
    else:
        print('not enough in stock')

def update_stock(product_id, new_quantity):
    try:
        #find the product in stock
        product  = in_stock.get(in_stock.id == product_id)
        #save the the new quantity of stock in the variable
        product.stock = new_quantity
        #save the variable to the database
        product.save()
    except:
        print('Error there is something wrong')

#remove product from user
def remove_product(product_id,user_id):
    product_is_from_user = False
    #join
    query = user.select().join(producten).where(producten.id == product_id)
    if query.exists():
        for item in query:
            if item.id == user_id:
                #find the model
                item_to_delete = producten.get(producten.id == product_id)
                item_to_delete.delete_instance()

    product_tags = Tag_for_products.select().where(Tag_for_products.product_id == product_id)
    for item in product_tags:
        item.delete_instance()


    
remove_product(76,1)
#purchase_product(1,1,1)