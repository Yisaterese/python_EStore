from decimal import Decimal

from Bank.Account import Account
from Bank.InvalidAccountError import InvalidAccountError
from Bank.InvalidPinError import InvalidPinError


class Bank:
    accounts = None

    def __init__(self, name: str):
        self.name = name
        self.account_number = 1234567890
        self.accounts = []

    def register_customer(self, first_name: str, last_name: str, pin: str):
        my_account = Account(first_name + " " + last_name, pin)
        my_account.set_account_number(self.account_number)
        # self.account_number += 1
        self.accounts.append(my_account)
        return my_account

    def get_number_of_accounts(self):
        return len(self.accounts)

    # def generate_account_number(self):
    #     random.randint
    def deposit(self, amount, account_number):
        for all_accounts in self.accounts:
            all_accounts.deposit(amount)

    def check_balance(self, account_number, pin):
        for account in self.accounts:
            return account.check_balance(pin)

    def get_account_number(self):
        return self.account_number

    def withdraw(self, amount: Decimal, account_number, pin):
        for account in self.accounts:
            if self.account_number == account_number:
                account.withdraw(amount, pin)
            if not self.valid(pin):
                raise InvalidPinError("Incorrect pin")


    @classmethod
    def valid(cls, pin):
        return Account.is_valid_length_of(pin)

    def remove(self, account_number: int, pin: str):
        accoubt: Account = self.find_account(account_number)
        if not self.valid(pin):
            raise InvalidPinError("Incorrect pin")

    def find_account(self, account_number):
        for account in self.accounts:
            if self.account_number == account_number:
                return account
            raise InvalidAccountError("account number does not exist")
