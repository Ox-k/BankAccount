#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 22:56:05 2022

@author: noelkodo
"""

"""Inherinting the super class Bank Account"""


"""SUB CLASS: Savings account"""




from Noel_BankAccount import BankAccount
class SavingsAccount(BankAccount):
    # creating a new class and inheriting from the super class BankAccount

    def __init__(self, customer, bank, balance, interest_rate=0):
        """Create a new class of customer Savings account

        The initial balance of the chequing account is 0

        takes:
            customer_name from the base class BankAccount
            bank_name from the base class BankAccount
            balance from the base class BankAccount
            interest_rate --> interest acrued
        """

        super().__init__(customer, bank, balance)  # call from the super constructor
        self._interest_rate = interest_rate

        """
        methods that accrue interest, 
        update the new balance with interest accrued.
   
        """
        

    
    def accrue_interest(self, interest_rate):
        savings = super().get_balance()
        # call inherited deposit method to supply balance
        if savings.__gt__(0):
            
            """ Calculating the total interest"""
            def __mul__(self, interest_rate):
                return float.__mul__(self._balance, interest_rate)
            print('${} annual interest has been accrued on a rate of {}%'.format(
                __mul__(self, interest_rate), interest_rate))
            
            """ adding the total interest to update amount"""
            def __add__(self,balance,interest_rate):
                return float.__add__(self._balance, float.__mul__(self._balance, interest_rate))
            
            """updating amount """
            self._balance = float.__add__(self._balance, float.__mul__(self._balance, interest_rate))
            
            return self._balance
        elif savings.__lt__(0) | self._balance.__eq__(0):
            print("Insufficient funds to accrue interest!")
        else:
            print("invalid balance")
            
        return savings

    

""" TEST UNIT FOR SAVINGS ACCOUNT"""
if __name__ == '__main__':

    """define an empty list of account instances"""

    accounts = []

    """testing instances of bank accounts from the list 'accounts'."""
    accounts.append(SavingsAccount('Chandler Bing', 'Dejardins Bank', 0))
    accounts.append(SavingsAccount('Tony Stark', 'ROyal Bank of Canada', 3000))

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
        print('Available funds: {}\n'.format(
            accounts[index].accrue_interest(0.023)))
        print('Available funds: {}\n'.format(accounts[index].deposit(10)))
        print('_'*50+'\n')
