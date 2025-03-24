from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans = inc = dec = 0
        n = len(nums)
        for i in range(1, n):
            if nums[i - 1] < nums[i]:
                inc += 1
                ans = max(ans, dec)
                dec = 0
            elif nums[i - 1] > nums[i]:
                dec += 1
                ans = max(ans, inc)
                inc = 0
            else:
                ans = max(ans, inc)
                ans = max(ans, dec)
                inc = dec = 0
        ans = max(ans, inc)
        ans = max(ans, dec)
        return ans + 1
