from collections import defaultdict


class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        n = len(s)
        c = defaultdict(int)
        for i in range(n):

            if i < k:
                c[s[i]] += 1
            else:
                c[s[i - k]] -= 1
                c[s[i]] += 1

            if c[s[i]] == k and i - k + 1 == 0 and i == n - 1:
                return True
            elif i - k + 1 == 0 and c[s[i]] == k and i < n - 1 and s[i + 1] != s[i]:
                return True
            elif i - k + 1 > 0 and c[s[i]] == k and i == n - 1 and s[i - k] != s[i]:
                return True
            elif i - k + 1 > 0 and c[s[i]] == k and i < n - 1 and s[i - k] != s[i] and s[i + 1] != s[i]:
                return True

        return False
