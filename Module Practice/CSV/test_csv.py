# A set is typically something with a bunch of values that has duplicated filtered out.

import csv

names = set()

with open("ictob.csv", "r") as file:
    reader = csv.DictReader(file)
    print("Printing names only: ")
    for row in reader:
        name = row["Name"].strip().upper()
        if not name in names:
            names.add(name)

# sorted(iterable) gives a sequence that is sorted already.
for name in sorted(names):
    print(name)
