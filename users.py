from models import *
from rich.console import Console
from rich.table import Table

console = Console()

#create a user
def create_user(name,address,billing_information):
    query = Users.select().where(Users.username == name)
    if query.exists():
        return 'Error : there is already a user with that name'
    else:
        Users.create(username = name, address = address, billing_information= billing_information)

#list the users that we have in our database
def user_list():
    table = Table(title='User List')
    table.add_column('name')
    table.add_column('addres')
    table.add_column('billing information')
    for user in Users:
        table.add_row(user.username, user.address, user.billing_information)
    console.print(table)

#list the users orders in a table
def list_user_orders(user_id):
    orders = (Products.select(Orders.product_ammount,Orders.order_date,Products)
    .join(Orders, attr='orders')
    .where(Orders.user_id == user_id))
    if orders.exists():
        user =  Users.get(Users.user_id == user_id)
        table = Table(title=f'The products of : {user.username}')
        table.add_column('Name')
        table.add_column('Description')
        table.add_column('Product price')
        table.add_column('Quantity')
        table.add_column('Total price')
        table.add_column('Date orderd')
        for order in orders:
            table.add_row(order.product_name,
            order.product_description,
            str(order.product_price_per_unit),
            str(order.orders.product_ammount),
            str(order.orders.total_ammount),
            str(order.orders.order_date))
        console.print(table)
    else:
        print('could not find user')
        return
        

def list_user_products(user_id):
    products = (Products.select().join(Orders).where(Orders.user_id == user_id))
    if products.exists():
        user =  Users.get(Users.user_id == user_id)
        table = Table(title=f'The products of : {user.username}')
        table.add_column('Name')
        table.add_column('Description')
        for product in products:
            table.add_row(product.product_name,
            product.product_description)
        console.print(table)
    else:
        print('could not find user')
        return
        

#list_user_orders(1)
#list_user_products(1)