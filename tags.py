from models import *

def create_tag(name, description):
    #find out if tag is already in our database
    query = Tags.select().where(Tags.tag_name == name)
    
    if query.exists():
        print('tag already exist use one with a different name')
    else:
    #create tag
        tag = Tags.create(tag_name = name, tag_description = description) 
        print(f'Created a tag with name : {tag.tag_name} and with description {tag.tag_description}')

def product_add_tag(product_id, tag_id):
    product_query = Products.select().where(Products.product_id == product_id)
    tag_query = Tags.select().where(Tags.id == tag_id)
    Tag_for_products_query = Tag_for_products.select()
    if tag_query.exists() and product_query.exists():
        product = Products.get(Products.product_id == product_id)
        tag = Tags.get(Tags.id == tag_id)
        for item in Tag_for_products_query:
            print(product.id)
            print(item.product_id == product.id)
            print(item.product_tag_id)
        Tag_for_products.create(product_id = product , product_tag_id = tag)
    else:
        print('Error: something went wrong')

def list_products_per_tag(tag_id):
    #make an empty list
    my_list = []
    #find the tag in our database

    #set a query
    """
    query = Tag_for_products.select(Tag_for_products,producten,Tags).join(Tags , JOIN.LEFT_OUTER).switch().join(producten, JOIN.LEFT_OUTER).switch(Tags).where(Tags.id == '2').switch(producten)
    for item in query:
        print(item.tag)
    """
    """
    query = in_stock.select().join(Tag_for_stock).where(tag_id == 1)
    #tag = tags.get(tags.id == tag_id)
    for product in query:
        my_list.append(product.name)
    #remove dublicates
    my_list = list(dict.fromkeys(my_list))
    return my_list
    """

#create_tag('laptop', 'lolol')
product_add_tag(1,1)
#list_products_per_tag(1)