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
        product = producten.create(name = stock_product.name, description = stock_product.description, price_per_unit = stock_product.price_per_unit, ammount = quantity)
        #add transaction
        transactie = transaction.create(name = stock_product.name, ammount = quantity, price_of_each_product = stock_product.price_per_unit, date='2022-04-14')
        #make a list of all the tags we need to add
        my_list = []
        #loop over the tags_stock_product
        for item in tags_stock_products:
            #check if the tags id == stock product id
            if item.in_stock.id == stock_product.id:
                #if so we add to the list
                my_list.append(item.tags_id)
        #check if list is not empty
        if my_list:
            #loop over the list
            for tag in my_list:
                #find the tag in the list
                find_tag = tags.get(tags.id == tag)
                find_tag.product_id.add(product)
        #add that product to the user profile
        buyer.products.add(product)
        #add the product to the transaction in stock database
        transactie.product_sold.add(stock_product)
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
    #find user
    gebruiker = user.select().where(user.id == user_id)
    #find stock
    user_product = producten.select().where(producten.id == product_id)
    if gebruiker.exists() & user_product.exists():
        #check if the user owns this item
        for item in user_products:
            if(item.user_id == user_id & (item.producten_id == product_id)):
                product_to_remove = producten.get(producten.id == product_id)
                product_to_remove.delete_instance()
                item.delete_instance()
                return
    else:
        print('Error')
        return
    if product_is_from_user == False:
        print('this product is not from the user')
        return


    
