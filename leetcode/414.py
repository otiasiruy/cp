import heapq
from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        k = 3
        l = []
        s = set()
        for i in nums:
            if i not in s:
                heapq.heappush(l, i)
                s.add(i)
            if len(l) > k:
                heapq.heappop(l)
        if len(l) < 3 or len(s) < 3:
            while len(l) > 1:
                heapq.heappop(l)
            return heapq.heappop(l)
        return heapq.heappop(l)