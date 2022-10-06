from pathlib import Path

# Path class can make system calls.
# Path.cwd() classmethod returns "current working directory"
print(Path.cwd())

# Path.home() returns users home directory.
print(Path.home())

myHome = Path.home()
print(myHome.samefile(Path.home()))

# Iterate over the directory.
for i in myHome.iterdir():
    print(i)

print(myHome.parent)
