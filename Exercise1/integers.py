# File name: integers.py
# Author: Jesse Rantakangas
# Description: reads integers until user input is 0
#                     and counts number of negative integers

numList = [] # define the list

# define the function getting integers
def integreader():
    while True:
        num = int(input("Input an integer (0 terminates):"))
        if num == 0:
            break
        else:
            numList.append(num)


    print("Terminated")
    print("Negative integers in the list: ", (sum(1 for num in numList if num <0)))

# define the function checking evens
def evenreader():
    even_sum = 0
    even_sum = sum(1 for num in numList if num % 2 == 0)
    print("Even integers in the list: ", (even_sum))

# define the functions checking divisible by 3
def divreader():
    div_sum = 0
    div_sum = sum(num for num in numList if num > 0 and num % 3 == 0)

    print("Sum of positive integers divisible by 3: ", (div_sum))

# call functions, although this could propably be done using classes and one main function
integreader()
evenreader()
divreader()