# Accepted in 2nd attempt.
# Time: O(n^3) mostly.
# Space: O(1).
# Ubuntu pastebin: https://pastebin.ubuntu.com/p/RhMMPpzBw3/

class Solution(object):
    def unequalTriplets(self, nums):
        ans = 0
        for i in range(0, len(nums), 1):
            for j in range(i + 1, len(nums), 1):
                if nums[i] != nums[j]:
                    for k in range(j + 1, len(nums), 1):
                        if nums[k] != nums[j] and nums[k] != nums[i]:
                            ans += 1
        return ans
