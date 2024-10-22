# Question 8: Write a program to print the following star pattern.

#       *
#     * * *
#   * * * * *
# * * * * * * *

n = int(input("Enter Value of n?"))
for i in range(n):
    print(" "*(n-i-1),end="")
    print("*"*(2*i+1),end="")
    print(" "*(n-i-1))
    