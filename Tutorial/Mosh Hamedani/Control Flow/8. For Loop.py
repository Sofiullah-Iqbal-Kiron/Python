for number in range(3):  # range(n): built-in function.
    print(f"Attempt {number + 1} time", (number + 1) * ".")  # The loop runs 0 to n-1 times.

for number in range(1, 4):
    print("Attempt.", number)

for number in range(1, 11, 2):  # range(start, end, step: increment)
    print(number)

for number in range(11, 1, -2):  # range(start, end, step: decrement)
    print(number)

successful = True
for number in range(1, 4):
    print("Attempt")
    if successful:
        print("Successful")
        break
