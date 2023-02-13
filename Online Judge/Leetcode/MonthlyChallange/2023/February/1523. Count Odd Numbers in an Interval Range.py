# Accepted in first term.
# Ubuntu pastebin: https://pastebin.ubuntu.com/p/D5yVs6TPgV/

class Solution:
    @classmethod
    def upodd(cls, num: int):
        if num % 2 == 0:
            return num + 1

        return num

    @classmethod
    def downodd(cls, num: int):
        if num % 2 == 0:
            return num - 1

        return num

    def countOdds(self, low: int, high: int) -> int:
        return int((Solution.downodd(high) - Solution.upodd(low)) // 2 + 1)
