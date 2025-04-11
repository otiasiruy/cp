from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        dq = deque()
        dq.append(root)
        max_sum = -10**9
        ans = 1
        level = 1
        while dq:
            n = len(dq)
            s = 0
            while n > 0:
                node = dq.popleft()
                s += node.val
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
                n -= 1
            if max_sum < s:
                max_sum = s
                ans = level
            level += 1
        return ans