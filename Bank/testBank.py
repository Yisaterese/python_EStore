import pytest
from _decimal import Decimal

from Bank import Account
from Bank.Bank import Bank
from Bank.InvalidPinError import InvalidPinError


def test_bank_can_register_customer():
    bank = Bank("zenith")
    bank.register_customer("Akinlade", "Mandela", "correct_pin")
    bank.register_customer("Akinyemi", "Mojo", "correct_pin")
    assert bank.get_number_of_accounts() == 2


def test_bank_deposit():
    bank = Bank("Obiakpor")
    account1: Account = bank.register_customer("Akande", "Jonathan", "incorrect_pin")
    account2: Account = bank.register_customer("Fanen", "Jona", "incorrect_pin")
    bank.deposit(500, account1)
    assert bank.check_balance(account1, "correct_pin") == 500


def test_bank_withdraw_with_wrong_pin_raise_invalid_pin_error():
    bank = Bank("Obiakpor")
    account1: Account = bank.register_customer("Akande", "Jonathan", "incorrect_pin")
    account2: Account = bank.register_customer("Fanen", "Jona", "incorrect_pin")
    assert bank.get_number_of_accounts() == 2
    bank.deposit(20000, account2)
    assert bank.check_balance(account2, "correct_pin")
    with pytest.raises(InvalidPinError) as info:
        bank.withdraw(Decimal(5000), account2, "Incorrect_pin")
    assert info.type == InvalidPinError


def test_bank_check_balance():
    bank = Bank("Dayo Ajor co-operative society")
    account1: Account = bank .register_customer("agbende", "ajangbadi","correct_pin")
    bank.deposit(4000,account1)
    assert bank.check_balance(account1,"correctPin") == 4000


def test_bank_can_register_three_account_remove_the_second():
    bank = Bank("Access")
    account1: Account = bank.register_customer("Oko", "Bioke", "correctPin")
    account2: Account = bank.register_customer("Ako", "Bike", "correctPin")
    account3: Account = bank.register_customer("uko", "Bie", "correctPin")
    bank.remove(account2, "correctPin")
    assert bank.get_account_number() == 2




def test_bank_withdraw():
    bank = Bank("Obiakpor")
    account1: Account = bank.register_customer("Akande", "Jonathan", "incorrect_pin")
    print(account1)
    account2: Account = bank.register_customer("Fanen", "Jona", "incorrect_pin")
    print(account2)
    assert bank.get_number_of_accounts() == 2
    bank.deposit(20000, account2)
    assert bank.check_balance(account2, "correct_pin")
    bank.withdraw(Decimal(5000), account2, "correct_pin")
    assert bank.check_balance(account2, "correct_pin") == 15000