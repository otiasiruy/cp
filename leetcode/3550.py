from typing import List


class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            s = str(nums[i])
            ps = 0
            for j in s:
                ps += int(j)
            if ps == i:
                return i
        return -1