from random import random
from typing import List


class Solution:

    def __init__(self, w: List[int]):
        self.px = []
        self.total = 0
        for i in w:
            self.total += i
            self.px.append(self.total)

    def pickIndex(self) -> int:
        x = random.random() * self.total
        l = 0
        r = len(self.px) - 1
        while l < r:
            m = (l + r) // 2
            if self.px[m] < x:
                l = m + 1
            elif self.px[m] > x:
                r = m
        return l
