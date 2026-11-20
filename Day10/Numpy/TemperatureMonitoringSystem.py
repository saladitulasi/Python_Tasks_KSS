import numpy as np

# Store temperatures of two days
temp = np.array([[30, 32, 31],
                 [29, 33, 34]])

# Print the array
print("Temperature Array:")
print(temp)

# Find total temperature
total = np.sum(temp)

print("Total Temperature:", total)