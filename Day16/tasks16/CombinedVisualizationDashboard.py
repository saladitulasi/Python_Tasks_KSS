import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create data
sales = np.array([100, 200, 150, 300])
products = ["A", "B", "C", "D"]

# Create DataFrame
df = pd.DataFrame({
    "Products": products,
    "Sales": sales
})

print(df)

# Create single figure with 3 subplots
plt.figure(figsize=(12, 4))

# 1. Line Graph
plt.subplot(1, 3, 1)
plt.plot(df["Products"], df["Sales"], marker='o', color='blue')
plt.title("Sales Trend")
plt.xlabel("Products")
plt.ylabel("Sales")

# 2. Bar Chart
plt.subplot(1, 3, 2)
plt.bar(df["Products"], df["Sales"], color='green')
plt.title("Sales Comparison")
plt.xlabel("Products")
plt.ylabel("Sales")

# 3. Pie Chart
plt.subplot(1, 3, 3)
plt.pie(df["Sales"], labels=df["Products"], autopct='%1.1f%%')
plt.title("Sales Distribution")

# Adjust layout
plt.tight_layout()

# Display graphs
plt.show()