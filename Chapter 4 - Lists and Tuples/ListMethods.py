# Consider the following list:
 
l1 = [1,8,7,2,21,15]

for i in l1:
    print(i,end=" ")
print()

# 1) Sort Function: It is used to short the given list.
l1.sort()
print(l1)

# 2) Reverse Function: It is used to short the given list.
l1.reverse()
print(l1)

# 3) Append Function: It is used to add an element to the end of given list.
l1.append(56)
print(l1)

# 4) Insert Function: It is used to insert an element to a given index in the given list.
l1.insert(3,45)
print(l1)

# 5) Pop Function: It is used to delete the given element from the list and return its value.
print(l1.pop(2))
print(l1)

# 6) Remove Function: It is used to remove the given element from the list.
l1.remove(45)
print(l1)