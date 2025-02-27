from collections import defaultdict


class Solution:
    def repeatedCharacter(self, s: str) -> str:
        d = defaultdict(int)
        for c in s:
            if c in d and d[c] == 1:
                return c
            else:
                d[c] += 1
        return 'a'