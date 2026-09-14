# Q10. Create:
# Employee
#  ├── Developer
#  └── Manager
# Override a method called work().


class Employee:
    def __init__(self, company, role):
        self.role = role
        self.company = company

    def company_details(self):
        print("Organization:", self.company)

    def work(self):
        print("Role:", self.role)


class Developer(Employee):
    def work(self):  # overriding
        print("Job Role:", self.role)


class Manager(Employee):
    def work(self):  # overriding
        print("Job Role:", self.role)


d1 = Developer("GOOGLE", "DEVELOPER")
m1 = Manager("GOOGLE", "MANAGER")

d1.company_details()
d1.work()
m1.company_details()
m1.work()

# Types of Inheritance: single inheritance
# multilevel inheritance
# multiple inheritance
