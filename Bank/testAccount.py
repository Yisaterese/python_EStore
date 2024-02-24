from Bank.Account import Account
import pytest
from decimal import Decimal


def test_can_deposit():
    my_account1 = Account("Fidelity", "correctPin")
    my_account1.deposit(Decimal(3000))
    assert my_account1.check_balance("correctPin") == Decimal(3000)


def test_can_withdraw():
    my_account1 = Account("gtb", "correctPin")
    my_account1.withdraw(Decimal(2000), "correctPin")
    assert my_account1.check_balance("correctPin") == Decimal(1000)


def test_account_can_check_balance():
    my_account1 = Account("gtb", "correctPin")
    my_account1.deposit(Decimal(1000.0))
    assert my_account1.check_balance("correctPin") == Decimal(1000)
