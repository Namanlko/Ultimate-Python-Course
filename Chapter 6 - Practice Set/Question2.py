# Question 2: Write a program to find out whether a student is pass or fail. If it requires total 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

a = int(input("Enter First Subject Marks:"))
b = int(input("Enter Second Subject Marks:"))
c = int(input("Enter Third Subject Marks:"))

if (a<33 or b<33 or c<33):
    print("Failed! You have less than 33% in one or more subjects.")
elif ((a+b+c)/3 <40):
    print("Failed! You have total aggregrate leass than 40%.")
else:
    print("Congratulations! You have passed exam with",(a+b+c)/3,"%")
