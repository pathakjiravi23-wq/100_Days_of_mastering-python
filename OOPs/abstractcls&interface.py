from abc import ABC, abstractmethod

# Q13. Create a payment system:

# Payment
#  ├── UPI
#  ├── CreditCard
#  └── PayPal

# Every class must implement:


# pay()
class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass


class Upi(Payment):
    def pay(self):
        print("Payemnt successfull through upi!")


class CreditCard(Payment):
    def pay(self):
        print("Payemnt successfull through CreditCard!")


class PayPal(Payment):
    def pay(self):
        print("Payemnt successfull through PayPal!")


transaction = Upi()
transaction.pay()

transaction = CreditCard()
transaction.pay()

transaction = PayPal()
transaction.pay()
