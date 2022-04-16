from models import *

def test_join():
    query = user.select().join(user).where(user.name == 'jeffrey')
    for product in query:
        print('test')

test_join()