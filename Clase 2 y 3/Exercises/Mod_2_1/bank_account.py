""" 
This module contains a BankAccount class 
to execute multiple bank movements from class methods 
"""

class BankAccount:

    """ This class contains multiple bank movements methods """

    def __init__(self, initial_balance=0):
        """
        Initialize the bank account with a main balance.

        Args:
            initial_balance (float): Main balance. 0 by default.
        """
        self.balance = initial_balance

    def deposit(self, amount):
        """
        Deposit a amount into the bank account.
        
        Args:
            amount (float): Amount value to deposit.
        
        Returns:
            float: New balance from bank account.
        """
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("You must deposit a higher amount")

        return self.balance

    def withdraw(self, amount):
        """
        Withdraw an amount from bank account if there's a enough balance.
        
        Args:
            amount (float): Amount to withdraw.
        
        Returns:
            float: New balance from account.
        
        Raises:
            ValueError: If amount to withdraw is higher than available balance.
        """
        if amount > self.balance:
            raise ValueError("Insufficient funds")

        self.balance -= amount

        return self.balance

    def get_balance(self):
        """
        Get current balance from bank account.
        
        Returns:
            float: Account current balance.
        """
        return self.balance
