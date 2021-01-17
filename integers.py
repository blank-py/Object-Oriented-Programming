# File name: integers.py
# Author: Jesse Malinen
# Description: reads integers until user input is 0
#                     and counts number of negative integers

numList = []


num = input("input an integer (0 stops):")


while num !=0:
    num = int(input("Input an integer (0 terminates):"))
    if num == 0:
        break
    else:
        numList.append(num)


print("Terminated")


print("Negative integers in the list: ", (sum(1 for num in numList if num <0)))



