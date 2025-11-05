import pandas as pd

data = pd.read_csv("bmw_sales.csv")

print("top 5 data :",data.head(10))
print("buttom 5 data:",data.tail(10))
print(data.shape)
print(data.info())
print(data.describe())
print(data.columns)
