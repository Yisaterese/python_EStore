

from Bank.Account import Account

from decimal import Decimal

def test_can_deposit():
    my_account1 = Account("Fidelity", 0)
    my_account1.deposit(Decimal(3000))
    assert my_account1.check_balance() == Decimal(3000)

def test_can_withdraw():
    my_account1 = Account("gtb", 0)
    my_account1.withdraw(2000, "correctPin")
    assert my_account1.check_balance("correctPin") == Decimal(1000)