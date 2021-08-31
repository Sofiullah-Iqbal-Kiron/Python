# Python's for statement iterates over the items of any sequence in order that they appear in the sequence.
# for, for...else, break, continue, pass
# for...else: else block under of for. It will execute when for block finises it's execution properly
# but break statement prevents this.
# pass: used to create an empty block of any control flow like, if, else, for, while and also def.

words = ['cat', 'window', 'book', 'master', 'varsity']
for word in words:
    print(f'{word}: {len(word)}')
