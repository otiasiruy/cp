from collections import defaultdict
from typing import List


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        c = defaultdict(int)
        for w in words:
            c[w] += 1
        cnt = 0
        eq = False
        seen = set()
        for w in words:
            #print(f"w {w}, cnt {cnt}, eq {eq}, w[0] == w[1] {w[0] == w[1]}")
            if w not in seen and w[0] != w[1]:
                m = min(c[w], c[w[1] + w[0]])
                cnt += m*4
                seen.add(w)
                seen.add(w[1] + w[0])
                #print(w)
            elif w not in seen and w[0] == w[1]:
                seen.add(w)
                if c[w] % 2 != 0:
                    eq = True
                if c[w] > 1:
                    cnt += 4*(c[w]//2)
        #print(f"eq {eq}, cnt {cnt}")
        return cnt + 2 if eq else cnt