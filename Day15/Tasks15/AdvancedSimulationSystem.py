import random
import numpy as np
import pandas as pd
import math

# Create Student class
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # Assign grade
    def get_grade(self):

        if self.marks >= 90:
            return "A"

        elif self.marks >= 75:
            return "B"

        elif self.marks >= 60:
            return "C"

        elif self.marks >= 40:
            return "D"

        else:
            return "Fail"


try:
    # Number of students
    n = int(input("Enter number of students: "))

    if n <= 0:
        raise ValueError("Number of students must be positive")

    names = []
    marks = []

    # Generate random marks
    for i in range(n):

        name = input("Enter student name: ")

        mark = random.randint(0, 100)

        names.append(name)
        marks.append(mark)

    # Convert marks into NumPy array
    marks_array = np.array(marks)

    # Create Pandas DataFrame
    data = pd.DataFrame({
        "Name": names,
        "Marks": marks_array
    })

    print("\nExam Results:")
    print(data)

    # Create Student objects
    students = []

    for i in range(n):
        student = Student(names[i], marks[i])
        students.append(student)

    # Display grades
    print("\nStudent Grades:")

    grades = []

    for student in students:

        grade = student.get_grade()

        grades.append(grade)

        print(
            student.name,
            "- Marks:",
            student.marks,
            "- Grade:",
            grade
        )

    # Add grades to DataFrame
    data["Grade"] = grades

    # Calculate statistics using math
    total = sum(marks)
    average = math.ceil(total / n)

    highest = max(marks)
    lowest = min(marks)

    print("\nExam Statistics:")
    print("Average Marks:", average)
    print("Highest Marks:", highest)
    print("Lowest Marks:", lowest)

    # Save report to file
    with open("exam_report.txt", "w") as file:

        file.write("EXAM RESULT REPORT\n")
        file.write("==================\n")

        for student in students:

            file.write(
                f"Name: {student.name}, "
                f"Marks: {student.marks}, "
                f"Grade: {student.get_grade()}\n"
            )

        file.write(f"\nAverage Marks: {average}")
        file.write(f"\nHighest Marks: {highest}")
        file.write(f"\nLowest Marks: {lowest}")

    print("\nReport saved successfully!")

except ValueError as e:
    print("Invalid Input:", e)

except Exception as e:
    print("Error:", e)