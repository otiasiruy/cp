class Solution:
    def numTilings(self, n: int) -> int:
#        1 - 1
#        2 - 2
#        3 - 5
#        4 - 2*3 + 1 (11)
#        5 - 2*4 + 2 (24)
#        6 - 2*5 + 3 (48 + 5)
#        7 - 2*6 + 4 (106 + 11)
        dp = [0] * 1001
        dp[1] = 1
        dp[2] = 2
        dp[3] = 5
        if n < 4:
            return dp[n]
        for i in range(4, n + 1):
            dp[i] = (2 * dp[i - 1] + dp[i - 3]) % (10**9 + 7)
        return dp[n]