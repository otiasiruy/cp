from collections import Counter
from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        c = Counter()
        for x, y in dominoes:
            if x <= y:
                c[(x,y)] += 1
            else:
                c[(y,x)] += 1
        ans = 0
        for v in c.values():
            if v > 1:
                ans += (v * (v - 1)) / 2
        return int(ans)