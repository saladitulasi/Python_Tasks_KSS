import numpy as np

values = np.array([10, 12, 15, 18, 100, 14, 13])
# Calculate mean and standard deviation
mean = np.mean(values)
std = np.std(values)

# Remove values more than 2 standard deviations from mean
filtered_values = values[np.abs(values - mean) <= 2 * std]

print("Mean:", mean)
print("Standard Deviation:", std)
print("Values after removing outliers:", filtered_values)