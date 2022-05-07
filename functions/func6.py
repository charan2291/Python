def shout(text):
    return text.upper()
def out(text):
    return text.lower()
def greet(func):
    greeting=func("Hi,I am created by a passed as an argument")
    print(greeting)
greet(shout)
greet(out)
"""
OUTPUT:
HI,I AM CREATED BY A PASSED AS AN ARGUMENT
hi,i am created by a passed as an argument
