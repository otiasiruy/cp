from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])
        for i in range(2, n - 1):
            if i != n - 1:
                dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
            elif i - 2 > 0:
                if n > 0 and n % 2 != 0:
                    dp[i] = max(dp[i - 1], nums[i] + dp[i - 2] - dp[0])
                else:
                    dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
            else:
                dp[i] = max(dp[i - 1], nums[i])

        nums.reverse()
        dp2 = [0] * n
        dp2[0] = nums[0]
        dp2[1] = max(dp2[0], nums[1])
        for i in range(2, n - 1):
            if i != n - 1:
                dp2[i] = max(dp2[i - 1], nums[i] + dp2[i - 2])
            elif i - 2 > 0:
                if n > 0 and n % 2 != 0:
                    dp2[i] = max(dp2[i - 1], nums[i] + dp2[i - 2] - dp2[0])
                else:
                    dp2[i] = max(dp2[i - 1], nums[i] + dp2[i - 2])
            else:
                dp2[i] = max(dp2[i - 1], nums[i])
        return max(dp[n - 2], dp2[n - 2])