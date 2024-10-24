# Question 5: Write a python function to print first n lines of the following star pattern as shown below for n=3.

# * * *
# * *
# *

n = int(input("Enter Value of n?"))

def Pattern(n):
    for i in range(0,n):
        for j in range(n-i):
            print("*",end=" ")
        print()

Pattern(n)