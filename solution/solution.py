import os
import sys
from math import ceil

if os.path.exists('input'):
    sys.stdin = open('input', 'r')
    sys.stdout = open('output', 'w')

def solve():
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        d = list(map(int, input().split()))
        d = [None]+d
        l = [[None]]
        r = [[None]]
        for _ in range(n):
            x, y = list(map(int, input().split()))
            l.append(x)
            r.append(y)
        lw = [0]*(n+1)
        hi = [0]*(n+1)
        p = True
        for i in range(1, n+1):
            if d[i] == 0:
                plw, phi = lw[i-1], hi[i-1]
            elif d[i] == 1:
                plw, phi = lw[i-1] + 1, hi[i-1] +1
            else:
                plw, phi = lw[i-1], hi[i-1]+1

            lw[i], hi[i] = max(plw, l[i]), min(phi, r[i])
            if lw[i] > hi[i]:
                print(-1)
                p = False
                break
        if not p:
            continue
        h = [0] * (n +1)
        h[n] = lw[n]

        for i in range(n, 0, -1):
            if d[i] != -1:
                h[i-1] = h[i] - d[i]
            else:
                if lw[i-1] <= h[i] <= hi[i-1]:
                    h[i-1] = h[i]
                    d[i] = 0
                else:
                    h[i-1] = h[i]- 1
                    d[i] = 1
        print(*d[1:])




if __name__ == "__main__":
    solve()