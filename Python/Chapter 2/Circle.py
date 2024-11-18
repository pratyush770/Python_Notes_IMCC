# Getter and Setter demonstration for Chapter 2.py
# If there are values which are mutating, then we make them private and access them through getters and setters.
import math


class Circle:
    _radius = 0.0  # private variable
    area = 0.0  # public variable

    def __init__(self, radius):
        self.setradius(radius)  # calling getter and setter

    def setradius(self, radius):
        if radius > 0.0:  # we can perform validations here which is not possible using =
            self._radius = radius  # _radius is private variable using _
            print(f"Radius is set...")
        else:
            print("Please enter a value greater than 0.0")

    def getradius(self):
        return self._radius

    def calarea(self):
        self.area = math.pi * self.getradius() * self.getradius()


rdVal = float(input("Enter the radius of the circle: "))
cir = Circle(rdVal)
cir.calarea()  # method to calculate the area
print(f"The area of the circle is : {cir.area}")  # directly calling cir.area instance variable
