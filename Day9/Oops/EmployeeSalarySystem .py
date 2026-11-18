# Base class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


# Derived class
class Manager(Employee):
    def display(self):
        print("Employee Name:", self.name)
        print("Employee Salary:", self.salary)


# Creating object
m1 = Manager("Arun", 50000)

# Displaying details
m1.display()