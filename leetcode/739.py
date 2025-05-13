from collections import deque
from typing import List


class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        n = len(temp)
        ms = deque()
        ans = [0] * n
        for i in range(n):
            while ms and ms[-1][1] < temp[i]:
                ans[ms[-1][0]] = i - ms[-1][0]
                ms.pop()
            ms.append((i, temp[i]))
        return ans