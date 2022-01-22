# File name: list.py
# Author: Jesse Rantakangas
# Description: prints out two user input lists

numberList = [] # define the list
print("Input 10 numbers:")

# getting user inputs
## don't know if there's a better way, hopefully
num1 = int(input("Enter 1st value: "))
num2 = int(input("Enter 2nd value: "))
num3 = int(input("Enter 3rd value: "))
num4 = int(input("Enter 4th value: "))
num5 = int(input("Enter 5th value: "))
num6 = int(input("Enter 6th value: "))
num7 = int(input("Enter 7th value: "))
num8 = int(input("Enter 8th value: "))
num9 = int(input("Enter 9th value: "))
num10 = int(input("Enter 10th value: "))

# replacing the empty list with user input
numberList = [num1, num2, num3, num4, num5, num6, num7, num8, num9, num10]

wordList = [] # define the list

print("Input 10 words:")

# user inputs
w1 = input("Enter 1st word: ")
w2 = input("Enter 2nd word: ")
w3 = input("Enter 3rd word: ")
w4 = input("Enter 4th word: ")
w5 = input("Enter 5th word: ")
w6 = input("Enter 6th word: ")
w7 = input("Enter 7th word: ")
w8 = input("Enter 8th word: ")
w9 = input("Enter 9th word: ")
w10 = input("Enter 10th word: ")

# replace empty list
wordList = [w1, w2, w3, w4, w5, w6, w7, w8, w9, w10]

print("Integers: ", numberList)
print("Strings: ", wordList)

# sort the lists
numberList.sort()
print("Sorted number list: ", numberList)

wordList.sort()
print("Sorted word list: ", wordList)

# randomise the integer list
import random
numberList = random.sample(range(1,101), 10)
print("Here's a list of 10 random numbers:")
print(numberList)

