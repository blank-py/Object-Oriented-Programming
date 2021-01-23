# File Name: task2.py
# Author: Jesse Malinen
# Description: program that prints out user's grade based on their completions

Exercises = int(input("How many exercises have you completed?:"))

if Exercises < 9:
    print("You have failed the course due to lack of completed exercises.")
elif Exercises == 9:
    print("Your grade is 1.")
elif Exercises == 10:
    print("Your grade is 2.")
elif Exercises == 11:
    print("Your grade is 3.")
elif Exercises == 12:
    print("Your grade is 4.")
elif Exercises == 13 or Exercises > 13:
    print("Your grade is 5.")
else:
    print("Your input is incorrect.")

