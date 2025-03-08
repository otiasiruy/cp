from collections import Counter


class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        n = len(s)
        if n < k:
            return 0
        ans = 0
        l = 0
        for i in range(k, n + 1):
            c = Counter(s[l:i])
            if len(c) == k:
                ans += 1
            l += 1
        return ans