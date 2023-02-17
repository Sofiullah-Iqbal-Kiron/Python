# Accepted in first term.
# __init__ or constructor in python is important, learn more about it
# taken help from: https://leetcode.com/problems/minimum-distance-between-bst-nodes/solutions/3195252/inorder-traversal-easy-explanation-video-java-c-python/

import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.values = []

    def inOrder(self, root: TreeNode) -> None:
        if root is None:
            return

        self.inOrder(root.left)
        self.values.append(root.val)
        self.inOrder(root.right)

    def minDiffInBST(self, root: TreeNode) -> int:
        self.inOrder(root)

        ans = math.inf

        for i in range(0, len(self.values) - 1, 1):
            ans = min(ans, self.values[i + 1] - self.values[i])

        return ans
