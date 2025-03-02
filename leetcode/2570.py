from collections import defaultdict
from typing import List


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        ans = []
        m = defaultdict(int)
        for id, v in nums1:
            m[id] += v
        for id, v in nums2:
            m[id] += v
        for i in range(1001):
            if i in m:
                ans.append([i, m[i]])
        return ans