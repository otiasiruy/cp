from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        def valid(x, y):
            if 0 <= x < m and 0 <= y < n:
                return True
            return False

        def bfs():
            nonlocal ans
            nonlocal queue
            nonlocal seen

            while queue:
                r, c, dist = queue.popleft()

                for i, j in dir:
                    dx = r + i
                    dy = c + j
                    if valid(dx, dy) and (dx, dy) not in seen:
                        seen.add((dx, dy))
                        queue.append((dx, dy, dist + 1))
                        ans[dx][dy] = dist + 1

        m = len(mat)
        n = len(mat[0])
        ans = [[0] * n for _ in range(m)]
        dir = [(1,0), (-1,0), (0,1), (0,-1)]
        seen = set()
        queue = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j, 0))
                    seen.add((i, j))

        bfs()

        return ans