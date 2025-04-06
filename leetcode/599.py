import heapq
from collections import defaultdict
from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        l = []
        d1, d2 = defaultdict(int), defaultdict(int)
        n1, n2 = len(list1), len(list2)
        for i in range(n1):
            d1[list1[i]] = i
        for i in range(n2):
            d2[list2[i]] = i
        for k, v in d1.items():
            if k in d2:
                heapq.heappush(l, (v + d2[k], k))
        ans = []
        v, k = heapq.heappop(l)
        ans.append(k)
        ref_v = v
        while l and ref_v == v:
            ref_v, k = heapq.heappop(l)
            if ref_v == v:
                ans.append(k)
        return ans