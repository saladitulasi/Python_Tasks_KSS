import numpy as np

data = np.array([1, 2, 2, 3, 1, 4, 2, 3])
# Find unique numbers and their counts
numbers, counts = np.unique(data, return_counts=True)

print("Unique Numbers:", numbers)
print("Counts:", counts)