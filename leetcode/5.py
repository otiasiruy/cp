class Solution:
    def longestPalindrome(self, s: str) -> str:
        def valid(s):
            l = 0
            r = len(s) - 1
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        n = len(s)
        if n == 1:
            return s
        dp = [0] * n
        dp[0] = 1
        dp[1] = dp[0]
        ans = s[0]
        if valid(s[0:2]):
            dp[1] = 2
            ans = s[0:2]
        for i in range(2, n):
            l = 0
            while not valid(s[l:i + 1]):
                l += 1
            dp[i] = max(dp[i - 1], i - l + 1)
            if dp[i] > dp[i - 1]:
                ans = s[l:i + 1]
        return ans