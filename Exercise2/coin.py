# File name: coin.py
# Author: Jesse Malinen
# Description: short script for tossing a coin


import random

class Coin:
    
    # The __init__ method initializes the sideup data attribute with 'heads'
    
    def __init__(self):
        self.sideup = 'Heads'
    
    # The toss method generates a random number
    # in the range of 0 through 2. If the number is
    # 0, then the sideup is set to 'Heads',
    # 1 it is set to 'Tails',
    # 2 it is set to 'Upright on the table, no side is up',
    # and otherwise is set to 'Fell into a rabbit hole and disappeared'
    
    def toss(self):
        if random.randint(0, 2) == 0:
            self.sideup = 'Heads'
        elif random.randint(0, 2) == 1:
            self.sideup = 'Tails'
        elif random.randint(0, 2) == 2:
            self.sideup = 'Upright, no side is up'
        else:
            self.sideup = 'into a rabbit hole and disappeared.'
    
    # The get_sideup method returns the value referenced by sideup
            
    def get_sideup(self):
        return self.sideup
    
    
# The main function

def main():
    
    # Create an object from the Coin class.
    my_coin = Coin()
    #your_coin = Coin()
    
    # Display the side of the coin that is facing up.
    print('This side is up:', my_coin.get_sideup())
    
    # Toss the coin.
    print('I am tossing the coin ...')
    my_coin.toss()
    
    # Display the side of the coin that is facing up.
    print('The coin has landed:', my_coin.get_sideup())

    
# Call the main function.
main()