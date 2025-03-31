from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:

        def dfs(pre, node, level, is_left):
            if not node:
                return
            if not node.left and not node.right:
                level.append(node.val)
                if is_left:
                    pre.left = None
                else:
                    pre.right = None
                return
            if node.left:
                dfs(node, node.left, level, True)
            if node.right:
                dfs(node, node.right, level, False)
            return

        node = root
        ans = []
        while node and (node.left or node.right):
            level = []
            dfs(node, node, level, True)
            ans.append(level)

        ans.append([root.val])
        return ans