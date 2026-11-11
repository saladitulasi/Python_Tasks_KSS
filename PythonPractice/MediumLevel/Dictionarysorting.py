students = {
    "Rahul": 85,
    "Amit": 92,
    "Priya": 78,
    "Sneha": 95
}

# Sort dictionary by marks
sorted_students = sorted(
    students.items(),
    key=lambda x: x[1],
    reverse=True
)

print("Sorted students:")

for name, marks in sorted_students:
    print(name, ":", marks)

# Print top two students
print("\nTop two students:")

for name, marks in sorted_students[:2]:
    print(name, ":", marks)