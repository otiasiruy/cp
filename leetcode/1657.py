from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        n1 = len(word1)
        n2 = len(word2)
        if n1 != n2:
            return False
        c1 = Counter(word1)
        c2 = Counter(word2)
        k1 = set(c1.keys())
        k2 = set(c2.keys())
        if len(k1) != len(k2):
            return False
        for i in k1:
            if i not in k2:
                return False
        l1 = list(c1.values())
        l2 = list(c2.values())
        l1.sort()
        l2.sort()
        m1 = len(l1)
        m2 = len(l2)
        if m1 != m2:
            return False
        for i in range(m1):
            if l1[i] != l2[i]:
                return False
        return True