
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Monthly sales
sales = np.array([100, 150, 200, 180, 220, 300])
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

# Create DataFrame
df = pd.DataFrame({
    "Month": months,
    "Sales": sales
})

print("Monthly Sales Data:")
print(df)

# 1. Line Graph
plt.figure(figsize=(6, 4))
plt.plot(months, sales, marker='o', color='blue')
plt.title("Monthly Sales Trend")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

# 2. Bar Chart
plt.figure(figsize=(6, 4))
plt.bar(months, sales, color='green')
plt.title("Month-wise Sales Comparison")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()

# 3. Pie Chart
plt.figure(figsize=(6, 4))
plt.pie(
    sales,
    labels=months,
    autopct='%1.1f%%',
    startangle=90
)
plt.title("Monthly Sales Contribution")
plt.show()

# 4. Histogram
plt.figure(figsize=(6, 4))
plt.hist(sales, bins=5, color='orange', edgecolor='black')
plt.title("Distribution of Sales")
plt.xlabel("Sales Values")
plt.ylabel("Frequency")
plt.show()

# 5. Scatter Plot
plt.figure(figsize=(6, 4))
plt.scatter(range(len(sales)), sales, color='red')
plt.title("Month Index vs Sales")
plt.xlabel("Month Index")
plt.ylabel("Sales")
plt.grid(True)
plt.show()
