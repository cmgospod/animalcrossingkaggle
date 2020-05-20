import pandas as pd

items = pd.read_csv('items.csv')
print(items.shape)

critic = pd.read_csv('critic.csv')
print(critic.shape)

user_reviews = pd.read_csv('user_reviews.csv')
print(user_reviews.shape)

villagers = pd.read_csv('villagers.csv')
print(villagers.shape)

male_villagers = villagers[villagers['gender']=='male']
print(male_villagers.shape)

female_villagers = villagers[villagers['gender']=='female']
print(female_villagers.shape)

print(villagers['personality'].value_counts())
print(male_villagers['personality'].value_counts())
print(female_villagers['personality'].value_counts())


print(items.head(3))
