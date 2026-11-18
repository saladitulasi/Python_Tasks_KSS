# Base class
class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed


# Derived class
class Car(Vehicle):
    def display(self):
        print("Car Brand:", self.brand)
        print("Car Speed:", self.speed)


class Bike(Vehicle):
    def display(self):
        print("Bike Brand:", self.brand)
        print("Bike Speed:", self.speed)


# Creating objects
c1 = Car("Toyota", 120)
b1 = Bike("Honda", 80)

c1.display()
b1.display()