# ac

# range(), str.strip([char sequence])

# str.strip() removes all trailing and leading char that are passed as argument. If no char is defined,
# this function will auto detect a single space.
# This returns a copy of the string with the leading and trailing characters removed.
# strip() docs: https://python-reference.readthedocs.io/en/latest/docs/str/strip.html
# range(initial, end, inc/dec)

n = int(input())
s = ''
for i in range(1, n + 1):
    s += str(i)
print(s.strip())
