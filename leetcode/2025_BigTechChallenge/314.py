from collections import defaultdict, deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        dq = deque()
        dq.append((root, 0))
        nodes = []
        col = 0
        set_cols = set()
        while dq:
            node, col = dq.popleft()
            nodes.append((col, node.val))
            set_cols.add(col)
            if node.left:
                dq.append((node.left, col - 1))
            if node.right:
                dq.append((node.right, col + 1))

        ans = []
        d = defaultdict(list)
        sorted_cols =[]

        for i in set_cols:
            sorted_cols.append(i)

        sorted_cols.sort()

        for col, v in nodes:
            d[col].append(v)

        for i in sorted_cols:
            ans.append(d[i])

        return ans