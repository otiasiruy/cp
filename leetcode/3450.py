from collections import defaultdict
from typing import List


class Solution:
    def maxStudentsOnBench(self, students: List[List[int]]) -> int:
        d = defaultdict(set)
        for s in students:
            d[s[1]].add(s[0])
        ans = 0
        for k, v in d.items():
            ans = max(ans, len(v))
        return ans