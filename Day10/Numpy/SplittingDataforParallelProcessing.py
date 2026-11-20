import numpy as np

# Store the dataset
data = np.array([5, 10, 15, 20, 25, 30])

# Split data into 3 equal parts
parts = np.split(data, 3)

# Print the split arrays
print("Splitted Data:")
print(parts)