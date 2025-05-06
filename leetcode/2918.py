from typing import List


class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sm1 = sum(nums1)
        sm2 = sum(nums2)
        z1, z2 = 0, 0
        for i in nums1:
            if i == 0:
                z1 += 1
        for i in nums2:
            if i == 0:
                z2 += 1
        mn1 = sm1 + z1
        mn2 = sm2 + z2
        if (mn1 > mn2 and z2 == 0) or (mn2 > mn1 and z1 == 0):
            return -1
        return max(mn1, mn2)