import numpy as np

# Create a list of transaction amounts
transactions = [1200, 500, 800, 1500]

# Convert the list into a NumPy array
arr = np.array(transactions)

# Print the array
print("NumPy Array:", arr)

# Print the type of the object
print("Type:", type(arr))

# Verify whether it is a NumPy ndarray
print("Is NumPy ndarray:", isinstance(arr, np.ndarray))