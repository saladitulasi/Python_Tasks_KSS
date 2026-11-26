# Create Employee class
class Employee:

    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        print("ID:", self.emp_id)
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("-------------------")


# Dictionary to store employees
employees = {}

try:
    n = int(input("Enter number of employees: "))

    for i in range(n):

        emp_id = input("\nEnter Employee ID: ")
        name = input("Enter Employee Name: ")

        try:
            salary = float(input("Enter Employee Salary: "))

            if salary < 0:
                raise ValueError("Salary cannot be negative")

            emp = Employee(emp_id, name, salary)

            employees[emp_id] = emp

        except ValueError as e:
            print("Invalid Salary:", e)

    # Display all employees
    print("\nEmployee Details")

    for emp in employees.values():
        emp.display()

    # Save employee details to file
    with open("employees.txt", "w") as file:

        for emp in employees.values():
            file.write(
                f"ID: {emp.emp_id}, "
                f"Name: {emp.name}, "
                f"Salary: {emp.salary}\n"
            )

    print("Employee data saved successfully!")

except ValueError:
    print("Invalid number of employees!")

except Exception as e:
    print("Error:", e)