from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        values = []

        def DFS(node):
            if node is None:
                return
            values.append(node.val)
            DFS(node.left)
            DFS(node.right)

        DFS(root)
        values.sort()
        ans = 1e9
        for i in range(1, len(values), 1):
            ans = min(ans, values[i] - values[i - 1])
        return ans
