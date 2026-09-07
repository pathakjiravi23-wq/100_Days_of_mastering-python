# Q1. Create a Car class with brand, model, and price.


class Car:
    def __init__(self, brand, modal, price):
        self.brand = brand
        self.model = modal
        self.price = price

    def car_details(self):
        print(
            f"Its a {self.brand}'s Car, {self.model} model its costs almost {self.price} rupees"
        )


c1 = Car("Fararie", "v1", 21)
c2 = Car("Lamboghini", "v2", 11)
c3 = Car("marcedecis", "v3", 31)

c1.car_details()
c2.car_details()
c3.car_details()


# Q2. Create a BankAccount class with account_holder and balance,Add deposit() and withdraw() methods and Create 3 different bank account objects and perform transactions.
class BankAccount:
    def __init__(self, acc_holder, balance):
        self.account_holder = acc_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Now your current Balance is : {self.balance}")

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficiant Balance")
        else:
            self.balance -= amount
            print(f"Left Balance: {self.balance}")


acc1 = BankAccount("Ravi", 12000)
acc1.deposit(20000)
acc2 = BankAccount("Jyoti", 200000)
acc2.withdraw(10000)
acc3 = BankAccount("Neha", 200000)
acc3.withdraw(10000)

# Q5. Create an Employee class where: company is common to everyone name, salary, and department are different


class Employee:
    company = "Juspay"

    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def check_details(self):
        print(
            f"Name: {self.name}\nSalary: {self.salary}\nDepartment: {self.department}\nCompany: {self.company}"
        )


empy1 = Employee("Ravi Pathak", 40000, "IT")
empy2 = Employee("Amit", 30000, "IT")
empy1.check_details()
empy2.check_details()
