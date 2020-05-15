import pandas as pd

items = pd.read_csv('items.csv')
print(items.shape)

critic = pd.read_csv('critic.csv')
print(critic.shape)

user_reviews = pd.read_csv('user_reviews.csv')
print(user_reviews.shape)

villagers = pd.read_csv('villagers.csv')
print(villagers.shape)
