from collections import Counter


class Solution:
    def maxFreqSum(self, s: str) -> int:
        f = Counter(s)
        vo = {'a', 'e', 'i', 'o', 'u'}
        mc, mv = 0, 0
        for k, v in f.items():
            if k in vo:
                mv = max(mv, v)
            else:
                mc = max(mc, v)
        return mc + mv