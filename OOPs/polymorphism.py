import math


class Circle:
    def area(self, r: int):
        result = math.pi * r**2
        print("Area Of triangle: ", result)


class Rectangle:
    def area(self, length: int, width: int):
        result = length * width
        print("Area Of Triangle: ", result)


class Triangle:
    def area(self, base: int, height: int):
        result = 1 / 2 * base * height
        print("Area of triangle: ", result)


area = Circle()
area.area(12)

area = Rectangle()
area.area(10, 20)

area = Triangle()
area.area(5, 10)
