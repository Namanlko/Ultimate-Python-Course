# Question 4: Write a program to find whether a given number is prime or not.

n = int(input("Enter Number :)"))
prime = True

for i in range(2,n):
    if (n%i == 0):
        prime = False

if(prime):
    print(f"{n} is a Prime Number :)")
else:
    print(f"{n} is not a Prime Number :|")