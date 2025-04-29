import bisect
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        dp = []
        dp.append(nums[0])
        for i in range(1, n):
            if nums[i] > dp[len(dp) - 1]:
                dp.append(nums[i])
            elif nums[i] < dp[len(dp) - 1]:
                j = bisect.bisect_left(dp, nums[i])
                if nums[i] < dp[j]:
                    dp[j] = nums[i]
        return len(dp)