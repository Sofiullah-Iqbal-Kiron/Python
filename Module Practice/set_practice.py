# https://docs.python.org/3/library/stdtypes.html#set

# set is an iterable
# unordered collection
# no duplicates
# use set() to create empty set, {} will create empty dict
# basic usage includes membership testing and eliminating duplicate entries

a = set('nirob')
b = set('kiron')

a ^ b  # a or b but not both, symmetric difference
a.intersection_update(b)
