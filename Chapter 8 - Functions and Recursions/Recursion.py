# Recursion: Recursion is a function which calls itself. It is used to directly use a mathematical formula as a function.

# Example - Factorial of a Number.

def Fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n * Fact(n-1)

print(Fact(7))