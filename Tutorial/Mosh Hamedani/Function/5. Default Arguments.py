# All the parameters are essential by default.
# Let's make parameter optional.

def increment(value, by=1):  # Default parameters must stay after required parameters.
    return value + by


print(increment(value=2))
print(increment(value=3, by=1))
print(increment(by=3, value=4))
