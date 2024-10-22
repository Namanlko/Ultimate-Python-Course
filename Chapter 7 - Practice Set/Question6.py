# Question 6: Write a program to calculate the factorial of a given number using for loop.

n = int(input("Enter Value of n?"))

fact=1
for i in range(1,n+1,1):
    fact = fact*i

print("Factorial is",fact) 