# File name: task4.py
# Author: Jesse Malinen
# Description: Script that calculates averages score based on input

names = []
grades = []

while True:
    
    name = (input("Student's name: "))
    if name == "q":
        break
    else:
        names.append(name)
    
    grade = int(input("Student's grade: "))
    grades.append(grade)
    
    avg = sum(grades) / float(len(grades))
        
print("Average of the class: ", avg)