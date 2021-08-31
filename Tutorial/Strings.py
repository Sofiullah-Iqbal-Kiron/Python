# Strings in python is very handy to control and manipulate. They are immutable.
# Assigned into single/double/triple quote.
# Strings are:
# 1. instance of str class.
# 2. Immutable list of bytes(8 bit packet) representing unicode character.
# Make multiline string with triple quote.
# Can use escape sequence \n, \t
# Substring string_name[start: end]

course = 'Python For Beginners'
multiline = '''Sofiullah Iqbal Kiron
BSMRSTU, SHIICT, CSE 18-19
'''
multiline2 = 'Sofiullah Iqbal Kiron\n\tBSMRSTU, SHIICT, CSE 18-19'
unicodeK = '\u004B'
print(f'Printing K with unicode: {unicodeK}')

print(multiline)
print(f'Multiline 2:\n{multiline2}')
print(course[3:-1])

# len() is a general purpose function, Not string class method.
print(f'Length of the string course by general purpose function len(): {len(course)}')

# Strings are like arrays of character (in C), access by square bracketed index(0 based index).
print(f'Third character: {course[2]}')

# String class methods: count(), find(), startswith(), endswith(), isalpha(), isdecimal(), isdigit()
# strip(), upper(), lower(), replace(),  etc.
# Reference: https://www.w3schools.com/python/python_strings_methods.asp
print(f"Number of 'n': {course.count('n')}")
print(f"First index of 'o': {course.find('o')}")  # Case-sensitive
print(f"Starts with 'Jy': {course.startswith('Jy')}")
print(f"Ends with 'ers': {course.endswith('ers')}")
