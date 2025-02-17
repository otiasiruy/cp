from typing import Optional


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
from collections import deque


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:

        queue = deque()
        queue.append(root)
        levels = []

        while queue:

            nodes = []
            while queue:
                nodes.append(queue.popleft())

            sum = 0

            for node in nodes:
                sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            levels.append(sum)

        if len(levels) < k:
            return -1

        levels.sort(reverse=True)

        return levels[k - 1]
