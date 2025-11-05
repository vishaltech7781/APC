import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv("bmw_sales.csv")

# Use first 10 rows for simplicity
data1 = data.head(15)

plt.pie(data1['Price_USD'], labels=data1['Model'], autopct='%1.1f%%', startangle=90)
plt.title("Pie Chart - BMW Model Sales Share")
plt.show()
