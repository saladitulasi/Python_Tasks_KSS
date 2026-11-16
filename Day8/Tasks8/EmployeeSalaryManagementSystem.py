# Employee Salary Management System

# Read employee data from file
file = open("employees.txt", "r")

employees = []

print("Employee Details:")
print("------------------")

for line in file:
    name, salary = line.split()
    salary = int(salary)

    employees.append((name, salary))
    print("Name:", name, "Salary:", salary)

file.close()

# Find employee with highest salary
if employees:
    highest = max(employees, key=lambda x: x[1])

    print("\nEmployee with Highest Salary:")
    print("Name:", highest[0])
    print("Salary:", highest[1])

# Append a new employee record
file = open("employees.txt", "a")

name = input("\nEnter new employee name: ")
salary = int(input("Enter employee salary: "))

file.write(name + " " + str(salary) + "\n")

file.close()

print("New employee record added successfully!")