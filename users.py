from models import *
from rich.console import Console
from rich.table import Table

console = Console()

#create a user
def create_user(name,address,billing_information):
    #find if we have already a user with same username like how many websites will check it
    query = user.select().where(user.name == name)
    if query.exists():
        return 'Error : there is already a user with that name'
    else:
        #create user
        user.create(name = name, address = address, billing_information= billing_information)

#list the users that we have in our database
def user_list():
    #make table
    table = Table(title='User List')
    #add collums
    table.add_column('name')
    table.add_column('addres')
    table.add_column('billing information')
    #loop over all the users
    for gebruiker in user:
        #add the row the the table for each user
        table.add_row(gebruiker.name, gebruiker.address, gebruiker.billing_information)
    #print the table
    console.print(table)

#list the users product in a table
def list_user_products(user_id):
    
    #query
    query = producten.select().join(user).where(user.id == user_id)
    if query.exists():
        # find the user so we can display the name
        gebruiker =  user.get(user.id == user_id)
        #make a table
        table = Table(title=f'The products of : {gebruiker.name}')
        #add columns to the table
        table.add_column('name')
        table.add_column('description')
        table.add_column('price per unit')
        table.add_column('ammount')
        #loop over all the products
        for product in query:
            print(product)
            table.add_row(product.name,product.description, str(product.price_per_unit), str(product.ammount))
        console.print(table)
    else:
        print('could not find user')
        return

