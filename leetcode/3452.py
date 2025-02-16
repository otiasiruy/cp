from typing import List


class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        good = []
        n = len(nums)
        for i in range(n):
            if i - k >= 0 and i + k < n and nums[i] > nums[i - k] and nums[i] > nums[i + k]:
                good.append(nums[i])
            elif i - k >= 0 and i + k >= n and nums[i] > nums[i - k]:
                good.append(nums[i])
            elif i - k < 0 and i + k < n and nums[i] > nums[i + k]:
                good.append(nums[i])
        ans = 0
        for v in good:
            ans += v
        return ans