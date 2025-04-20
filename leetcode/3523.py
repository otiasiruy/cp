from typing import List


class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        ans = []
        n = len(nums)
        min_v = nums[0]
        for i in range(n):
            if nums[i] >= min_v:
                ans.append(nums[i])
                if nums[i] > min_v:
                    min_v = nums[i]
        return len(ans)