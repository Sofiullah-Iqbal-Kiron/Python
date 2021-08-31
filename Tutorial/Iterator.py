# An iterator is an object that can traverse through all the values upon iterable from start to end.
# str, list, tuple, dict, set are all iterable objects which we can get an iterator from.
# All these objects have a iter() method which is used to get an iterator.

# There are many features available in iterator.

li_one = ['Kiron', 'Mack', 'Ultra']
new_it = iter(li_one)
for i in range(3):
    print(next(new_it))

string = 'MyName'
str_itr = iter(string)
for i in range(len(string)):
    print(next(str_itr))

# Looping through an iterator
mytuple = ('one', 'two', 'three')
for i in mytuple:
    print(i)
