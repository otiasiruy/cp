from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        ans = [0] * 2
        n = len(grid)
        mp = [0] * (n * n + 1)
        for i in range(n):
            for j in range(n):
                mp[grid[i][j]] += 1
                if mp[grid[i][j]] == 2:
                    ans[0] = grid[i][j]
        for i in range(1, len(mp)):
            if not mp[i]:
                ans[1] = i
                break
        return ans