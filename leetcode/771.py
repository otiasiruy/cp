class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s = set(jewels)
        ans = 0
        for c in stones:
            if c in s:
                ans += 1
        return ans