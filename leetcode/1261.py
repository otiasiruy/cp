from typing import Optional



class FindElements:

    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    root: Optional[TreeNode] = None

    def __init__(self, root: Optional[TreeNode]):

        def dfs(node):
            if not node:
                return
            if node.left:
                node.left.val = 2 * node.val + 1
                dfs(node.left)
            if node.right:
                node.right.val = 2 * node.val + 2
                dfs(node.right)

        FindElements.root = root
        FindElements.root.val = 0
        dfs(FindElements.root)

    def find(self, target: int) -> bool:
        def dfs(node):
            if not node or node.val > target:
                return False
            if node.val == target:
                return True
            return dfs(node.left) or dfs(node.right)

        return dfs(FindElements.root)

