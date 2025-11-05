import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("bmw_sales.csv")

data1 = data.head(30)

plt.hist(data1['Price_USD'], bins=5, color='skyblue', edgecolor='black')

plt.xlabel("Price (in ₹)")
plt.ylabel("Frequency")
plt.title("BMW Sales Price Distribution")

plt.show()
