
"""Inherinting the super class Bank Account"""

from Noel_BankAccount import BankAccount
"""SUB CLASS: checking account"""

class CheckingAccount(BankAccount):
    #creating a new class and inheriting from the super class BankAccount
    
    def __init__(self, customer, bank, balance, transaction_fee = 3.00):
        """ Create a new class of customer checking account
    
        The initial balance of the chequing account is 0
    
        takes:
            customer_name from the base class BankAccount
            bank_name from the base class BankAccount
            balance from the base class BankAccount
            transac_fee --> applied on purchases from the checking account
        """
    
        super().__init__(customer, bank, balance) #call from the super cpnstructor
        self._transaction_fee = transaction_fee
    
    """
    methods that make purchase, 
    call withdraw function form the super class
    and apply transaction fees
    """
    
    #making a purchase
    def make_purchase(self, amount, transaction_fee): #deducts purchase amount from BankAccount
        
        successiful_purchase = super().withdraw(amount) #call inherited method
        
        
        if successiful_purchase: #checks if amount in BankAccount > than purchase amount
            print('A ${} successiful transaction has been completed.'.format(amount))
            self._balance.__sub__(amount) #deduct amount
            print('A ${} transaction fee has been applied.'.format(self._transaction_fee))
            
            self._balance = self._balance.__sub__(self._transaction_fee) #deduct transaction fee
            print('Your new balance is ${}.'.format(self._balance))
            
        elif not successiful_purchase: #checks if amount in BankAccount = 0 or < purchase amount
            print('Can not complete purchase! Your account balance is ${}'.format(self._balance))
           
        return successiful_purchase


""" TEST UNIT FOR CHECKING ACCOUNT"""
if __name__ == '__main__':
    
    """define an empty list of account instances"""

    accounts = []

    """testing instances of bank accounts from the list 'accounts'."""
    accounts.append(CheckingAccount('Chandler Bing', 'Dejardins Bank', 0))
    accounts.append(CheckingAccount('Tony Stark', 'ROyal Bank of Canada', 3000))

    for index in range(len(accounts)):
        """
        executing methods:
            get_customer()
            bank_name()
            get_balance()
            deposit()
            withdraw()
            make_purchase
        """
        print('\nAccount Holder: {}'.format(accounts[index].customer_name()))
        print('Institution name: {}'.format(accounts[index].bank_name()))
        print('Available funds: {}\n'.format(accounts[index].get_balance()))
        print('Available funds: {}\n'.format(accounts[index].make_purchase(500,3)))
        print('Available funds: {}\n'.format(accounts[index].deposit(10)))
        print('_'*50+'\n')