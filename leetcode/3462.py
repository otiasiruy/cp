import heapq
from typing import List


class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        rows = []
        pq = []
        for i in range(len(grid)):
            rows.append(grid[i])
            rows[i].sort(reverse=True)
        for i in range(len(rows)):
            for j in range(limits[i]):
                heapq.heappush(pq, -rows[i][j])
        ans = 0
        for i in range(k):
            ans += (-heapq.heappop(pq))
        return ans
