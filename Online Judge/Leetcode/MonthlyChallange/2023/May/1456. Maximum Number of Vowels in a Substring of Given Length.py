# Accepted in second term.
# sliding window, two pointer

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels: int = 0
        vowels_list = list('aeiou')
        first_window = s[0:k]

        for c in first_window:
            if c in vowels_list:
                vowels += 1

        ans: int = vowels

        slow: int = 0
        fast: int = k
        while fast < len(s):
            if s[fast] in vowels_list:
                vowels += 1
            if s[slow] in vowels_list:
                vowels -= 1
            slow += 1
            fast += 1
            ans = max(ans, vowels)

        return ans
