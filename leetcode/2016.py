from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        mx = -1
        pre = nums[0]
        for j in range(1, len(nums)):
            d = nums[j] - pre
            if d > 0:
                mx = max(mx, d)
            pre = min(pre, nums[j])
        return mx