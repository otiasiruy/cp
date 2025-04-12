import heapq
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        l = []
        for key, v in c.items():
            heapq.heappush(l, (v * (-1), key))
        ans = []
        while k > 0 and l:
            k -= 1
            s, key = heapq.heappop(l)
            ans.append(key)
        return ans