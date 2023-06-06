# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.strip().split(r"\s"))


line = "Hello, my name is John"
print(line.split())
