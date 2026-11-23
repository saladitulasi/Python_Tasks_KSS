import numpy as np

# Generate random sales for 10 days
sales = np.random.randint(100, 501, size=10)

print("Sales Data:", sales)

# Calculate average sales
avg_sales = np.mean(sales)

print("Average Sales:", avg_sales)