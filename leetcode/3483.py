import itertools
from typing import List


class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        c = list(itertools.permutations(digits, 3))
        unq = set(c)
        diff = 0
        for i, j, k in unq:
            if i == 0:
                diff += 1
            elif k % 2 == 1:
                diff += 1
        return len(unq) - diff