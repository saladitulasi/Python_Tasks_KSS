
# Student Marks Management System

# Tuple to store subject names
subjects = ("Python", "Java", "C++")

# Set to maintain unique student names
students = set()

# Dictionary to store student marks
student_records = {}


# Function to add a student
def add_student():
    try:
        name = input("Enter student name: ")

        if name in students:
            print("Student already exists!")
            return

        marks = []

        for subject in subjects:
            mark = float(input(f"Enter marks in {subject}: "))

            if mark < 0 or mark > 100:
                print("Marks must be between 0 and 100.")
                return

            marks.append(mark)

        students.add(name)
        student_records[name] = marks

        print("Student added successfully!")

    except ValueError:
        print("Error: Please enter numeric marks only.")


# Recursive function to calculate total marks
def calculate_total(marks):
    if not isinstance(marks, list):
        raise TypeError("Marks must be stored in a list.")

    if len(marks) == 0:
        return 0

    return marks[0] + calculate_total(marks[1:])


# Function to display all student records
def display_students():
    if not student_records:
        print("No student records available.")
        return

    print("\n--- Student Records ---")

    for name, marks in student_records.items():
        print("\nStudent Name:", name)

        for i in range(len(subjects)):
            print(subjects[i], ":", marks[i])

        print("Total Marks:", calculate_total(marks))
        print("Average Marks:", calculate_average(name))


# Function to calculate average marks
def calculate_average(name):
    try:
        if name not in student_records:
            raise NameError("Student name does not exist.")

        marks = student_records[name]

        if not isinstance(marks, list):
            raise TypeError("Incorrect data type for marks.")

        total = calculate_total(marks)
        average = total / len(marks)

        return average

    except NameError as e:
        print("Error:", e)
        return None

    except TypeError as e:
        print("Error:", e)
        return None

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None


# Main menu
while True:
    print("\n===== STUDENT MARKS MANAGEMENT =====")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Calculate Student Average")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_student()

        elif choice == 2:
            display_students()

        elif choice == 3:
            name = input("Enter student name: ")
            average = calculate_average(name)

            if average is not None:
                print("Average Marks of", name, "=", average)

        elif choice == 4:
            print("Exiting program. Thank you!")
            break

        else:
            print("Invalid choice! Please select 1 to 4.")

    except ValueError:
        print("Error: Please enter a valid numeric choice.")

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

    except TypeError:
        print("Error: Incorrect data type.")

