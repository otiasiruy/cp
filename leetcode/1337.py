import heapq
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        l = []
        for r in range(len(mat)):
            heapq.heappush(l, (sum(mat[r]), r))
        ans = []
        while k > 0:
            s, i = heapq.heappop(l)
            ans.append(i)
            k -= 1
        return ans