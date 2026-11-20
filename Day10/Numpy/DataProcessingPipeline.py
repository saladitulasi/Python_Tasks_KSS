import numpy as np

# Convert list into NumPy array
data = np.array([12, 7, 25, 3, 18, 10])

# Sort the array
sorted_data = np.sort(data)

# Split into two equal parts
parts = np.split(sorted_data, 2)

# Calculate sum of each part
sum1 = np.sum(parts[0])
sum2 = np.sum(parts[1])

# Print sorted array
print("Sorted Array:", sorted_data)

# Print split arrays
print("First Part:", parts[0])
print("Second Part:", parts[1])

# Print sums
print("Sum of First Part:", sum1)
print("Sum of Second Part:", sum2)