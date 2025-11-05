import pandas as pd

data = pd.read_csv("bmw_sales.csv")
sales = data['Year']   # <-- This is a Series

print("Average Sales:", sales.mean())
print("Max Sales:", sales.max())
print("Min Sales:", sales.min())

print("top 5 of the data ",sales.head())
print("buttom 5 of the data",sales.tail())
print(sales.shape)
print(sales.median())
print(sales.unique())


col = data['Color']

print(col.head())
print(col.tail())
print(col.unique())

