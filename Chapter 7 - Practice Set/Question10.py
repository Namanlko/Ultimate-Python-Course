# Question 10: Write a program to print multiplication table of n using for loop in reversed order.

n = int(input("Enter value of n?"))
for i in range(10,0,-1):
    print(f"{n} X {i} = {n*i}")