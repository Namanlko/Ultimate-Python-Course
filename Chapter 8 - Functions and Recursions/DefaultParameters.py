# Default Parameter in Function: We can have a value as default argument in a function. If we specify name="Stranger" in the line containing def, this value is used when no argument is passed.

def Greet(name="Unknown"):
    gr = "Hello, "+name
    return gr

a = Greet()
print(a)

b = Greet("Angela Yu")
print(b)