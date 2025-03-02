from collections import defaultdict
from typing import List


class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        ans = []
        d = defaultdict(int)
        for r in nums:
            for c in r:
                d[c] += 1
        for k, v in d.items():
            if v == len(nums):
                ans.append(k)
        ans.sort()
        return ans