from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def binarySearch(l, r, x):
            while l <= r:
                m = (l + r) // 2
                if x + numbers[m] == target:
                    return m
                elif x + numbers[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return -1
        n = len(numbers)
        ans = []
        for i in range(n - 1):
            ret = binarySearch(i + 1, n - 1, numbers[i])
            if ret != -1:
                return [i + 1, ret + 1]
        return []