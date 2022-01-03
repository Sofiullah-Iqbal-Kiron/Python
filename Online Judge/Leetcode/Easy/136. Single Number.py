# ac.
# Python: 108 milisec, 15.9 MB
# Java: 1 milisec, 39 MB
# C++: 16 milisec, 16.8 MB (It would vary.)

# XOR operation of any number with 0 returns the number itself.
# XOR of any numbers appearing even times, returns 0.
# a ^ b ^ b ^ c ^ c = a

class Solution(object):
    def singleNumber(self, nums):
        ans = nums[0]
        for i in range(1, len(nums), 1):
            ans ^= nums[i]
        return ans
