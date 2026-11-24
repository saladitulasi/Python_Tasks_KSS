import numpy as np

temps = np.array([28, 32, 35, 31, 29, 40, 38])
# Identify temperatures greater than 30
hot_days = temps[temps > 30]

# Find their indices
indices = np.where(temps > 30)

print("Temperatures above 30:", hot_days)
print("Day Indices:", indices[0])