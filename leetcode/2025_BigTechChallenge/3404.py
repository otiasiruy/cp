from bisect import bisect_right
from collections import defaultdict
from typing import List


class Solution:
    def numberOfSubsequences(self, nums: List[int]) -> int:
        n = len(nums)
        pq = defaultdict(list)
        for p in range(n - 6):
            for q in range(p + 2, n - 4):
                ratio = nums[p] / nums[q]
                pq[ratio].append(q)

        for ratio in pq:
            pq[ratio].sort()

        ans = 0
        for r in range(4, n - 2):
            for s in range(r + 2, n):
                ratio = nums[s] / nums[r]
                if ratio in pq:
                    pos = bisect_right(pq[ratio], r - 2)
                    ans += pos
        return ans