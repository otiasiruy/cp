from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])
        for i in range(2, n):
            if nums[i] + dp[i - 2] > dp[i - 1]:
                dp[i] = nums[i] + dp[i - 2]
            else:
                dp[i] = dp[i - 1]
        return dp[n - 1]