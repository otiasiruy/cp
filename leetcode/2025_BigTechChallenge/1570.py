from collections import defaultdict
from typing import List


class SparseVector:
    def __init__(self, nums: List[int]):
        self.sp = defaultdict(int)
        for i in range(len(nums)):
            if nums[i] != 0:
                self.sp[i] = nums[i]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ans = 0
        for k, v in self.sp.items():
            if k in vec.sp:
                ans += v * vec.sp[k]
        return ans

