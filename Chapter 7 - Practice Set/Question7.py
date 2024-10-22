# Question 7: Write a program to print the following star pattern.

# *
# * *
# * * *
# * * * *

# Method 1
for i in range(1,5):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

# Method 2
for i in range(1,5):
    print("* "*i)