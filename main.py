__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

from models import *
import products
import users
import tags
import orders


db.create_tables([Users,Products,Orders,Tags,Transactions,Tag_for_products])


"""def search(term):
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
    """



#def add_product_to_catalog(user_id, product):
def add_product_to_catalog(product_name, description, price_per_unit, stock):
    #create the product in our stock 
    Products.create(product_name = product_name, product_description = description, product_price_per_unit= price_per_unit, product_stock = stock)



#earning filter
def show_revenue(date):
    #find the selected date
    query = Transactions.select().where(Transactions.date == date)
    #if query exist
    if query.exists():
        #make a variable to keep track how much we have
        revenue_counter = 0
        #loop through the query
        for item in query:
            #add the amount of each product to the counter
            revenue_counter = revenue_counter + item.price_of_each_product
        #return the revenue
        return round(revenue_counter,2)
    else:
        return 'no record found'

#make some test data

def make_test_data():
    add_product_to_catalog('laptop', 'an amazing phone', 100.99, 2)
    add_product_to_catalog('Phone', 'an amazing phone', 100.99, 2)
    users.create_user('tomas', 'Ardennenlaan 12', 'AI')
    users.create_user('jeffrey', 'Ardennenlaan 12', 'AI')
    users.create_user('Dexter', 'Ardennenlaan 12', 'AI')
    orders.purchase_product(2,1,1)


#print(show_revenue('2022-04-14'))

#create_tag('laptop', 'An amazing computer')
#tags.product_add_tag(1,1)
#print(users.list_user_products(1))
#print(list_products_per_tag(1))
#add_product_to_catalog('phone', 'an amazing phone', 100.99, 2)
#product.update_stock(50,100)
#users.create_user('tomas', 'Ardennenlaan 12', 'AI')
#users.user_list()
#print(users.list_user_products(1))
#product.remove_product(19,2)
#orders.purchase_product(2,1,1)
#find user
#print(search("computer"))
#make_test_data()
