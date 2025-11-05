import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Read the CSV file
data = pd.read_csv("bmw_sales.csv")

print("Preview of BMW Sales Data:")
print(data.head(100))

# Step 3: Select only numeric columns for correlation
corr = data[['Price_USD', 'Year','Sales_Volume']].corr()

# Step 4: Print the correlation matrix (optional)
print("\nCorrelation Matrix:")
print(corr)

# Step 5: Create a Heatmap
plt.figure(figsize=(8, 6))  # adjust the figure size
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)

# Step 6: Add title and show plot
plt.title("Heatmap - BMW Sales C")
plt.show()
