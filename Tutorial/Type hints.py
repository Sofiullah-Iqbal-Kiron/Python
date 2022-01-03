# https://docs.python.org/3/library/typing.html#type-aliases

# Specifying types but optional only. That's why it is called, hints.
def greet(name: str) -> list:
    return list(f"Hello {name}")


def one(relate: int) -> str:
    return 1


print(type(greet("Kiron")), end='\n')
print(type(one("No")))
