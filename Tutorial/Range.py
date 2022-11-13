# Reference: https://docs.python.org/3/library/stdtypes.html#ranges
# range() returns an immutable sequence.
# range(stop), range(start, stop), range(start, stop, step)
# By default, start is 0, stop is (passed_value - 1), step is 1.
# If step is zero, ValueError is raised.

r = list(range(10))
print(r)