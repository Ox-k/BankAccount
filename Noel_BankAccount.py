"""Abtsratct base class"""

class BankAccount:
    """ Consumer bank account"""
    
    def __init__(self,customer, bank, balance):
        """ Create a new bank account
    
        The initial balance is 0
    
        customer_name --> name of the customer (e.g., John')
        bank_name     --> name of the bank (e.g., CIBC)
        deposit       --> deposit method (in $)
        withdraw      --> withdraw method (in $)
        """
    
        self._customer = str(customer)
        self._bank = str(bank)
        self._balance = float(balance)
    
    """methods to collect user data"""
    def customer_name(self):   #returns customer name
        return self._customer
    
    def bank_name(self):   #returns the name of banking institution
        return self._bank
    
    def get_balance(self):   #returns the balance
        return self._balance
    
    """methods that deposits funds in the account"""
    def deposit(self, amount):
        """
        get user input in $, and balance, adds them
        updates the account balance
        """
        if amount.__gt__(0):
            print('${} have been deposited'.format(amount))
            return self._balance.__add__(amount)
        elif amount.__lt__(0) | amount.__eq__(0):
            print('deposits funds cannot be 0 or less!')
        else:
            print('invalid balance')
            
    """method to withdraw funds from the account"""
    def withdraw(self, amount):
        """
        get user input in $, and balance, adds them
        updates the account balance
        """
        if self._balance.__lt__(0) or self._balance.__eq__(0):
            return False
        else:
            self._balance = self._balance.__sub__(amount)
            return True
            
    
    