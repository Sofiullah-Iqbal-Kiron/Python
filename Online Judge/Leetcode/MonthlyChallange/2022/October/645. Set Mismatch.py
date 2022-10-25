class Solution:
    # Official solution.
    def findErrorNums(self, nums):
        n = len(nums)
        dup, miss = -1, -1
        for i in range(1, n + 1, 1):
            count = 0
            for j in range(0, n, 1):
                if (nums[j] == i):
                    count += 1
            if count == 2:
                dup = i
            elif count == 0:
                miss = i
        return [dup, miss]

    # https://leetcode.com/problems/set-mismatch/discuss/2733774/Python-3-oror-3-lines-sets-oror-TM%3A-9744
    def findErrorNums2(self, nums):
        n, a, b = len(nums), sum(nums), sum(set(nums))
        s = (n * n + 1) // 2
        return [a - b, s - b]

    # Bit manipulation.
    def findErrorNums3(self):
        pass

