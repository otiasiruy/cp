from collections import deque
from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        m = len(maze)
        n = len(maze[0])

        if m == 1 and n <= 1:
            return - 1

        def valid(x, y):
            if 0 <= x < m and 0 <= y < n and maze[x][y] == '.' and (x, y) not in seen:
                return True
            return False

        def exit(x, y):
            if (x, y) != (entrance[0], entrance[1]) and ((x == 0 or x == m - 1) or (y == 0 or y == n - 1)):
                return True
            return False

        dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        seen = {(entrance[0], entrance[1])}
        queue = deque([(entrance[0], entrance[1], 0)])

        while queue:
            x, y, step = queue.popleft()
            if exit(x, y):
                return step
            for i, j in dir:
                dx = x + i
                dy = y + j
                if valid(dx, dy):
                    seen.add((dx, dy))
                    queue.append((dx, dy, step + 1))
        return -1