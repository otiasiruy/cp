from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def bs(x):
            l = 0
            r = len(dp)
            while l <= r:
                mid = l + (r - l) // 2
                if x == dp[mid]:
                    return mid
                elif dp[mid] < x:
                    l = mid + 1
                else:
                    r = mid - 1
            return l

        n = len(nums)
        if n == 1:
            return 1
        dp = [nums[0]]
        for i in range(1, n):
            if nums[i] > dp[len(dp) - 1]:
                dp.append(nums[i])
            elif nums[i] < dp[len(dp) - 1]:
                j = bs(nums[i])
                if nums[i] < dp[j]:
                    dp[j] = nums[i]
        return len(dp)