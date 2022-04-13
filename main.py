__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

from models import *

db.create_tables([user,producten,in_stock,tags,user_products,tags_stock_products,tags_producten,])


def search(term):
    #make a list
    my_list = []
    #search in the in_stock table if there is something what that name
    query = in_stock.select().where(in_stock.name == term)
    #if it is found we loop over the finding else we return an error message
    if query.exists():
        for item in query:
            my_list.append(item.name)
    else:
        print('nothing found')
        
    print(my_list)
    


def list_user_products(user_id):
    #make a list
    my_list = []
    # find the user that we want to see the products
    gebruiker =  user.get(user.id == user_id)
    #loop over all the products
    for product in gebruiker.products:
        my_list.append(product.name)
    #return the list
    return my_list


def list_products_per_tag(tag_id):
    #make an empty list
    my_list = []
    #find the tag in our database
    tag = tags.get(tags.id == tag_id)
    for product in tag.stock_id:
        my_list.append(product.name)
    return my_list



#def add_product_to_catalog(user_id, product):
def add_product_to_catalog(product_name, description, price_per_unit, stock):
    #create the product in our stock 
    in_stock.create(name = product_name, description = description, price_per_unit= price_per_unit, stock = stock)


def update_stock(product_id, new_quantity):
    #find the product in stock
    product  = in_stock.get(in_stock.id == product_id)
    #save the the new quantity of stock in the variable
    product.stock = new_quantity
    #save the variable to the database
    product.save()


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
        #add the right tag of the stock to the product
        for tag in stock_product.name_tags:
            product.name_tags.add(tag)
        #add that product to the user profile
        buyer.products.add(product)
    else:
        print('not enough in stock')


def remove_product(product_id):
    #search the product
    stock_product = in_stock.get(in_stock.id == product_id)
    #find out which tags is connected to the stock
    for item in tags_stock_products:
        if item.in_stock_id == stock_product.id:
            item.delete_instance()
    #And remove that product
    stock_product.delete_instance()

def create_user(name,address,billing_information):
    #create user
    user.create(name = name, address = address, billing_information= billing_information)

def create_tag(name, description):
    #find out if tag is already in our database
    query = tags.select().where(tags.name == name)
    if query.exists():
        print('tag already exist use one with a different name')
    else:
    #create tag
        tags.create(name = name, description = description)   

def product_add_tag(product_id, tag_id):
    #find product in our stock
    try:
        product = in_stock.get(in_stock.id == product_id)
    except:
        print('the product does not exist')
        return
    #find the tag in our tag database
    try:
        tag = tags.get(tags.id == tag_id)
    except:
        print('that tag does not exist')
        return
    #find out if the product already have this tag
    for stock in tag.stock_id:
        if stock.id == product.id:
            #if this item has this tag then we will end the function
            print('this item has already this tag')
            return 
    #add the tag to the product in our stock
    tag.stock_id.add(product)

#create_user('jef', 'Ardennenlaan 12', 'AI')
#create_tag('telefoon', 'An amazing computer')
#product_add_tag(3,1)
#print(list_user_products(1))
#print(list_products_per_tag(1))
#add_product_to_catalog('laptop', 'an amazing laptop', 100.99, 2)
#update_stock(1,100)
#purchase_product(1,1,1)

#remove_product(3)

#find user
search("banana")

