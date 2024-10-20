# Question 6: Write a program to calculate the grade of a student from his marks from the following scheme.

# 1) 90-100     Ex
# 2) 80-90      A
# 3) 70-80      B
# 4) 60-70      C
# 5) 50-60      D
# 6) < 50       F

marks = int(input("Enter Marks!"))

if (marks>=90):
    grade = 'Ex'
elif (marks>=80):
    grade = 'A'
elif (marks>=70):
    grade = 'B'
elif (marks>=60):
    grade = 'C'
elif (marks>=50):
    grade = 'D'
else:
    grade = 'F'

print("Your Grade is",grade)