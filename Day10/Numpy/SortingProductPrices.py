import numpy as np

# Store product prices
prices = [499, 299, 799, 199, 599]

# Convert list into NumPy array
arr = np.array(prices)

# Sort prices in ascending order
sorted_prices = np.sort(arr)

# Print sorted prices
print("Sorted Prices:", sorted_prices)