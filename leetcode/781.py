from typing import List, Counter


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        c = Counter(answers)
        ans = 0
        for k, v in c.items():
            if k == 0:
                ans += v
            elif k == 1:
                r = v % (2)
                ans += v + r
            elif k + 1 < v:
                r = v // (k + 1)
                ans += (k + 1) * r + k + 1
            else:
                ans += k + 1
        return ans