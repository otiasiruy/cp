# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import Optional, List


class TreeNode:
    pass


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        dq = deque()
        dq.append(root)
        ans = []
        while dq:
            level = deque()
            value = 0
            while dq:
                node = dq.popleft()
                value = node.val
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            dq = level.copy()
            ans.append(value)
        return ans