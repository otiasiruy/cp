# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        graph = defaultdict(list)

        def dfs(node):
            if not node:
                return
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                dfs(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                dfs(node.right)

        dfs(root)
        seen = {target.val}
        queue = deque()
        queue.append((target.val, 0))
        ans = []
        while queue:
            node, level = queue.popleft()
            if (level == k):
                ans.append(node)
            for next_node in graph[node]:
                if next_node not in seen:
                    seen.add(next_node)
                    queue.append((next_node, level + 1))
        return ans