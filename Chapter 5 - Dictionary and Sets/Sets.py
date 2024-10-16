# Set is a collection of non repetitive elements. If you are a programming begineer without much knowledge of mathematical operations on sets, you can simply look at sets in Python as data types containing unique values.

sets = {1,2,3,4}
print(sets)
print(type(sets))

# Amazing Fact:
s = {} # This is Dictionary not set. So we cannot create Empty set like this.
print(type(s)) # <class 'dict'>

st = set() # This way we can create an Empty set.
print(type(st))

# Properties of Sets:
# 1) Sets are unordered. Element's order doesn't matter.
# 2) Sets are unindexed. Cannot access elements by index.
# 3) There is no way to change items in sets.
# 4) Sets cannot contain duplicate values.