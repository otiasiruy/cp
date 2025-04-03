from collections import deque
from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        dq = deque()
        for i in nums:
            if i % 2 == 0:
                dq.appendleft(i)
            else:
                dq.append(i)
        return list(dq)