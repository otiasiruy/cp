from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        i = n - 1
        while i >= 0:
            if nums[i] + i >= n - 1:
                n = i + 1
            i -= 1
        return n - 1 == 0