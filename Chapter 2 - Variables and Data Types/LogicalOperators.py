# Logical Operators: Logical operator in python works on some condition and based on that condtion return answers in boolean (True or False)

# 1) Logical AND:
# Logical AND return True if both the conditions are Ture otherwise it return False.

a = 10
b = 9
c = 7

Result1 = (a>b) and (b>c)
print("Result is", Result1)

# 2) Logical OR:
# Logical OR return True if one of the condition is True and if both the condtions are False it will return False.

a = 10
b = 9
c = 7

Result2 = (a>b) or (b>c)
print("Result is", Result2)

# 3) Logical NOT:
# Logical NOT return True if the condtion is False and vice-versa.

flag = False
print("Result is", not flag)