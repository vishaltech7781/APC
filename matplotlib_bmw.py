import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("bmw_sales.csv")
data1 = data.head(20)

plt.plot(data1['Model'],data1['Year'])

plt.xlabel("model")
plt.ylabel("year")
plt.title("BMW sales record")

plt.show()