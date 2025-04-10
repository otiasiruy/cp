import heapq
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = []
        n = len(arr)
        for i in range(n):
            heapq.heappush(l, (abs(arr[i] - x), i))
        ans = []
        while k > 0:
            k -= 1
            i, j = heapq.heappop(l)
            ans.append(arr[j])
        ans.sort()
        return ans