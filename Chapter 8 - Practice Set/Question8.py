# Question 8: Write a function in python program to print the print multiplication table of a given number.

def Table(n):
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")

n = int(input("Enter Value of n?"))
Table(n)