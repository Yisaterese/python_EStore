from Bank.Account import Account
import pytest
from decimal import Decimal


def test_can_deposit():
    my_account1 = Account("Fidelity", "correctPin", 76546)
    my_account1.deposit(Decimal(3000))
    assert my_account1.check_balance("correctPin") == Decimal(3000)


def test_can_withdraw():
    my_account1 = Account("gtb", "correctPin", 7567)
    my_account1.deposit(Decimal(3000))
    my_account1.withdraw(Decimal(2000), "correctPin")
    assert my_account1.check_balance("correctPin") == Decimal(1000)


def test_account_can_check_balance():
    my_account1 = Account("gtb", "correctPin", 976)
    my_account1.deposit(Decimal(1000.0))
    assert my_account1.check_balance("correctPin") == Decimal(1000)


def test_withdraw_less_than_0_raise_insufficient_funds_exception():
    my_account1 = Account("gtb", "correctPin", 7567)
    my_account1.deposit(Decimal(1000.0))
    with pytest.raises(ValueError) as info:
        my_account1.withdraw(Decimal(-10), 7567)
    assert info.type == ValueError


def test_withdraw_more_than_balance_raise_value_error():
    my_account = Account("zenith", "correctPin", 3455)
    my_account.deposit(Decimal(3000))
    with pytest.raises(ValueError) as info:
        my_account.withdraw(Decimal(5000), "correctPin")
    assert info.type == ValueError