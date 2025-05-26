from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def valid(x, y):
            if (x,y) not in seen and 0 <= x < rows and 0 <= y < cols and grid[x][y] == 1:
                return True
            return False

        e = fr = rot = 0
        dq = deque()
        seen = set()
        rows = len(grid)
        cols = len(grid[0])
        dir = [(1,0), (0,1), (-1,0), (0,-1)]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    e += 1
                elif grid[i][j] == 1:
                    fr += 1
                else:
                    rot += 1
                    dq.append((i,j))
        mn = 0
        while dq:
            l = []
            while dq:
                i, j = dq.popleft()
                l.append((i,j))

            for i, j in l:
                if (i,j) not in seen:
                    seen.add((i,j))
                    for r, l in dir:
                        dx = i + r
                        dy = j + l
                        if valid(dx, dy):
                            dq.append((dx,dy))
                            grid[dx][dy] = 2
                            fr -= 1
            mn += 1
        return max(mn - 1, 0) if fr == 0 else -1