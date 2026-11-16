# Take student name as input
name = input("Enter student name: ")

# Append the name to the file
with open("attendance.txt", "a") as file:
    file.write(name + "\n")

# Display the contents of the file
print("\nStudent Attendance Record:")

with open("attendance.txt", "r") as file:
    print(file.read())