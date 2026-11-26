import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create data
products = ["Pen", "Book", "Pencil"]
sales = np.array([50, 80, 40])

# Create DataFrame
df = pd.DataFrame({
    "Products": products,
    "Sales": sales
})

print(df)

# Plot bar chart
plt.bar(df["Products"], df["Sales"], color='skyblue')

# Add labels and title
plt.xlabel("Products")
plt.ylabel("Sales")
plt.title("Product Sales Bar Chart")

plt.show()