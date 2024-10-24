# Question 4: Write a recursive function to calculate the sum of first n natural number.

def Sum(n):
    if n==1:
        return 1
    else:
        return n + Sum(n-1)
    
print(Sum(10))