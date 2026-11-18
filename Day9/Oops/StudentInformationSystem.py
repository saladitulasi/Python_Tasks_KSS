class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Marks:", self.marks)
        print("------------------")


# Creating objects
s1 = Student("Rahul", 101, 85)
s2 = Student("Priya", 102, 90)
s3 = Student("Amit", 103, 78)

# Displaying student details
s1.display()
s2.display()
s3.display()