import numpy as np

# Generate 8 random float values
arr = np.random.rand(8)

print("Original Values:", arr)

# Normalize by multiplying with 100
normalized = arr * 100

print("Normalized Values:", normalized)

# Filter values greater than 50
filtered = normalized[normalized > 50]

print("Values Greater Than 50:", filtered)

# Sort filtered values
sorted_values = np.sort(filtered)

print("Sorted Values:", sorted_values)