# https://www.geeksforgeeks.org/decorators-in-python/
# Functions in python can be treated as a object.
# We can store this object inside another variable.
# Can pass function to another function.
# Just assume giving alias name to a function.

def greet(name):
    return f'Hello {name}'

def upper(greet,name):
    print(greet(name).upper)
    

upper(greet())