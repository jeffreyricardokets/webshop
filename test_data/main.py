from peewee import *
from model import *


def create_tables():
    db.create_tables([
        User,
        Tweet,
        Favorite])

def populate_test_data():
    db.create_tables([User, Tweet, Favorite])

    data = (
        ('huey', ('meow', 'hiss', 'purr')),
        ('mickey', ('woof', 'whine')),
        ('zaizee', ()))
    for username, tweets in data:
        user = User.create(username=username)
        for tweet in tweets:
            Tweet.create(user=user, content=tweet)

    # Populate a few favorites for our users, such that:
    favorite_data = (
        ('huey', ['whine']),
        ('mickey', ['purr']),
        ('zaizee', ['meow', 'purr']))
    for username, favorites in favorite_data:
        user = User.get(User.username == username)
        for content in favorites:
            tweet = Tweet.get(Tweet.content == content)
            Favorite.create(user=user, tweet=tweet)

user = User.get(User.id == 1)
tweet = Tweet.get(Tweet.id == 1)

Favorite.create(user = user ,tweet = tweet)

"""#simple join test
query = Favorite.select().join(User).where(User.username == 'zaizee')
for tweet in query:
    print(tweet.user_id)"""