from typing import List
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        if grid[0][0]:
            return -1

        n = len(grid)

        def valid(i, j):
            if 0 <= i < n and 0 <= j < n and not grid[i][j]:
                return True
            return False

        dq = deque()
        dq.append((0, 0, 1))
        dir = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        seen = {(0, 0)}

        while dq:
            neighbor = dq.popleft()

            if (neighbor[0], neighbor[1]) == (n - 1, n - 1):
                return neighbor[2]

            for x, y in dir:
                dx = x + neighbor[0]
                dy = y + neighbor[1]
                if (dx, dy) not in seen and valid(dx, dy):
                    seen.add((dx, dy))
                    dq.append((dx, dy, neighbor[2] + 1))

        return -1
