class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            ans += (i + 1) * (27 - (ord(s[i]) - 96))
        return ans