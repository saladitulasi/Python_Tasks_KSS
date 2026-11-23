import numpy as np

# List of student roll numbers
roll_numbers = [101, 102, 103, 104, 105, 106]

# Convert list into NumPy array
arr = np.array(roll_numbers)

# Extract middle students using slicing
middle_students = arr[2:5]

# Print the result
print("All Roll Numbers:", arr)
print("Middle Students:", middle_students)