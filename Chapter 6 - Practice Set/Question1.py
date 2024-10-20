# Question 1: Write a program to find greatest of the four numbers enetered by the user.

n1 = int(input("Enter First Number :)"))
n2 = int(input("Enter Second Number :)"))
n3 = int(input("Enter Third Number :)"))
n4 = int(input("Enter Fourth Number :)"))

if n1>n2:
    if n1>n3:
        if n1>n4:
            mx = n1
elif n2>n3:
    if n2>n4:
        mx = n2
elif n3>n4:
    mx = n3
else:
    mx= n4

print("Maximum Value is",mx)
