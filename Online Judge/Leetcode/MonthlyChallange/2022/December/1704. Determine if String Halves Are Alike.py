# Accepted.

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        i, half = 0, len(s) // 2
        j = half
        iV, jV = 0, 0
        while i < half and j < len(s):
            if s[i] in vowels:
                iV += 1
            if s[j] in vowels:
                jV += 1
            i += 1
            j += 1
        return iV == jV
