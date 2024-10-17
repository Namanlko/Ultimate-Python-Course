# Question 4: What will be the length of the following set S?

s = set()
s.add(20)
s.add(20.0)
s.add("20")

print(len(s))

# Answer: The length of set is 2 because element 20 and 20.0 are treated as identical and consider as a single element.