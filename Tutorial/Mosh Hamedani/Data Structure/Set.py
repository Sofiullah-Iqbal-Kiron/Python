# Set is one of the built-in data structure in python that doesn't support duplicates.
# Set implements general mathematical set's concept.
# Unordered linear DS, so that we can not access items by index.
# Set items placed in between a set of curly braces.
# To access set items, convert it to a list.
# Can add items by append() but can not change.
# Set is immutable.
# Can iterate over set by for loop.
# Don't implement stack by using set cause set is unordered.
# pop() will remove last item from the set but we will not know what item gets removed.

# Making a set from a list
values = [1, 2, 3, 4, 5, 1, 2, 1]
set1 = set(values)
print(set1)

# Define a set by putting items inside curly brace.
# set will keep only first occurrence of a item.
set2 = {'a', 'a', 'c', 'd', 'b'}
print(set2)

# Add item set_name.add(item)
set2.add('new item by add()')
print(set2)

# set_name.update(iterable)
list1 = [1, 2, 3, 4]
set2.update(list1)
print(set2)

# clear(): empty the set
set2.clear()
print(set2)
