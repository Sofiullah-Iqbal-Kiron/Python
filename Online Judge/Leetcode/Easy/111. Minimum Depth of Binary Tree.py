# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    ans = 10 ** 5 + 1
    stack = list()
    traversed = set()

    def dfs(self, root):
        if root not in self.traversed:
            self.stack.append(root)
            if root.left is not None:
                self.dfs(root.left)
            if root.right is not None:
                self.dfs(root.right)
            self.ans = min(self.ans, len(self.stack))
            self.traversed.add(self.stack.pop())
        return

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self.dfs(root)
        return self.ans
