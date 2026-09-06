class Student:
    def __init__(self, my_name, my_age) -> None:
        self.name = my_name
        self.age = my_age

    def details(self):
        print("Name: ", self.name)
        print("age: ", self.age)


s1 = Student("Ravi", 22)
s1.details()


class MyInt(float):

    def __new__(cls, value):
        return super().__new__(cls, value)

    def __init__(self, value):
        print("self:", self)
        print("id(self):", id(self))


x = MyInt(10.0)

print("x:", x)
print("id(x):", id(x))
