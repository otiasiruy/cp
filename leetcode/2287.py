from collections import Counter


class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        d = Counter(s)
        d_target = Counter(target)
        ans = 101
        for k, v in d_target.items():
            if k in d:
                ans = min(ans, (int) (d[k]/v))
            else:
                return 0
        return ans