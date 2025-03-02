from collections import defaultdict
from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        d[0] = 1
        ans = 0
        pfsum = 0
        for i in nums:
            pfsum += i % 2
            if pfsum - k in d:
                ans += d[pfsum - k]
            d[pfsum] += 1
        return ans