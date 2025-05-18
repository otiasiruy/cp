from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        i = 0
        dq = deque()
        ra = di = 0
        for s in senate:
            dq.appendleft(s)
            if s == 'R':
                ra += 1
            else:
                di += 1

        r = d = 0
        while dq:
            s = dq.pop()
#            print(f"s {s}, d {d}, r {r}, ra {ra}, di {di}")
            if s == 'R' and d == 0:
                r += 1
                dq.appendleft(s)
            elif s == 'D' and r == 0:
                d += 1
                dq.appendleft(s)

            if s == 'R' and d > 0:
                ra -= 1
                d -= 1
            elif s == "D" and r > 0:
                di -= 1
                r -= 1
            if ra == 0:
                return "Dire"
            if di == 0:
                return "Radiant"