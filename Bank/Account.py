from decimal import Decimal


class Account:
    def __init__(self, name: str, pin: str):
        self.name = name
        self.pin = pin

    def __init__(self, accountNumber: int):
        self.accountNumber = accountNumber
        self._balance = Decimal

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance: Decimal):
        if balance < Decimal(0.00):
            raise ValueError("Invalid amount for balance")
        self._balance = balance

    def withdraw(self, amount: Decimal, pin):
        self.balance -= Decimal(amount)

    def deposit(self, depositAmount: Decimal):
        self.balance += Decimal(depositAmount)

    def check_balance(self, pin):
        return self._balance

    def get_name(self):
        return self.name
