from decimal import Decimal
class Account:
    def __init__(self,name,balance ):
        self.name = name
        self._balance = balance



    @property
    def balance(self):
        return self._balance

    @balance.setter

    def balance(self, balance: Decimal):
        if balance < Decimal(0.00):
            raise ValueError("Invalid amount for balance")
        self._balance = balance

    def withdraw(self, amount:Decimal, pin):
        self.balance -= Decimal(amount)

    def deposit(self,depositAmount:Decimal):
       self.balance += Decimal(depositAmount)

    def check_balance(self,pin):
        return self._balance

    def get_name(self):
        return self.name

    #overriding the tostring method
   # def __repr__(self):
         #   return f"Your account name is: {self.name}\nYour account Balance is: #{self.balance}"



