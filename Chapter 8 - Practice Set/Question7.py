# Question 7: Write a python program to remove a given word from a list and strip it at the same time.

def ReplaceAndStrip(string,word):
    newStr = string.replace(word,"")
    return newStr.strip()

str = input("Enter String :)")
word = input("Enter Word :)")
print("Formatted String:",ReplaceAndStrip(str,word))
