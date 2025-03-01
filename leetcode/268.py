from collections import Counter
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        m = Counter(nums)
        n = len(nums)
        for i in range(n + 1):
            if m[i] == 0:
                return i
        return -1