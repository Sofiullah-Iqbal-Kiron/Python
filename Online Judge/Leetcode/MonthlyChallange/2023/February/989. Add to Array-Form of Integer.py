# Accepted in first term but this approach is not optimized enough.

from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        toStr = ""
        for n in num:
            toStr += str(n)

        result = str(int(toStr) + k)
        toRet = []
        for s in result:
            toRet.append(int(s))

        return toRet
