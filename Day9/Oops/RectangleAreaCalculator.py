class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        area = self.length * self.width
        print("Area of Rectangle:", area)


# Creating object
r1 = Rectangle(10, 5)

# Calculating area
r1.calculate_area()