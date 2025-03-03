from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hist = Counter(text)
        ref = Counter("balloon")
        ans = 10**4
        for k, v in ref.items():
            if k in hist:
                ans = min(ans, (int) (hist[k]/v))
            else:
                ans = 0
                break
        return ans