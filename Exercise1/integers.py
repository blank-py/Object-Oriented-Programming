# File name: integers.py
# Author: Jesse Malinen
# Description: reads integers until user input is 0
#                     and counts number of negative integers

numList = []

def integreader():
    while True:
        num = int(input("Input an integer (0 terminates):"))
        if num == 0:
            break
        else:
            numList.append(num)


    print("Terminated")
    print("Negative integers in the list: ", (sum(1 for num in numList if num <0)))

def evenreader():
    even_sum = 0
    even_sum = sum(1 for num in numList if num % 2 == 0)
    print("Even integers in the list: ", (even_sum))

def divreader():
    div_sum = 0
    div_sum = sum(num for num in numList if num > 0 and num % 3 == 0)

    print("Sum of positive integers divisible by 3: ", (div_sum))

integreader()
evenreader()
divreader()