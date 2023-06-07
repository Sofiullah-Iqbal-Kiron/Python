# accepted at 4'th attempt
# bit manipulation, comparison

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        result = bin(a | b)[2:]
        max_len = len(bin(max(a, b, c))[2:])
        a, b, c, flips = bin(a)[2:], bin(b)[2:], bin(c)[2:], 0
        a, b, c, result = '0' * (max_len - len(a)) + a, '0' * (max_len - len(b)) + b, '0' * (
                max_len - len(c)) + c, '0' * (max_len - len(result)) + result

        for i in range(max_len - 1, -1, -1):
            print(i)
            r = result[i]
            bit1 = a[i]
            bit2 = b[i]
            required = c[i]
            if required == '1' and r == '0':
                flips += 1
            elif required == '0' and r == '1':
                if bit1 == '1':
                    flips += 1
                if bit2 == '1':
                    flips += 1

        return flips
