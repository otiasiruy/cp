import heapq
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l = []
        for r in matrix:
            for c in r:
                heapq.heappush(l, c)
        ans = 0
        while l and k > 0:
            ans = heapq.heappop(l)
            k -= 1
        return ans