# Question 1: Write a program to store seven fruits in a list enetered by the user.

f1 = input("Enter 1st Fruit :)")
f2 = input("Enter 2nd Fruit :)")
f3 = input("Enter 3rd Fruit :)")
f4 = input("Enter 4th Fruit :)")
f5 = input("Enter 5th Fruit :)")
f6 = input("Enter 6th Fruit :)")
f7 = input("Enter 7th Fruit :)")

fruits = [f1,f2,f3,f4,f5,f6,f7]
print(fruits)

for i in fruits:
    print(i,end=" ")