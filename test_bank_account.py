import pytest
from bank_account_management_system_v2 import SavingsAccount


def test_balance_positive_after_deposit_withdraw_and_interest():
    account = SavingsAccount("Artur")

    account.deposit(500)
    account.withdraw(100)
    account.apply_interest()

    assert account.get_balance() > 0
