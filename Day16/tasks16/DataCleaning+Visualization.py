import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create data
data = np.array([100, np.nan, 200, 150, np.nan, 300])

# Convert into Pandas Series
s = pd.Series(data)

print("Original Data:")
print(s)

# Calculate mean
mean = s.mean()

print("Mean:", mean)

# Replace NaN with mean
s = s.fillna(mean)

print("Cleaned Data:")
print(s)

# Create figure with 2 subplots
plt.figure(figsize=(10, 4))

# 1. Line Graph
plt.subplot(1, 2, 1)
plt.plot(s.index, s.values, marker='o', color='blue')
plt.title("Cleaned Data Line Graph")
plt.xlabel("Index")
plt.ylabel("Values")
plt.grid(True)

# 2. Filter values greater than average
filtered = s[s > mean]

plt.subplot(1, 2, 2)
plt.bar(filtered.index, filtered.values, color='green')
plt.title("Values Above Average")
plt.xlabel("Index")
plt.ylabel("Values")

# Adjust layout
plt.tight_layout()

# Display graphs
plt.show()