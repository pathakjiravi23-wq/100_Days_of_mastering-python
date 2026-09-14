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


circle1 = Circle()
circle1.area(12)

rec1 = Rectangle()
rec1.area(10, 20)

tri = Triangle()
tri.area(5, 10)
