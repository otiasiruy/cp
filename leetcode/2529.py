from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        p = n = 0
        for i in nums:
            if i > 0:
                p += 1
            elif i < 0:
                n += 1
        return p if p >= n else n