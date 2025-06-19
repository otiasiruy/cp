from typing import List


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        mn = nums[0]
        cnt = 1
        for i in range(1, n):
            if nums[i] - mn > k:
                mn = nums[i]
                cnt += 1
        return cnt