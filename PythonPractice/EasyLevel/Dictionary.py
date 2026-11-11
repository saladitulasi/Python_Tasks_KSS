students = {
    "Tulasi": 85,
    "jay": 90,
    "vardhan": 78
}

# Add a new student
students["ravi"] = 95

# Update existing student's marks
students["Tulasi"] = 92

# Print all student details
for name, marks in students.items():
    print(name, ":", marks)