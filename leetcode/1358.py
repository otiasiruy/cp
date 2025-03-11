from collections import defaultdict


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l = 0
        d = defaultdict(int)
        ans = 0
        n = len(s)
        for i in range(n):
            d[s[i]] += 1
            while len(d) == 3:
                ans += n - i
                if d[s[l]] > 1:
                    d[s[l]] -= 1
                else:
                    del d[s[l]]
                l += 1
        return ans
