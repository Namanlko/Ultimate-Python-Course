# Dictionary Methods: Consider the following dictionary.

dict = {
    "name": "Angela Yu",
    "From": "Germany",
    "Marks": [92,98,96]
}

# 1) Items Function: It is used to return all the key-value pairs in form of tuple of dictionary.
for item in dict.items():
    print(item)


# 2) Key Function: It is used to return a list containing dictionary's keys.
for key in dict.keys():
    print(key)

# 3) Update Function: It is used to update a value in dictionary corresponding to a key.
dict.update({"From":"India"})
print(dict)

# 4) Get Function: It is used to return the value of specified key.
marks = dict.get("Marks")
print("Marks are",marks)

# Note: More methods are available on docs.python.org.