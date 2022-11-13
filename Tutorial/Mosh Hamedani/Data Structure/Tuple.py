# 4 built-in data types in python: list, tuple, set, dict.
# Tuples are immutable/unchangeable and ordered.
# Items placed inside a set of parenthesis or not but must be separated by comma.
# Allow duplicates.
# Can hold any type of data/object.
# We can pack/unpack tuple items as list items.

tup1 = (1, 2, 3)
tup2 = 'a', 'b', 'c'
print(type(tup1))
print(tup2[-1])

# A tuple containing single item, put a comma after item, it's must.
tup3 = 'One',  # comma indicating that this is a tuple.
tup4str = ('One')  # but that's not tuple, there is no comma delimiter exist.
print(type(tup3), type(tup4str))

# combined tuple
tup5 = 1, 'R', True
print(tup5)

# unpack tup5
intex, strex, boolex = tup5
print(intex, strex, boolex)

# join tuples by + operator
tup6 = tup3 + tup5
print(tup6)

# make a tuple from a list by tuple(iterable)
my_tuple = tuple([1, 2, 3])
print(my_tuple)

# repeat value in a tuple
tup7 = ('a',) * 10  # don't forget parenthesis.
print(tup7)
print(tup7.count('a'))
print(tup7.index('a'))
