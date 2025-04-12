import heapq
from math import sqrt
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        l = []
        for point in points:
            heapq.heappush(l, (sqrt(pow(point[0], 2) + pow(point[1], 2)), point))
        ans = []
        while k > 0:
            d, point = heapq.heappop(l)
            ans.append(point)
            k -= 1
        return ans