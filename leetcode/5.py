class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s
        dp = [[False] * n for _ in range(n)]
        ans = ""
        for i in range(n):
            dp[i][i] = True
            if len(ans) < len(s[i : i + 1]):
                ans = s[i : i + 1]
            if i < n - 1 and s[i] == s[i + 1]:
                dp[i][i + 1] = True
                if len(ans) < len(s[i : i + 2]):
                    ans = s[i : i + 2]
        for j in range(2, n):
            for i in range(n - 1):
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    if len(ans) < len(s[i : j + 1]):
                        ans = s[i : j + 1]
        return ans