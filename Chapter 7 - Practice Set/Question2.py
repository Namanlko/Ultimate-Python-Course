# Question 2: Write a program to greet all the person names stored in a list l1 and which starts with S.

l1 = ["Angela", "Soham", "Sachin", "John", "Sam"]

for i in l1:
    if(i.startswith('S')):
        print("Hello",i)