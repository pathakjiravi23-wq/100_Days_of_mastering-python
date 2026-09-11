class BankAccount:
    def __init__(self, balance, name):
        self.__balance = balance  # private attribute
        self._name = name  # protected attribute

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self.__balance += amount
        else:
            print("Insufficiant balance")


s1 = BankAccount(10000, "Ravi")
print(s1.balance)

s1.balance = 20000
print(s1.balance)
