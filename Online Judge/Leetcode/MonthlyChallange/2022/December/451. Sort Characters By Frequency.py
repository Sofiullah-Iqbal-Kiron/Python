# Accepted in first term.

# Issue1: https://www.freecodecamp.org/news/sort-dictionary-by-value-in-python/
# Issue2: https://docs.python.org/3/howto/sorting.html#sorting-how-to

from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        ans = ""
        for a in sorted(c, key=lambda x: c[x], reverse=True):
            for i in range(c[a]):
                ans += a

        return ans.strip()
