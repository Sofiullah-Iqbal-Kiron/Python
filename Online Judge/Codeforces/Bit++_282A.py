# Accepted in first term.
# Ubuntu pastebin: https://pastebin.ubuntu.com/p/9PwPwQhKts/
# First problem that is solved using Python in Codeforces.

import re

x: int = 0;

i: int = int(input())

for idx in range(i):
    line: str = input().strip()
    if re.match("X\+\+|\+\+X", line):
        x += 1
    else:
        x -= 1
print(x)
