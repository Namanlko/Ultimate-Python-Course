# Sets Methods: Consider the following set:

s = {1,8,2,3}

# 1) Len Function: It is used to return the length (Number of elements present) of a set.
print(len(s))


# 2) Remove Function: It is used to remove the given element from the set.
s.remove(8) # Remove 8 from the set.
print(s)

# 3) Pop Function: It is used to remove a random element from the set and also return that element.
print(s.pop())
print(s)

# 4) Clear Function: It is used to remove all the element of a set. We can say it use to empty set.
s.clear()
print(s)

s1 = {1,2,3,4,5,6}
s2 = {5,6,7,8,9,10}

# 5) Union Function: It is used to return the union of two sets.
print(s1.union(s2))

# 6) Intersection Function: It is used to return the intersection of two sets.
print(s1.intersection(s2))