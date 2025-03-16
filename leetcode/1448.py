from collections import defaultdict
from typing import List


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        d = defaultdict(int)
        delete = set()
        for i in nums:
            d[i] += 1
        for k, v in d.items():
            if v > 1:
                delete.add(k)
        for i in delete:
            del d[i]
        return sum(d)