class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        letters = set(s)
        ans = 0
        for c in letters:
            l = s.find(c)
            r = s.rfind(c)
            b = set()
            for i in range(l + 1, r):
                b.add(s[i])
            ans += len(b)
        return ans