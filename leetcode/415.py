from collections import deque


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n1 = len(num1) - 1
        n2 = len(num2) - 1
        n = max(n1, n2)
        ans = deque()
        d = {}
        for i in range(0, 10):
            for j in range(0, 10):
                d[str(i) + str(j)] = str(i+j)
        i = -1
        s = ''
        v = ''
        while i < n:
            i += 1
            v1 = v2 = '0'
            if n1 >= 0:
                v1 = num1[n1]
                n1 -= 1
            if n2 >= 0:
                v2 = num2[n2]
                n2 -= 1
            v = d[v1 + v2]
#            print(f"v {v}, v1 + v2 {v1 + v2}")
            if s != '':
#                print(f"v[-1] + s {v[-1] + s}")
                if len(v) > 1:
                    v2 = d[v[-1] + s]
                    v = v[0] + v2
                else:
                    v = d[v + s]
#                print(f"new v {v}")
            if len(v) == 1:
                ans.appendleft(v)
                s = ''
            else:
                ans.appendleft(v[-1])
                s = v[0]
#            print(f"v {v}, s {s}")
        if len(v) > 1:
            ans.appendleft(v[0])
        return ''.join(ans)