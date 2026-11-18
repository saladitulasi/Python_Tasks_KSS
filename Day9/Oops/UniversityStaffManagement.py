class Staff:
    def __init__(self, name, staff_id):
        self.name = name
        self.staff_id = staff_id

    def display(self):
        print("Name:", self.name)
        print("Staff ID:", self.staff_id)


class Professor(Staff):
    def show(self):
        self.display()
        print("Role: Professor")


class LabAssistant(Staff):
    def show(self):
        self.display()
        print("Role: Lab Assistant")


class Administrator(Staff):
    def show(self):
        self.display()
        print("Role: Administrator")


p = Professor("Rahul", 101)
l = LabAssistant("Priya", 102)
a = Administrator("Arun", 103)

print("Professor Details:")
p.show()

print("\nLab Assistant Details:")
l.show()

print("\nAdministrator Details:")
a.show()