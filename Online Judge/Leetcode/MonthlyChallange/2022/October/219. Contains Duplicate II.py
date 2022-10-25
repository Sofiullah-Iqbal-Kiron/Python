# Helper code: https://leetcode.com/problems/contains-duplicate-ii/discuss/2727273/Python-3-oror-5-lines-dict-w-example-oror-TM%3A-9576
# Accepted in second term.
# Posted in twitter.
# Ubuntu pastebin: https://pastebin.ubuntu.com/p/Yr7cWMXRkg/

from collections import defaultdict


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        myD = defaultdict(int)
        for i, num in enumerate(nums):
            if num in myD and i - myD[num] <= k:
                return True
            myD[num] = i

        return False
