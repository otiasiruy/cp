from collections import deque


class Solution:
    def removeStars(self, s: str) -> str:
        dq = deque()
        for c in s:
            if c == '*':
                dq.pop()
            else:
                dq.append(c)
        return ''.join(dq)