# accepted

class Solution:
    def reverseBits(self, n: int) -> int:
        toBin = bin(n)[2:]
        toBin = '0' * (32 - len(toBin)) + toBin
        return int(toBin[::-1], 2)
