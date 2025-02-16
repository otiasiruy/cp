from typing import List


class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        n = len(pizzas)
        pizzas.sort()
        ans = 0
        pn = (int)(n / 4)
        if pn % 2 == 0:
            pn = (int)(pn / 2)
        else:
            pn = (int)(pn / 2) + 1

        r = n - 1
        l = 0
        for i in range(pn):
            print(pizzas[r])
            ans += pizzas[r]
            l += 3
            r -= 1

        i = 1
        while l < r:
            ans += pizzas[r - 1]
            r -= 2
            l += 2
            i += 1
        return ans
