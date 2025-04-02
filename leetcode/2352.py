from collections import defaultdict
from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        r = defaultdict(int)
        c = defaultdict(int)
        n = len(grid)
        for i in grid:
            row = []
            for j in i:
                if j < 10:
                    row.append('0' + str(j))
                else:
                    row.append(str(j))

            num = ''.join(row)
            r[num] += 1

        for j in range(n):
            col = []
            for i in range(n):
                if grid[i][j] < 10:
                    col.append('0' + str(grid[i][j]))
                else:
                    col.append(str(grid[i][j]))
            num = ''.join(col)
            c[num] += 1

        ans = 0
        for k, v in r.items():
            if k in c:
                ans += c[k] * v
        return ans
