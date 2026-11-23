import numpy as np

# Original image data
image = [[1, 2, 3],
         [4, 5, 6]]

# Convert into NumPy array
arr = np.array(image)

# Flatten the array into 1-D
flat_arr = arr.flatten()

# Print the flattened array
print("Original Array:")
print(arr)

print("Flattened Array:")
print(flat_arr)