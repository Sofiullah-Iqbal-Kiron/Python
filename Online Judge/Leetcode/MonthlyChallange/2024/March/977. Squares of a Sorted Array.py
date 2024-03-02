# Accepted in first attempt.

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans: List = list()
        start: int = 0
        end: int = len(nums) - 1
        while (start <= end):
            if abs(nums[start]) > abs(nums[end]):
                ans.insert(0, nums[start] ** 2)
                start += 1
            else:
                ans.insert(0, nums[end] ** 2)
                end -= 1

        return ans
