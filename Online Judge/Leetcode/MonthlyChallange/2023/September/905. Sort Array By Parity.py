# Accepted n first attempt.

from typing import List
import numpy as np


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        lEn = len(nums)
        i, e, o = 0, 0, lEn - 1
        ans = np.array(nums)
        while i < lEn:
            if nums[i] % 2 == 0:
                ans[e] = nums[i]
                e += 1
            else:
                ans[o] = nums[i]
                o -= 1
            i += 1

        return list(ans)
