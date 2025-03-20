from typing import List


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        da = [0] * (n + 1)
        for q in queries:
            da[q[0]] += 1
            da[q[1] + 1] -= 1
        for i in range(1, len(da)):
            da[i] += da[i - 1]
        for i in range(n):
            if nums[i] > da[i]:
                return False
        return True