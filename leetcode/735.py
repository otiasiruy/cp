from collections import deque
from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        dq = deque()
        for a in asteroids:
            dq.append(a)
            while dq and len(dq) > 1:
                n = len(dq)
                if dq[n - 2] > 0 and dq[n - 1] < 0:
                    if abs(dq[n - 2]) == abs(dq[n - 1]):
                        dq.pop()
                        dq.pop()
                    elif abs(dq[n - 2]) > abs(dq[n - 1]):
                        dq.pop()
                    else:
                        dq.pop()
                        dq[len(dq) - 1] = a
                else:
                    break
        return list(dq)