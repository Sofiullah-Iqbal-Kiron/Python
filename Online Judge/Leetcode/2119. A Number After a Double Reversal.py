# accepted

class Solution:
    def reverse_num(self, num: int) -> int:
        ans = 0
        while num > 0:
            digit = num % 10
            ans = ans * 10 + digit
            num //= 10
        return ans

    def isSameAfterReversals(self, num: int) -> bool:
        rev1 = self.reverse_num(num)
        rev2 = self.reverse_num(rev1)
        return rev2 == num
