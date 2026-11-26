
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Product sales and profit data
sales = np.array([200, 300, 250, 400, 350])
profit = np.array([50, 70, 60, 90, 80])
products = ["A", "B", "C", "D", "E"]

# Create DataFrame
df = pd.DataFrame({
    "Product": products,
    "Sales": sales,
    "Profit": profit
})

print("Product Sales and Profit Data:")
print(df)

# 1. Line Graph - Sales Trend
plt.figure(figsize=(6, 4))
plt.plot(products, sales, marker='o', color='blue')
plt.title("Product Sales Trend")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

# 2. Bar Chart - Product vs Sales
plt.figure(figsize=(6, 4))
plt.bar(products, sales, color='green')
plt.title("Product-wise Sales")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.show()

# 3. Pie Chart - Sales Contribution
plt.figure(figsize=(6, 4))
plt.pie(
    sales,
    labels=products,
    autopct='%1.1f%%',
    startangle=90
)
plt.title("Product Sales Contribution")
plt.show()

# 4. Histogram - Profit Distribution
plt.figure(figsize=(6, 4))
plt.hist(profit, bins=5, color='orange', edgecolor='black')
plt.title("Profit Distribution")
plt.xlabel("Profit")
plt.ylabel("Frequency")
plt.show()

# 5. Scatter Plot - Sales vs Profit
plt.figure(figsize=(6, 4))
plt.scatter(sales, profit, color='red')
plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.grid(True)
plt.show()
