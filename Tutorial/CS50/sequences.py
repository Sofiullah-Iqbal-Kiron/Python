# str in python most like char array in C
# Counting starts from 0 and ends at (length - 1).

name = "Kiron"
print(name[0])

# All data is represented as a object in python. 3 is a object of <int> class.
# Define list(dynamic array like vector in C++ or ArrayList in Java) with square bracket.
# List can store any type of data. There is no data-type limitation to store data in a list.
# To gather type of a data in list, just use this general-purpose function, type(data) then it will return
# a string that describes the data type.
# Lists are mutable.
# Zero indexed system exist in python.
# List supports duplicate.
# Get length: len(list_name)
# Append data: list_name.append(data)
# Insert: list_name.insert(index, data)
# Append multiple values at a time: list_name.extend(value1, value2, value3)
# Lists can multi-dimensional(list of lists) as 2D or 3D array in C/C++/Java.
# Negative indexing means start from the end.
# -1 is first negative index that indicates last(len-1'th) element of the list.

mixed_list = ['Kiron', 'A', 21, 21, 12.98, True, None]
print(type(mixed_list[0]))
print(type(mixed_list[1]))  # There is no char type in python, that's why it will return 'str'
print(type(mixed_list[2]))
print(type(mixed_list[3]))
print(type(mixed_list[4]))
print(type(mixed_list[5]))
print(type(mixed_list[6]))
print(f'List before insert: {mixed_list}')
mixed_list.insert(2, 'InsertedValueAtIndex2')
print(f'List after insertion: {mixed_list}')
print(f'Length of mixed list: {len(mixed_list)}.')

# A multi-dimensional list:
TwoD_list = [[1, 2], ['kiron', 'nirob'], [True, False]]
print(TwoD_list[1][0])
print(TwoD_list[-1][0])