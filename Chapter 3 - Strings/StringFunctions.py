# String Functions: Some of the most commonly used functions to perform operations on or manipulate strings are.

str = "Angela Yu"

# 1) Len() Function: This function returns the length of the String.
print(len(str))

# 2) str.endswith(String) Function: This function tells whether the variable string ends with the mentioned string or not. If the variable string ends with same metioned string it will return true otherwise it will return false.
print(str.endswith("Yu"))

# 3) str.count(Character) Function: This function returns the total number of occurance of any character.
print(str.count('a'))

# 4) str.capitalize() Function: This function capitalizes the first character of a given string.
print(str.capitalize())

# 5) str.find(word) Function: This function finds a word and returns the index of first occurence of that word in the string.
print(str.find("Yu"))

# 6) str.replace(OldWord ,NewWord) Function: This function replaces the oldword with newword in the entire string.
print(str.replace("Yu","Yo"))