import math

class Circle:
    def area(self):
        r = 5
        print("Circle Area:", math.pi * r * r)


class Rectangle:
    def area(self):
        l = 10
        w = 5
        print("Rectangle Area:", l * w)


class Triangle:
    def area(self):
        b = 10
        h = 6
        print("Triangle Area:", 0.5 * b * h)


# Creating objects
c = Circle()
r = Rectangle()
t = Triangle()

# Same method for different objects
for shape in (c, r, t):
    shape.area()