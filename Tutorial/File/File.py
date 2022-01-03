# File is in term of basic input/output: IO.

# open(file, mode='r') method returns a file as a object that most commonly used with these two arguments.
# Contents of the file returned as str.
# In-built functions, no need to import any module.
# Flags: r - read only;
# w - write only, truncating the file first;
# a - write without truncate, appends to the end of file.
# x - exclusive open, fail if file already exists.
# + - open for update, read & write.
file = open('test.txt', mode='a')

# Create a TeX file in current working directory which is not exist already.
file2 = open('test2.tex', mode='w')
file2.write('\documentclass[11pt]{' + 'article' + '}' + '\n\n' + r'\author{Sofiullah Iqbal Kiron}')

# read(size) method reads and returns all of it's contents as a str if size is omitted.
# Size is the length of the content.
# print(file.read(10), end='\n')

# Read line by line.
# print('Reading line by line:')
# print(file.readline())

# File object is iterable
# for line in file:
#     print(line, end='')

# Return lines as a list of string. This method is equivalent to list(file).
# print(file.readlines())

# Write onto the file. write() returns the number of characters written.
# print(file.write('Here is some text written from py program.\n'))

# Tell the current position of the file object in the file.
print(file.tell())

# Change the file position.

# Close the file. No longer available to read, write or modify.
file.close()

# Check that file closed or not.
print('\nFile closed: ' + str(file.closed) + '.')
