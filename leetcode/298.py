from collections import deque
from typing import Optional


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        dq = deque()
        dq.append((root, 1))
        ans = 1
        while dq:
            node, seq = dq.popleft()
            if node.left:
                if node.left.val - node.val == 1:
                    ans = max(ans, seq + 1)
                    dq.append((node.left, seq + 1))
                else:
                    dq.append((node.left, 1))
            if node.right:
                if node.right.val - node.val == 1:
                    ans = max(ans, seq + 1)
                    dq.append((node.right, seq + 1))
                else:
                    dq.append((node.right, 1))
        return ans