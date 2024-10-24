# Question 1: Write a program using function to find greatest of three numbers.

def max(a,b,c):
    if a>b:
        if b>c:
            m = a
        else:
            m = c
    elif b>c:
        m = b
    else:
        m = c
    return m

print(max(1,10,6))