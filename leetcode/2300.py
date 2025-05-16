from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        def bs(s):
            l = 0
            r = len(potions) - 1
            while l <= r:
                m = l + (r - l) // 2
                if s * potions[m] == success:
                    return m
                elif s * potions[m] > success:
                    r = m - 1
                else:
                    l = m + 1
            return l

        potions.sort()
        ans = []
        memo = {}
        for s in spells:
            if s in memo:
                ans.append(memo[s])
                continue
            i = bs(s)
#            print(f"s {s}, i {i}")
            while 0 <= i < len(potions) and potions[i] * s >= success:
                i -= 1
#            print(i)
            if i == 0 and potions[i] * s >= success:
                ans.append(len(potions))
            elif i == 0 and potions[i] * s < success:
                ans.append(len(potions) - 1)
            elif i == len(potions):
                ans.append(0)
            else:
                ans.append(len(potions) - i - 1)
            memo[s] = ans[-1]
        return ans