from typing import List


class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        ans = 0
        m = max(nums)
        for i in range(k):
            ans += m
            m += 1
        return ans