def bonus(func):
    def wrapper(self):
        self.salary = self.salary + 5000
        func(self)
    return wrapper


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @bonus
    def display_salary(self):
        print("Employee Name:", self.name)
        print("Salary with Bonus:", self.salary)


e = Employee("Rahul", 25000)

e.display_salary()