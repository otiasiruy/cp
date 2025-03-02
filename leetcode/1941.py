from collections import Counter


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        if len(s) == 1:
            return True
        hist = Counter(s)
        s = set()
        for v in hist.values():
            s.add(v)
        return True if len(s) == 1 else False