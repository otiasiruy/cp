from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        n = len(graph)

        def backtrack(curr, i):

            if curr and curr[-1] == n - 1:
                ans.append(curr[:])
                return

            for a in range(len(graph[i])):
                curr.append(graph[i][a])
                backtrack(curr, graph[i][a])
                curr.pop()

        ans = []
        backtrack([0], 0)
        return ans
