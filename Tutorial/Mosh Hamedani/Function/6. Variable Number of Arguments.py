# It's time to create a function with variable number of arguments.

def print_all(*numbers):
    for number in numbers:
        print(number)
    print(numbers)  # Print all the objects as a tuple (tuples are noted by parenthesis).


print_all(1, 2, 3, 4, 5)
