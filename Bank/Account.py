from decimal import Decimal


class Account:
    def __init__(self, name: str, pin: str, accountNumber: int):
        self.name = name
        self.pin = pin
        self.accountNumber = accountNumber
        self._balance = Decimal(0)




    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance: Decimal):
        if balance < Decimal(0.00):
            raise ValueError("Invalid amount for balance")
        self._balance = balance

    def withdraw(self, amount: Decimal, pin):
        if amount < Decimal(0.00):
            raise ValueError("Invalid amount for balance")
        self.balance -= Decimal(amount)

    def deposit(self, depositAmount: Decimal):
        self.balance += depositAmount#Decimal(depositAmount)

    def check_balance(self, pin):
        return self._balance

    def get_name(self):
        return self.name
