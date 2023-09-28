from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) < 1:
            return []
        ans = list()
        a = nums[0]
        i = 0
        while i < len(nums):
            if i + 1 < len(nums) and nums[i + 1] - 1 == nums[i]:
                i += 1
            else:
                if a != nums[i]:
                    ans.append(f"{a}->{nums[i]}")
                elif a == nums[i]:
                    ans.append(f"{a}")
                if i + 1 < len(nums):
                    a = nums[i + 1]
                i += 1

        return ans
