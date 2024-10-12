# Question 2: Write a program to fill in a letter template given below with name and date.

# letter = '''Dear <|NAME|>,
#                 You are Selected!
#                 <|DATE>'''

letter = '''Dear <|NAME|>,
                You are Selected!
                <|DATE|>'''

date = input("Enter Date :)")
name = input("Enter Name :)")

letter = letter.replace("<|NAME|>",name)
letter = letter.replace("<|DATE|>",date)

print(letter)