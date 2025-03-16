from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        ans = 0
        s = set(nums)
        max_value = -200
        for i in s:
            max_value = max(max_value, i)
            if i > 0:
                ans += i
        return ans if ans > 0 else max_value