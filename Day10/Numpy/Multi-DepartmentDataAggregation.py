import numpy as np

# Store Branch A data
branchA = np.array([[10, 20],
                    [30, 40]])

# Store Branch B data
branchB = np.array([[5, 15],
                    [25, 35]])

# Combine both matrices
combined = np.concatenate((branchA, branchB))

# Calculate total employees
total = np.sum(combined)

# Print combined matrix
print("Combined Matrix:")
print(combined)

# Print total employees
print("Total Employees:", total)