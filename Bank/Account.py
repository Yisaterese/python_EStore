from decimal import Decimal


class Account:
    def __init__(self, name: str, pin: str):
        self.account = None
        self.name = name
        self.pin = pin
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

    def deposit(self, depositAmount: Decimal) -> None:
        self.balance += depositAmount  # Decimal(depositAmount)

    def check_balance(self, pin) -> Decimal:
        return self._balance

    def set_account_number(self, account_number: int) -> None:
        self.account_number = account_number

    @classmethod
    def is_valid_length_of(cls, pin):
        return len(pin) == 10


