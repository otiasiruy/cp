from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        ans = -1
        max_v = max(nums)
        for i in range(len(nums)):
            if nums[i] == max_v:
                ans = i
            else:
                if nums[i] * 2 > max_v:
                    return -1
        return ans