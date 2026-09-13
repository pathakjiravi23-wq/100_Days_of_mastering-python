class BankAccount:
    def __init__(self, balance, name):
        self.__balance = balance  # private attribute
        self._name = name  # protected attribute

    @property  # getter for controlled access
    def balance(self):
        return self.__balance

    @balance.setter  # setter for controlled modification
    def balance(self, amount):
        if amount >= 0:
            self.__balance += amount
        else:
            print("Insufficiant balance")


s1 = BankAccount(10000, "Ravi")
print(s1.balance)

s1.balance = 20000
print(s1.balance)
print(s1._name)
s1._name = "BUBU"
print("protected fields,Could be Updated ", s1._name)
print(
    s1.__balance
)  # error because it is now having controlled access u can use .balance(getter) for accessing private attribute
