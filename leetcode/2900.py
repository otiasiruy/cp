from typing import List


class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        mx = 0
        g = -1
        ans = []
        for i in range(n):
            g = groups[i]
            sub = [words[i]]
            for j in range(i + 1, n):
                if groups[j] != g:
                    g = groups[j]
                    sub.append(words[j])
            if mx < len(sub):
                mx = len(sub)
                ans = sub[:]
        return ans