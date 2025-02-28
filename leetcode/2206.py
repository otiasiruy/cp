from collections import Counter
from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        c = Counter(nums)
        pairs = 0
        for i in c.values():
            if i % 2 != 0:
                return False
        return True