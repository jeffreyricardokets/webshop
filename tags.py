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
        test_query = Tag_for_products.select().where(Tag_for_products.product_id == product.product_id ,Tag_for_products.product_tag_id == tag.id)
        if test_query.exists():
            print('tag already added to this product')
        else:
            Tag_for_products.create(product_id = product , product_tag_id = tag)
            print('tag has been added')
    else:
        print('Error: something went wrong')

def list_products_per_tag(tag_id):
    #make an empty list
    my_list = []
    #find the tag in our database
    
    query = Products.select().join(Tag_for_products).where(Tag_for_products.product_tag_id == tag_id)
    for item in query:
        print(item.product_name)
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
#product_add_tag(1,2)
#list_products_per_tag(2)