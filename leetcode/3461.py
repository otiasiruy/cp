from collections import deque


class Solution:
    def hasSameDigits(self, s: str) -> bool:
        dq = deque(map(int, s))
        while len(dq) > 2:
            new_dq = deque()
            for i in range(len(dq) - 1):
                new_dq.append((dq[i] + dq[i + 1]) % 10)
            dq = new_dq
        return True if dq[0] == dq[1] else False