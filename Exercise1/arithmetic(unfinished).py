# File name: arithmetic.py
# Author: Jesse Malinen
# Description: counts the number of terms in the AP, their sum
#                     and the sum of squared terms in the AP

def AProg(last_term, terms, term_sum, squared_sum):
    last_term = int(input("Please give the last term:"))
    
    div = 2
    terms = last_term % 2
    
    term_sum = (terms * (2 * a + (terms - 1) * div)) / 2
    