__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

from models import *
import products
import users
import tags
import orders
import datetime

from autocorrect import Speller

Word = Speller(lang='en')



db.create_tables([Users,Products,Orders,Tags,Tag_for_products])

def add_query_item_to_list(query, tag_query, product_id_list):
    for item in query:
        product_id_list.append(item.product_id)
    for item in tag_query:
        product_id_list.append(item.product_id)
    return product_id_list

#find out if the
def run_search_query(term):
    tag_query = Tag_for_products.select(Tag_for_products).join(Tags).where(Tags.tag_name.contains(term) |
    Tags.tag_description.contains(term))
    
    query = Products.select().where(Products.product_name.contains(term) |
    Products.product_description.contains(term))
    return query, tag_query

def search(term):
    product_id_list =[]
    query, tag_query =  run_search_query(term)
    if (query.exists() or tag_query.exists()):
        product_id_list = add_query_item_to_list(query, tag_query, product_id_list)
    else:
        converted_term = Word(term)
        query, tag_query =  run_search_query(converted_term)
        if (query.exists() or tag_query.exists()):
            print(f'Could not find the item in the database with term {term}')
            print(f'We searched with term {converted_term} and found the following')
            product_id_list = add_query_item_to_list(query, tag_query, product_id_list)
        else:
            print('could find nothing at all')
    products.product_list_to_table(product_id_list)        


#def add_product_to_catalog(user_id, product):
def add_product_to_catalog(product_name, description, price_per_unit, stock):
    product = Products.select().where(Products.product_name == product_name)
    if product.exists():
        print('That productname already exist do you want to put this record in the database?')
        input_user = input('Write Y to continue and N to exit ')
        if input_user == 'n' or input_user == 'N':
            print('You chose the option not to make another product with the same name')
            return
        elif input_user == 'y' or input_user == 'Y':
            print('You chose the option to make another product with the same name')
        else:
            print('you pressed the wrong key')
    Products.create(product_name = product_name, product_description = description, product_price_per_unit= price_per_unit, product_stock = stock)

#Def remove product from catalog search by id
def remove_product_from_catalog_by_id(product_id):
    remove_products = (Products.select().where(Products.product_id == product_id))
    if remove_products.exists():
        delete_products(remove_products)
    else:
        print('product not found')

#def remove product from catalog search by name mostly usefull to delete multiple objects
def remove_product_from_catalog_by_name(product_name):
    remove_products = (Products.select().where(Products.product_name ** product_name))
    if remove_products.exists():
        delete_products(remove_products)
    else:
        print('Product is not found')
        return

def delete_products(remove_products):
    for product in remove_products:
        remove_tags_from_product = Tag_for_products.select().where(Tag_for_products.product_id == product.product_id)
        if remove_tags_from_product.exists():
            for tag in remove_tags_from_product:
                tag.delete_instance()
                print('removed tag from this product')
        else:
            print('No tag connected to this product')
        product.delete_instance()
        print('deleted this product')

#earning filter
def show_revenue(first_date,second_date):
    orders = Orders.select().where(Orders.order_date.between(first_date,second_date))
    if orders.exists():
        revenue_counter = 0
        for order in orders:
            revenue_counter = revenue_counter + order.product_price
        return f"the revenenue from the selected date's is : {round(revenue_counter,2)} euro's"
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

def add_some_product_to_catalog():
    add_product_to_catalog('laptop', 'an amazing phone', 100.99, 2)
    add_product_to_catalog('Phone', 'an amazing phone', 100.99, 2)
    tags.product_add_tag(1,1)
    tags.product_add_tag(2,1)


#add_some_product_to_catalog()
print(show_revenue('2022-04-01', '2022-04-20'))
#remove_product_from_catalog_by_name('phone')
#remove_product_from_catalog_by_id(1)
#create_tag('laptop', 'An amazing computer')
#tags.product_add_tag(1,1)
#print(users.list_user_products(1))
#print(list_products_per_tag(1))
#add_product_to_catalog('phone', 'an amazing phone', 100.99, 2)
#products.update_stock(1,200)
#users.create_user('tomas', 'Ardennenlaan 12', 'AI')
#users.user_list()
#print(users.list_user_products(1))
#product.remove_product(19,2)
#orders.purchase_product(2,1,1)
#find user
#print(search("computer"))
#make_test_data()
