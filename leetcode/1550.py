from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        odds = 0
        for i in arr:
            if i % 2 != 0:
                if odds == 2:
                    return True
                odds += 1
            else:
                odds = 0
        return False