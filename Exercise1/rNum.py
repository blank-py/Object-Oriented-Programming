# File name: rNum.py
# Author: Jesse Rantakangas
# Description: Returns random number between 1-6 when called

import random # we need this to get random numbers

def randomNum(): # defining the function
    
    return random.randint(1, 6) # exercise cleverly pointed out that the function returns the number
    
print("Random number is :", randomNum()) # calling the function inside the print statement