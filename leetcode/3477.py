from typing import List


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        ans = 0
        n = len(fruits)
        for f in fruits:
            added = False
            for i in range(n):
                if f <= baskets[i]:
                    baskets[i] = 0
                    added = True
                    break
            if not added:
                ans += 1
        return ans