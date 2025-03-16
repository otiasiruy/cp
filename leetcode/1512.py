from collections import defaultdict
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        d = defaultdict(int)
        for i in nums:
            ans += d[i]
            d[i] += 1
        return ans