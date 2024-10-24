# Question 6: Write a python function which converts the inches to cms.

def CM(n):
    return n*2.54

c = int(input("Enter in Inches :)"))
print(c,"Inches =",CM(c),"Centimetre")