import math

# List of tuples
students = [
    ("Arun", 85),
    ("Bala", 45),
    ("Charan", 75),
    ("Divya", 90),
    ("Esha", 35)
]

# Convert list of tuples into dictionary
student_dict = dict(students)

print("Student Scores:")
for name, marks in student_dict.items():
    print(name, ":", marks)

# Find students scoring above 50
print("\nStudents scoring above 50:")

for name, marks in student_dict.items():
    if marks > 50:
        print(name, ":", marks)

# Calculate average using math module
total = sum(student_dict.values())
average = math.ceil(total / len(student_dict))

print("\nAverage Marks:", average)

# Store results in a text file
with open("students.txt", "w") as file:
    file.write("Student Results\n")

    for name, marks in student_dict.items():
        file.write(f"{name}: {marks}\n")

    file.write(f"Average Marks: {average}")

print("\nResults saved successfully!")