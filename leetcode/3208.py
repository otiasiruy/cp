from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        ans = 0
        n = len(colors)
        w = 0
        for i in range(n + k - 2):
            if w == k:
                w -= 1
            if i < n - 1:
                if colors[i] != colors[i + 1]:
                    if w == 0:
                        w += 2
                    else:
                        w += 1
                    if w == k:
                        ans += 1
                else:
                    w = 0
            else:
                if colors[i - n] != colors[i - n + 1]:
                    if w == 0:
                        w += 2
                    else:
                        w += 1
                    if w == k:
                        ans += 1
                else:
                    w = 0
        return ans