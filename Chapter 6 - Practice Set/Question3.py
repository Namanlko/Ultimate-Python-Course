# Question 3: A spam comment is defined as a text containing following keywords. 
# 1) "make a lot of money"
# 2) "buy now"
# 3) "subscribe this"
# 4) "click this"

comment = input("Please Enter Your Comment!")

if ("make a lot of money" in comment):
    spam = True
elif ("buy now" in comment):
    spam = True
elif ("subscribe this" in comment):
    spam = True
elif ("click this" in comment):
    spam = True
else:
    spam = False

if (spam):
    print("This is Spam!")
else:
    print("This is not a Spam!")