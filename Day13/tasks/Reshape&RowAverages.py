import numpy as np

data = np.arange(1, 13)
# Reshape into a 3x4 matrix
matrix = data.reshape(3, 4)

# Calculate average of each row
row_averages = np.mean(matrix, axis=1)

print("3x4 Matrix:")
print(matrix)

print("Row Averages:", row_averages)