from models import *

def create_tag(name, description):
    #find out if tag is already in our database
    query = Tags.select().where(Tags.name == name)
    
    if query.exists():
        print('tag already exist use one with a different name')
    else:
    #create tag
        Tags.create(name = name, description = description)   

def product_add_tag(product_id, tag_id):
    stock = in_stock.get(in_stock.id == product_id)
    tag = Tags.get(Tags.id == tag_id)
    #add the tag to the product in our stock
    #tag_for_product.create(product = product , tag = tag)
    Tag_for_stock.create(stock = stock , tag = tag)

def list_products_per_tag(tag_id):
    #make an empty list
    my_list = []
    #find the tag in our database

    #set a query
    query = Tag_for_products.select(Tag_for_products,producten,Tags).join(Tags , JOIN.LEFT_OUTER).switch().join(producten, JOIN.LEFT_OUTER).switch(Tags).where(Tags.id == '2').switch(producten)
    for item in query:
        print(item.tag)
    """
    query = in_stock.select().join(Tag_for_stock).where(tag_id == 1)
    #tag = tags.get(tags.id == tag_id)
    for product in query:
        my_list.append(product.name)
    #remove dublicates
    my_list = list(dict.fromkeys(my_list))
    return my_list
    """

#create_tag('test', 'lolol')
#product_add_tag(1,3)
list_products_per_tag(1)