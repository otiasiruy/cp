"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':

        def depth(node):
            d = 0
            while node:
                d += 1
                node = node.parent
            return d

        dp = depth(p)
        dq = depth(q)

        while dp > dq:
            dp -= 1
            p = p.parent

        while dq > dp:
            dq -= 1
            q = q.parent

        while p != q:
            p = p.parent
            q = q.parent

        return p