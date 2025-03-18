from typing import Optional


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        length = 0
        def dfs(node):
            if not node:
                return 0
            nonlocal length
            l = dfs(node.left)
            r = dfs(node.right)
            length = max(length, r + l)
            return max(l, r) + 1
        dfs(root)
        return length