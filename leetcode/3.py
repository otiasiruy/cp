class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ndup = set()
        l = 0
        n = len(s)
        ans = 0
        for i in range(n):
            if s[i] not in ndup:
                ndup.add(s[i])
                ans = max(ans, len(ndup))
            else:
                while s[i] in ndup:
                    ndup.remove(s[l])
                    l += 1
                ndup.add(s[i])
        return ans