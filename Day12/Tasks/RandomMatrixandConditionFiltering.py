import numpy as np

# Generate a 3x3 random matrix
matrix = np.random.randint(0, 51, size=(3, 3))

print("Original Matrix:")
print(matrix)

# Filter elements greater than 25
result = matrix[matrix > 25]

print("Filtered Values:", result)