# Question 5: Write a program to find the sum of first n natural numbers using while loops.

n = int(input("Enter Value of n?"))

sum=0
i=1
while i<=n:
    sum = sum+i
    i=i+1

print("Sum is",sum)