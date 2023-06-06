# Accepted.
# Pythonic issue occurs while dividing. Use "//" to solve

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        lV, rV = nums[0], sum(nums, -nums[0])
        mAD = abs(lV - rV // (n - 1))
        mI = 0

        for i in range(1, n, 1):
            lV += nums[i]
            rV -= nums[i]
            curMAD = abs(lV // (i + 1) - rV // max(1, n - i - 1))
            if curMAD < mAD:
                mAD = curMAD
                mI = i

        return mI
