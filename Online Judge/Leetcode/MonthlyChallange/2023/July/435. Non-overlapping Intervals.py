# Accepted.
# Learn interval scheduling problem.

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        ans = 0
        i, j = 0, 1
        while j < len(intervals):
            if intervals[i][1] > intervals[j][0]:
                ans += 1
                j += 1
            else:
                i = j
                j += 1

        return ans
