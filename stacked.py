import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("bmw_sales.csv")

data1 = data.head(100)

plt.bar(data1['Model'], data1['Price_USD'], label='US', color='skyblue')
plt.bar(data1['Model'], data1['Price_USD'], bottom=data1['Price_USD'], label='EU', color='orange')
plt.title("Stacked Bar Plot - BMW Sales (US vs EU)")
plt.xlabel("Model")
plt.ylabel("Units Sold")
plt.xticks(rotation=45)
plt.legend()
plt.show()
