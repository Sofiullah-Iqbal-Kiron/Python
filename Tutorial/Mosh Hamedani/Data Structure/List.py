# Default implementation of dynamic array.
# Slow downs. Use numpy.array instead.
# Elements are in square bracket.
# Access by [index]. 0 based index. As like array in C/C++/Java.
# List can contain all type of value: [int, float, 'str', bool] -> [1, 9.3, 'Me', True]
# Combine/merge/join/concatenate lists: list_final = list_one + list_two
# Lists are mutable.
# Front indexing [0, 1, 2] is same as [-3, -2, -1] back indexing.
# list_name[start:end]

# List of str
names = ['Kiron', 'Nirob', 'Max', 'Tupa']

# List of list of int
matrix = [[1, 2], [2, 6], [7, 0]]

print(names[3])
print(matrix[1][1])

all_type = [1, 9.3, 'Me', True]
for i in all_type:
    print(type(i))

# Repeat items in a list
zeros = [0] * 10
print(zeros)

# Combined list
list_one = [1, 2, 3]
list_two = [4.3, 2.5, 1.1]
list_final = list_one + list_two
print(f'Combined list: {list_final}')

# Create list by giving iterable value
number_till_20 = list(range(20))
print(number_till_20)

# [start:end]
new_list = [1, False, 'Name', 0, 4.0]
print(new_list[1:3])

# [::step]
print(new_list[::-1])

# List unpacking
# pack-unpack method in a list
# Number of items in the list should be equal number of unpack variables.
list_three = [1, True, 0.3]
a, b, c = list_three
print('Unpacked data: ', end='')
print(a, b, c)

list_four = [1, 2, 3, 4, 4, 4, 4]
one, two, three, *fours = list_four
print(fours)

# iterate and enumerate
# built-in enumerate(iterable) will give us a set of tuple holding (index, value) pair.
list_five = ['a', 'b', 'c']
for letter in enumerate(list_five):
    print(letter[0], letter[1])

# we can unpack tuple as well as list
for index, letter in enumerate(list_five):
    print(index, letter)
