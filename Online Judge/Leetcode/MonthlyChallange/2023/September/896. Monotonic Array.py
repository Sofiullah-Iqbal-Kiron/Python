# Accepted in first attempt.

from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        left_increased = True
        right_increased = True
        n = len(nums)
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                left_increased = False
            if nums[n - i] > nums[n - i - 1]:
                right_increased = False

        return left_increased or right_increased
