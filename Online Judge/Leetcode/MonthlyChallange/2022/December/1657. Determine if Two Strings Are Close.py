# Accepted in 3'rd term.
# Solved but submitted after the valid time duration.

from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)

        return sorted(c1.values()) == sorted(c2.values()) and sorted(c1) == sorted(c2)
