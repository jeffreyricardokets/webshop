from models import *
from rich.console import Console
from rich.table import Table

console = Console()

#get a list of id and turn them into a table
def product_list_to_table(my_list):
    table = Table(title = 'Product list')
    table.add_column('product id')
    table.add_column('product name')
    table.add_column('product description')
    table.add_column('product price')
    for id in my_list:
        item = Products.get(Products.product_id == id)
        table.add_row(str(item.product_id), item.product_name, item.product_description, str(item.product_price_per_unit))
    console.print(table)    


def update_stock(product_id, new_quantity):
    try:
        product  = Products.get(Products.product_id == product_id)
        product.product_stock = new_quantity
        product.save()
    except:
        print('Error there is something wrong')



#update_stock(2,100)
    