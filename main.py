__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

from models import *

db.connect()
db.create_tables([user,producten,in_stock,tags,transaction,user_products,tags_stock_products,tags_producten,transaction_products])


#tags.stock_id.add(product)

def search(term):
    #make a dict
    my_dict = {}
    #store all the id of the tags we find
    store_id_tag_list =[]
    #store a list which all the in_stock_id so we can find the product
    store_in_stock_tag_list = []
    #search inm the tag database for tags that contains the same name or description
    tag_query = tags.select().where(tags.name.contains(term) | tags.description.contains(term))
    if tag_query.exists():
        for item in tag_query:
            store_id_tag_list.append(item.id)
    #loop through the tag list we created
    for id in store_id_tag_list:
        #search in the tags_in_stock database for the tags_id that is same as the id in our list
        tags_in_stock_query = tags_stock_products.select().where(tags_stock_products.tags_id == id)
        #check if it exist
        if tags_in_stock_query.exists():
            for item in tags_in_stock_query:
                store_in_stock_tag_list.append(item.in_stock_id)
    if store_in_stock_tag_list:
        for item in store_in_stock_tag_list:
            query = in_stock.select().where(in_stock.id == item)
            if query.exists():
                for result in query:
                    my_dict[result.id] = result.name
    #search in the in_stock table if there is something that contains the search variable
    query = in_stock.select().where(in_stock.name.contains(term))
    #if it is found we loop over the finding else we return an error message
    if query.exists():
        for item in query:
            #add item to dict
            my_dict[item.id] = item.name

    if my_dict:
        return(my_dict)
    else:
        return('nothing found in our database')
    


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
        #add transaction
        transaction.create(name = stock_product.name, ammount = quantity, price_of_each_product = stock_product.price_per_unit, date='2022-04-14')
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
            return ('this item has already this tag')
    #add the tag to the product in our stock
    tag.stock_id.add(product)



#create_user('jef', 'Ardennenlaan 12', 'AI')
#create_tag('telefoon', 'An amazing computer')
#product_add_tag(13,2)
#print(list_user_products(1))
#print(list_products_per_tag(1))
#add_product_to_catalog('laptop', 'an amazing laptop', 100.99, 2)
#update_stock(1,100)
purchase_product(2,1,1)

#remove_product(3)

#find user
#print(search("computer"))

