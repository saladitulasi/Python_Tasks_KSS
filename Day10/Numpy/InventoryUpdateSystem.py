import numpy as np

# Create inventory matrix
inventory = np.array([[10, 15],
                      [20, 25]])

# Add 2 units to every element
updated_inventory = inventory + 2

# Print updated inventory
print("Updated Inventory:")
print(updated_inventory)