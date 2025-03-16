from collections import defaultdict


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = defaultdict()
        words = s.split()
        w = 0
        s = set()
        for c in pattern:
            if w >= len(words):
                return False
            if c not in d:
                d[c] = words[w]
                if words[w] in s:
                    return False
                s.add(words[w])
            elif d[c] != words[w]:
                return False
            w += 1
        if w < len(words):
            return False
        return True