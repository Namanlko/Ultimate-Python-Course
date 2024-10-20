# Question 5: Write a program which find whether a given user name contains less than 10 characters or not.

name = input("Enter Your Name :)")

if(len(name)<10):
    print("Name contains less than 10 Characters!")
else:
    print("Name contains more than 10 Characters!")