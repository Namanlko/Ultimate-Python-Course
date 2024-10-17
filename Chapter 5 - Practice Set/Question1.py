# Question 1: Write a program to create a dictionary of Hindi words with the values as their english translation. Provide user with an option to look it up!

dict = {"Kitab":"Book","Naam":"Name","Seb":"Apple","Kalam":"Pen","Suraya":"Sun"}

print("Available Word in Dictionary are:",dict.keys())
word = input("Enter Hindi Word!\n")
print("English Meaning of",word,"is",dict[word])