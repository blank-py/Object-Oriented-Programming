# File name: accountTest.py
# Author: Jesse Malinen
# Description: Demonstrates the BankAccount class.

import bankAccount


def main():
    
    print('Hello')
    
    # Get the starting balance.
    start_bal = float(input("Enter the starting balance: "))
    
    # Get the owner 
    owner = input("Enter the owner: ")
    
    # Create a BankAccount object.
    savings = bankAccount.BankAccount(start_bal, owner)
    
    # Display the balance.
    print(savings)
    
    # Alternative way of displaying balance
    #print("Balance is: ",
    #      format(savings.get_balance(), ',.2f'), sep = ' ')
    
    # Get the amount to deposit.
    amount = float(input("Enter the amount to be deposited: "))
    savings.deposit(amount)
    
    # Display the balance.
    print(savings)

    # Get the amount to withdraw.
    amount = float(input("Enter the amount to be withdrawn: "))
    savings.withdraw(amount)
    
    # Display the balance.
    print(savings)
    
    
    
# Call the main function
main()