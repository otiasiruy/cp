from typing import List


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        perm = [0] * (n + 1)
        l = 0
        r = n
        for i in range(0, n):
            if s[i] == 'I':
                perm[i] = l
                l += 1
                perm[i + 1] = l
            else:
                perm[i + 1] = perm[i]
                perm[i] = r
                r -= 1
        return perm