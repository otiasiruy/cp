from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        c = defaultdict(int)
        c[0] = 1
        n = len(nums)
        ans = 0
        pfsum = 0
        for i in range(n):
            pfsum += nums[i]
            if (pfsum - k) in c:
                ans += c[pfsum - k]
            c[pfsum] += 1
        return ans