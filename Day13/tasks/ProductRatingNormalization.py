import numpy as np

ratings = np.array([2, 3, 4, 5, 1])
# Find minimum and maximum ratings
min_value = np.min(ratings)
max_value = np.max(ratings)

# Normalize ratings between 0 and 1
normalized = (ratings - min_value) / (max_value - min_value)

print("Original Ratings:", ratings)
print("Normalized Ratings:", normalized)