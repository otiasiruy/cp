import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)
        l = []
        for i in stones:
            heapq.heappush(l, i * (-1))
        while len(l) > 1:
            y = heapq.heappop(l)
            x = heapq.heappop(l)
            if y < x:
                heapq.heappush(l , y - x)
        return 0 if len(l) == 0 else l[0] * (-1)