"""
This module contains BankAccount testing class, 
checking correct behaviors for BankAccount module methods
"""

import unittest
from bank_account import BankAccount


class TestBankAccount(unittest.TestCase):
    """
    Class which contains unit tests for BankAccount class
    """

    def test_deposit(self):
        """
        Verifying that deposit value was succesfully consigned 
        """
        account = BankAccount()
        # Arrange:
        amount = 100
        # Act:
        cur_balance = account.deposit(100)
        # Assert:
        self.assertEqual(cur_balance, amount, "Current balance must be the same value than amount")

    def test_withdraw(self):
        """
        Verifying that amount to withdraw is lower or equal to current balance
        """
        account = BankAccount(100)
        # Arrange:
        amount = 50
        balance = account.get_balance()
        # Act:
        cur_balance = account.withdraw(amount)
        # Assert:
        self.assertNotEqual(cur_balance, balance, "Current balance must be lower after withdrawal")
        # Case amount is higher than current balance
        with self.assertRaises(ValueError) as context:
            account.withdraw(100)
        # Assert:
        self.assertEqual(str(context.exception), "Insufficient funds")

    def test_current_balance(self):
        """
        Verifying that current balance is equal to amount parameter
        """
        # Arrange:
        amount = 300
        # -----------
        account = BankAccount(amount)
        # Act:
        result = account.get_balance()
        self.assertEqual(result, amount)


if __name__ == '__main__':
    unittest.main()
