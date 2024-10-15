# Question 2: Write a program to accept marks of 6 students and display them in a sorted manner.

marks1 = int(input("Enter 1st Subject Marks :)"))
marks2 = int(input("Enter 2nd Subject Marks :)"))
marks3 = int(input("Enter 3rd Subject Marks :)"))
marks4 = int(input("Enter 4th Subject Marks :)"))
marks5 = int(input("Enter 5th Subject Marks :)"))
marks6 = int(input("Enter 6th Subject Marks :)"))

allMarks = [marks1,marks2,marks3,marks4,marks5,marks6]
allMarks.sort()
print("Marks is Sorted Order Are:")
print(allMarks)