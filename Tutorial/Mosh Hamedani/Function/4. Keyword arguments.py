# Keep keyword argument after positional argument, must.

def increment(value, by):
    return value + by


print(increment(by=5,
                value=1))  # "by=2": this is a keyword argument. Now, we can read this code like almost plain english.
