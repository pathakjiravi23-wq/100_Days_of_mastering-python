# Q6. Create a Student class with:


# instance method display()
# class method change_college()
# static method is_valid_age()
class Student:
    college = "NIT"  # class attribute

    def __init__(self, name, stream):
        self.Name = name
        self.Stream = stream

    # instance method
    def display(self):
        print(f"His NAME is {self.Name} He is studying related to {self.Stream}")

    @classmethod
    def change_college(
        cls, new_college
    ):  # class method( used to alter class attributes)
        cls.college = new_college
        return cls.college

    @staticmethod
    def is_valid_age(
        age,
    ):  # static method which do not require any object or class attributes
        return age > 18


# iniatilize object
s1 = Student("RAVI", "CSE")
# invoke instance method
s1.display()

# Invoke class method
Student.change_college("IIT")
print(Student.college)

# Invoke static method
print(Student.is_valid_age(18))
