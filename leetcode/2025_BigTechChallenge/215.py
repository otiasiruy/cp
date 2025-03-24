import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        l = []
        for i in nums:
            heapq.heappush(l, i * (-1))
        ans = 0
        while k > 0:
            ans = heapq.heappop(l)
            k -= 1
        return ans * (-1)