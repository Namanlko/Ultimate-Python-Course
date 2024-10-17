# Question 6: Create an empty dictionary. Allow 4 friends to enter their favourite programming language as values and use keys as their names. Assume that the names are unique.

language = {}

a = input("Enter Your Favourite Programming Language Angela Yu: ")
b = input("Enter Your Favourite Programming Language John Purshall Yu: ")
c = input("Enter Your Favourite Programming Language Sam Pearson: ")
d = input("Enter Your Favourite Programming Language Hal Erld: ")

language["Angela Yu"] = a
language["John Purshall"] = b
language["Sam Pearson"] = c
language["Hal Erld"] = d

print(language)