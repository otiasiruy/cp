from collections import defaultdict
from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        m1 = defaultdict(int)
        m2 = defaultdict(int)
        for match in matches:
            m1[match[0]] += 1
            m2[match[1]] += 1
        ans = []
        l1 = []
        l2 = []
        for k, v in m1.items():
            if k in m1 and k not in m2:
                l1.append(k)
        for k, v in m2.items():
            if k in m2 and v == 1:
                l2.append(k)
        l1.sort()
        l2.sort()
        ans.append(l1)
        ans.append(l2)
        return ans