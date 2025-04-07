from typing import List


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        if n % 2 != 0:
            ans = sum(nums) - min(nums)
        else:
            min_pair = 10**6
            for i in range(1, n):
                s = nums[i] + nums[i - 1]
                if min_pair > s:
                    min_pair = s
            ans = sum(nums) - min_pair
        return ans