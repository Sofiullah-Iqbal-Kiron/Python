# input() function always going to give you back a str.
# int() takes anything and convert it to int and then returns.

n = input('Number: ')
n=int(n)
if n > 0:
    print('Number is positive')
elif n == 0:
    print('Number is zero')
else:
    print('Undetermined')
