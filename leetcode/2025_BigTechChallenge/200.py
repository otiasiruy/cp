from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def valid(x, y):
            if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
                return True
            return False

        def dfs(x,y):
            if not valid(x,y) or (x,y) in seen:
                return
            seen.add((x, y))
            for i, j in dir:
                dfs(x + i, y + j)

        dir = [(1,0), (-1,0), (0,1), (0,-1)]
        m = len(grid)
        n = len(grid[0])
        seen = set()
        ans = 0
        for i in range(m):
            for j in range(n):
                if (i,j) not in seen and valid(i,j):
                    ans += 1
                    dfs(i,j)
        return ans