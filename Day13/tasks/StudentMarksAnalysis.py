import numpy as np

marks = np.array([
    [70, 80, 90],
    [60, 75, 85],
    [50, 65, 70],
    [90, 95, 85],
    [40, 55, 60]
])
# Calculate total marks of each student
total_marks = np.sum(marks, axis=1)

# Calculate class average
class_average = np.mean(total_marks)

# Identify students above class average
above_average = total_marks[total_marks > class_average]

print("Total Marks:", total_marks)
print("Class Average:", class_average)
print("Students Above Average:", above_average)