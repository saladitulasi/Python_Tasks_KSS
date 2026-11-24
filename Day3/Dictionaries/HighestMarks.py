students = {
    "Tulasi": 85,
    "Jay": 90,
    "Vardhan": 78
}

topper = max(students, key=students.get)

print("Student with highest marks:", topper)
print("Highest marks:", students[topper])