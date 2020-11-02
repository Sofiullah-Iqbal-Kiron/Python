def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number


print(f"6 is {fizz_buzz(6)}, 10 is {fizz_buzz(10)}, 15 is {fizz_buzz(15)} and 7 is {fizz_buzz(7)}")
