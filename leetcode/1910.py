from collections import deque

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        dq = deque()
        n = len(s)
        for i in range(n):
            dq.append(s[i])
            if "".join(dq).find(part) != -1:
                for _ in range(len(part)):
                    dq.pop()
        return "".join(dq)