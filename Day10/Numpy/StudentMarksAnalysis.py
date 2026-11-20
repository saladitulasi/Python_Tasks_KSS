import numpy as np

# Store student marks
marks = [45, 67, 89, 56, 72]

# Convert list into NumPy array
arr = np.array(marks)

# Add 5 grace marks
updated_marks = arr + 5

# Print updated marks
print("Updated Marks:", updated_marks)